from flask import Flask, request, jsonify, render_template
import difflib
from spellchecker import SpellChecker

app = Flask(__name__)
qa_data = [ 
    # ⛔ Paste your full JSON Q&A data here
    {
        "id": "Admission in collage.",
        "questions": [
            "admission in mvit clg",
            "admission in mit clg",
            "I want to put admission in mvit clg",
            "I want to put admission in mit clg",
            "I want to put admission for AIML course in your collage.",
            "I want to put admission for IOT course in your collage.",
            "I want to put admission for FT course in your collage.",
            "I want to put admission for RA course in your collage.",
            "I want to put admission for MECH course in your collage.",
            "I want to put admission for IT course in your collage.",
            "I want to put admission for CSE course in your collage.",
            "I want to put admission for ECE course in your collage.",
            "I want to put admission for EEE course in your collage.",
            "admission for EEE."
        ],
        "answer": "https://forms.gle/rCcmmLxLe1waj3tJ8 (you can put your admission by using this link)"
    }]



# PREPROCESS once at startup for fast lookups
question_to_answer = {}
all_questions = []

for entry in qa_data:
    for q in entry["questions"]:
        ql = q.lower().strip()
        question_to_answer[ql] = entry["answer"]
        all_questions.append(ql)

# Create spellchecker once
spell = SpellChecker()

def find_best_match(user_input):
    ui = (user_input or "").lower().strip()
    if not ui:
        return "Please type a question."
    if ui in question_to_answer:
        return question_to_answer[ui]
    match = difflib.get_close_matches(ui, all_questions, n=1, cutoff=0.60)
    if match:
        return question_to_answer[match[0]]
    return "Answer not available."


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])

def get_bot_response():
    data = request.get_json(force=True) or {}
    user_message = data.get('msg', '')

    print(f"Received user message: {user_message}")

    # Correct typos word-by-word
    words = user_message.lower().split()
    corrected_words = [spell.correction(word) for word in words]
    corrected_text = " ".join(corrected_words)
    print(f"Corrected user input: {corrected_text}")

    reply = find_best_match(corrected_text)
    print(f"Bot reply: {reply}")

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
