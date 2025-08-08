import os
import json

# ✅ Your Dialogflow 'intents' folder path
intents_dir = r"C:\Users\haris\Downloads\Chrome Downloads\chat-Bot\intents"
output_file = "answers_only.json"

answers = {}

for filename in os.listdir(intents_dir):
    if "_usersays" not in filename and filename.endswith(".json"):
        intent_name = filename.replace(".json", "")
        filepath = os.path.join(intents_dir, filename)

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

                # Drill down to: responses → messages → speech[0]
                responses = data.get("responses", [])
                if responses:
                    messages = responses[0].get("messages", [])
                    for msg in messages:
                        speech = msg.get("speech", [])
                        if isinstance(speech, list) and speech:
                            answers[intent_name] = speech[0]
                            break
                        elif isinstance(speech, str):
                            answers[intent_name] = speech
                            break

        except Exception as e:
            print(f"❌ Error in {filename}: {e}")

# ✅ Save result
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(answers, f, indent=2, ensure_ascii=False)

print(f"✅ Answers saved to {output_file}")

