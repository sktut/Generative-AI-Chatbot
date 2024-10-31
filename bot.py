import openai

openai.api_key = 'NULL'    --write accordingly

def chat_with_bot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

if __name__ == "__main__":
    print("Welcome to the Generative AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chat_with_bot(user_input)
        print(f"Bot: {response}")
