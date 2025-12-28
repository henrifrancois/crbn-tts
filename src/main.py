from fastapi import FastAPI
from tts_types import TTSMessageData

app = FastAPI()

@app.get("/")
async def service_status():
    return { "message" : "service is up" }

@app.get("/lang/{speaker_id}")
async def speaker_language(speaker_id: int):
    # TODO: return language from speaker ID lookup
    return { "speaker language": None }

@app.get("/voice/{speaker_id}")
async def speaker_voice(speaker_id: int):
    # TODO: return voice string from speaker ID lookup
    return { "speaker voice": None }

@app.get("/gender/{speaker_id}")
    # TODO: return voice 'gender' from speaker ID lookup
async def speaker_gender(speaker_id: int):
    return { "speaker gender": None }

@app.post("/speak")
async def speak(message: TTSMessageData):
    # TODO: return audio file from transcription
    return { "message": message.messageContent }
    