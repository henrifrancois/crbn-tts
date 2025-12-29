from backends.piper import PiperBackend
from tts_types import TTSMessageData, TTSParams, GenderOptions, LanguageOptions

class TTSService:

    def __init__(self) -> None:
        self.piper_client = PiperBackend()

    async def consume(self, message: TTSMessageData):
        #TODO Retrive from cache and get user settings
        response = await self.piper_client.synthesize(message.messageContent, GenderOptions.MALE.value, LanguageOptions.ENGLISH.value)
        return response
        

    def cacheRetrieve():
        pass

    def route(self) -> None:
        pass
    