import os
import json

# ✅ Replace with your actual intents folder path
intents_dir = r"C:\Users\haris\Downloads\Chrome Downloads\chat-Bot\intents"
output_file = "usersays_questions.json"

result = {}

for filename in os.listdir(intents_dir):
    if "usersays" in filename and filename.endswith(".json"):
        intent_name = filename.split("_usersays")[0]
        filepath = os.path.join(intents_dir, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                questions = []

                for entry in data:
                    text_parts = entry.get("data", [])
                    phrase = "".join(part.get("text", "") for part in text_parts)
                    if phrase:
                        questions.append(phrase)

                if questions:
                    result[intent_name] = questions

            except Exception as e:
                print(f"❌ Error reading {filename}: {e}")

# Save all extracted questions
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"✅ Training questions extracted to: {output_file}")
