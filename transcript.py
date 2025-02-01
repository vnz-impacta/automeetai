import os
import assemblyai as aai

def transcribe():

    aai.settings.api_key = os.getenv("ASSEMBLYAI_KEY")

    FILE_URL = "exported_audio.mp3"

    config = aai.TranscriptionConfig(
        speaker_labels=True,
        speakers_expected=2,
        language_code="pt",
        speech_model=aai.SpeechModel.best)

    transcriber = aai.Transcriber(config=config)

    transcript = transcriber.transcribe(FILE_URL)

    if transcript.status != aai.TranscriptStatus.error:
        with open("transcription.txt", "w", encoding="utf-8") as file:
            for utterance in transcript.utterances:
                file.write(f"Speaker {utterance.speaker}: {utterance.text}\n")

