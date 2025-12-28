from google.cloud import texttospeech
from tts_types import TTSParams

class GoogleBackend:
    lang_map = {
        "en": "en-US",
        "en-alt": "en-GB",
        "fr": "fr-FR",
        "fr-alt": "fr-CA"
    }

    name = {
        "male": {
            "en": "en-US-Standard-A",
            "en-alt": "en-GB-Standard-B",
            "fr": "fr-FR-Standard-F",
            "fr-alt": "fr-CA-Standard-D" 
        },
        "female": {
            "en": "en-US-Standard-C",
            "en-alt": "en-GB-Standard-A",
            "fr": "fr-FR-Standard-F",
            "fr-alt": "fr-CA-Standard-A"
        }
    }


    def __init__(self, params: TTSParams) -> None:
        self.client = texttospeech.TextToSpeechAsyncClient()

        # Default to 'en' if language is invalid or not provided
        lang_key = params.language if params.language in self.lang_map else "en"
        language_code = self.lang_map[lang_key]

        # Default to 'female' if gender is invalid or not provided
        gender_key = params.gender if params.gender in self.name else "female"

        # Determine voice name
        # If voice is explicitly provided, use it. Otherwise, look up in map.
        voice_name = params.voice
        if not voice_name:
            voice_name = self.name[gender_key].get(lang_key)
            # Fallback
            if not voice_name:
                voice_name = self.name["female"]["en"]

        self.voice_params = texttospeech.VoiceSelectionParams(
            language_code=language_code,
            name=voice_name
        )

        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.OGG_OPUS
        )

    async def synthesize(self, message: str) -> bytes:
        input_text = texttospeech.SynthesisInput(text=message)
        response = await self.client.synthesize_speech(
            input=input_text,
            voice=self.voice_params,
            audio_config=self.audio_config
        )
        return response.audio_content 