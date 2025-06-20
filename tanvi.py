import openai

# 🔑 Replace with your actual API key
openai.api_key = "YOUR_API_KEY"

def ask_chatgpt(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    question = "Hello, how are you?"
    answer = ask_chatgpt(question)
    print("ChatGPT:", answer)
