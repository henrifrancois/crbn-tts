from backends.piper import PiperBackend
from tts_types import TTSMessageData, TTSParams, GenderOptions, LanguageOptions

class TTSService:

    def __init__(self) -> None:
        self.piper_client = PiperBackend()

    async def consume(self, message: TTSMessageData, params : TTSParams):
        kwargs = {}
        if params.gender:
            kwargs['gender'] = params.gender
        if params.language:
            kwargs['language'] = params.language
        response = await self.piper_client.synthesize(message.messageContent, **kwargs)
        return response
        

    def cacheRetrieve():
        pass

    def route(self) -> None:
        pass
    