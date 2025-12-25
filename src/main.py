from fastapi import FastAPI
from tts_message import TTSMessageData

app = FastAPI()

@app.get("/")
async def service_status():
    return { "message" : "service is up" }

@app.get("/lang/{speaker_id}")
async def speaker_language(speaker_id: int):
    return { "speaker language": None }

@app.get("/voice/{speaker_id}")
async def speaker_voice(speaker_id: int):
    return { "speaker voice": None }

@app.get("/gender/{speaker_id}")
async def speaker_gender(speaker_id: int):
    return { "speaker gender": None }

@app.post("/speak/{speak_id}")
async def speak(speaker_id: int, message: TTSMessageData):
    return { "message": message.messageContent }
    