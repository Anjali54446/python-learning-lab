# Integrated Challenge: GenAI-style request data
request = {
    "model": "my-model",
    "messages": [
        {
            "role": "user",
            "content": "Explain Python"
        }
    ],
    "temperature": 0.2
}

user_message = request["messages"][0]["content"]
print("User message:", user_message)
