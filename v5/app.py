from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

# Sample chatbot logic
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.json.get("msg").lower()

    if "college building" in user_input:
        response = {
            "text": "Here are some college pictures you asked for:",
            "images": [
                url_for('static', filename='images/building1.jpg'),
                url_for('static', filename='images/building2.jpg'),
                url_for('static', filename='images/building3.jpg')
            ]
        }
    elif "library" in user_input:
        response = {
            "text": "Here are library pictures:",
            "images": [
                url_for('static', filename='images/library1.jpg'),
                url_for('static', filename='images/library2.jpg')
            ]
        }
    else:
        response = {"text": "Sorry, I don’t have pictures for that.", "images": []}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
