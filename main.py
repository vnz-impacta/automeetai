from extract_audio import mp4_to_mp3
from transcript import transcribe
from ata_writer import conversa_com_openai

mp4_filename = "entrevista de Boechat com Jô Soares curto.mp4"
mp3_filename = 'exported_audio.mp3'

print("Extraindo áudio")
mp4_to_mp3(mp4_filename, mp3_filename)

print("Transcrevendo")
transcribe()

system_prompt = "Com base na Transcrição, identifique quem são os Speakers e depois escreva uma ata da entrevista."
with open("transcription.txt", "r", encoding="utf-8") as file:
    user_prompt = file.read()
print("Fazendo Ata")
conversa_com_openai(system_prompt, user_prompt)