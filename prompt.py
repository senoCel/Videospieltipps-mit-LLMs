import ollama
import time

modelle = [
    "deepseek-r1:8b",
    "mistral:7b",
    "falcon3:7b",
    "llama3.1:8b",
    "qwen2.5:7b",
]

messages = [
    {
        "role": "system",
        "content": "Du bist ein hilfreicher Assistent, der wenn nötig Tipps für Videospiele geben kann:",
    },
    {
        "role": "user",
        "content": "Ich spiele Assasins Creed Origins. Erkläre, wie ich meine Waffen verbessern kann und wo ich die besten Waffen finde.",
    },
]

for modell in modelle:
    start = time.time()
    stream = ollama.chat(
        model=modell,
        stream=True,
        options={"temperature": 0.3, "seed": 0, "num_predict": 1024},
        messages=messages,
    )
    response = "".join([chunk["message"]["content"] for chunk in stream])
    end = time.time()
    print(f"\n{modell}:")
    print(response)
    # print(f"Antwortzeit: {end - start:.2f} Sekunden")