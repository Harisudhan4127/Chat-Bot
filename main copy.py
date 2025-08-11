import openai
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"
user_input = input("you: ")
reply=""
response = openai.ChatCompletion.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "system", "content": "you are a helpful"},
                   {"role": "user", "content": user_input},
                   {"role": "assistant","content": reply}])
reply = response['choices'][0]['message']['content']
print(f"chatbot: {reply}\n")



    