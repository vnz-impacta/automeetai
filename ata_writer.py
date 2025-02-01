import os
from openai import OpenAI

def conversa_com_openai(system_prompt, user_prompt):
    
    openai_client = OpenAI(
        api_key=os.getenv("OPENAI_KEY")
    )

    resposta = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        temperature=0.7,
        messages = [
            { 
                "role": "system", 
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    ata_content = resposta.choices[0].message.content

    with open("ata.txt", "w", encoding="utf-8") as file:
        file.write(ata_content)

if __name__ == "__main__":
    system_prompt = "Com base na Transcrição, identifique quem são os Speakers e depois escreva uma ata da entrevista."
    
    try:
        with open("transcription.txt", "r", encoding="utf-8") as file:
            user_prompt = file.read()
    except FileNotFoundError:
        user_prompt = "Transcrição não encontrada."

    conversa_com_openai(system_prompt, user_prompt)