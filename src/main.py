from fastapi import FastAPI
from tts_types import TTSMessageData
from tts_service import TTSService
from cache import KVStore, Settings
import uvicorn

app = FastAPI()
tts_service = TTSService()
cache = KVStore()
@app.get("/")
async def service_status():
    return { "message" : "service is up" }

@app.get("/lang/{speaker_id}")
async def speaker_language(speaker_id: int):
    value = cache.get(speaker_id, Settings.LANGAUGE)
    return { "speaker language": value }

@app.get("/voice/{speaker_id}")
async def speaker_voice(speaker_id: int):
    value = cache.get(speaker_id, Settings.VOICE)
    return { "speaker voice": value }

@app.get("/gender/{speaker_id}")
async def speaker_gender(speaker_id: int):
    value = cache.get(speaker_id, Settings.GENDER)
    return { "speaker gender": value }

@app.post("/speak")
async def speak(message: TTSMessageData):
    #TODO: get settings from KVStore
    response = await tts_service.consume(message)
    # TODO: return audio file from transcription
    return { "message": message.messageContent }
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)