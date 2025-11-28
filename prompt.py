import ollama
import time

start = time.time()

stream = ollama.chat(
    model="qwen2.5:7b",
    stream=True,
    options={
        "temperature": 0.2,
        "seed": 0,
    },
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that provides tips for the computer game Minecraft:",
        },
        {
            "role": "user",
            "content": "What are 5 useful tips for the computer game Minecraft?",
        },
    ],
)

response = "".join([chunk["message"]["content"] for chunk in stream])
end = time.time()
print(response)
print(f"Antwortzeit: {end - start:.2f} Sekunden")