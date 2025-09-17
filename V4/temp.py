from flask import Flask, request, jsonify
import difflib
from spellchecker import SpellChecker

app = Flask(__name__)

# Prepare spell checker
spell = SpellChecker()

# Extract questions list
questions = [item["question"] for item in qa_data]

def get_answer(user_input):
    # Step 1: Spell correction
    corrected_words = [spell.correction(word) or word for word in user_input.split()]
    corrected_input = " ".join(corrected_words)

    # Step 2: Find best match
    match = difflib.get_close_matches(corrected_input, questions, n=1, cutoff=0.6)

    # Step 3: Return answer if found
    if match:
        for item in qa_data:
            if item["question"] == match[0]:
                return item["answer"]

    # Step 4: Fallback response
    return "Sorry, I don't know that yet. Please try another question."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    response = get_answer(user_message)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
