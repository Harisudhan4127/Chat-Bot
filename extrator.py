import os
import json

# ✅ Update this to your correct path (use double backslashes or raw string)
intents_dir = r"C:\Users\haris\Downloads\Chrome Downloads\chat-Bot\intents"
output_file = "dialogflow_intents_kv.json"

intent_kv = {}

for filename in os.listdir(intents_dir):
    if filename.endswith(".json"):
        filepath = os.path.join(intents_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)

                # Handle follow-up intents stored as lists
                if isinstance(data, list):
                    data = data[0]

                if isinstance(data, dict):
                    intent_name = filename.replace(".json", "")
                    responses = data.get("responses", [])
                    if responses:
                        messages = responses[0].get("messages", [])
                        for msg in messages:
                            if msg.get("type") == "0":
                                speech = msg.get("speech")
                                if isinstance(speech, list) and speech:
                                    intent_kv[intent_name] = speech[0]
                                    break
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Save output as readable key-value JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(intent_kv, f, ensure_ascii=False, indent=2)

print(f"✅ Key-value intent data saved to: {output_file}")
