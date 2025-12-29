import wave
import io
import os
import subprocess
from piper import PiperVoice
from tts_types import TTSParams

class PiperBackend:
    lang_map = {
        "en": "en_US",
        "en-alt": "en_GB",
        "fr": "fr_FR",
        "fr-alt": "fr_FR" # Fallback or distinct if available
    }

    # Map (gender, lang_code) -> model_filename (without .onnx extension)
    # Assuming files are in 'voices/' directory relative to project root
    model_map = {
        "male": {
            "en": "en_US-lessac-medium",
            "en-alt": "en_GB-alan-medium",
            "fr": "fr_FR-siwis-medium", 
            "fr-alt": "fr_FR-siwis-medium"
        },
        "female": {
            "en": "en_US-libritts-high",
            "en-alt": "en_GB-jenny_dioco-medium",
            "fr": "fr_FR-siwis-medium", # Using same for now as placeholders
            "fr-alt": "fr_FR-siwis-medium"
        }
    }

    def __init__(self) -> None:
        self.voices_dir = os.path.join(os.getcwd(), "voices")
        self.voice = {}

    def get_voice(self, gender="male", language="en") -> PiperVoice:
        #First check if voice is in dict
        #self.voices_dir = os.path.join(os.getcwd(), "voices")
        
        # Default to 'en'
        lang_key = language if language in self.lang_map else "en"
        # Default to 'female'
        gender_key = gender if gender in self.model_map else "female"
        

        model_name = self.model_map[gender_key].get(lang_key)

        if model_name in self.voice:
            #if we already have the voice loaded, then we can skip
            return self.voice[model_name]
        if not model_name:
            model_name = "en_US-libritts-high" # Ultimate fallback

        model_path = os.path.join(self.voices_dir, f"{model_name}.onnx")
        config_path = os.path.join(self.voices_dir, f"{model_name}.onnx.json")

        if os.path.exists(model_path) and os.path.exists(config_path):
            self.voice[model_name] = PiperVoice.load(model_path, config_path=config_path)
            return self.voice[model_name]
        else:
            # For now, we print a warning or handle gracefully if files are missing
            # In a real scenario, we might download them or raise an exception
            print(f"Warning: Voice model not found at {model_path}")

    

    async def synthesize(self, message: str, gender="female", language="en" ) -> bytes:
        try:
            voice = self.get_voice(gender, language)
            print(f"Number of speakers: {voice.config.num_speakers}")
        except:
            raise RuntimeError("Piper voice backend not initialized correctly (model missing).")

        
       # Generate WAV in memory
 # Generate WAV in memory
        with io.BytesIO() as wav_io:
            with wave.open(wav_io, "wb") as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)
                wav_file.setframerate(voice.config.sample_rate)
                voice.synthesize_wav(message, wav_file)
            
            wav_bytes = wav_io.getvalue()
        
        # USE FOR DEBBUGING, this will write to a .wav file to ensure it works
        #with open("output.wav", "wb") as f:
       #      f.write(wav_bytes)
            
        # Convert to OGG OPUS using ffmpeg
        try:
            # -loglevel quiet to reduce noise
            process = subprocess.run(
                ["ffmpeg", "-f", "wav", "-i", "pipe:0", "-c:a", "libopus", "-f", "ogg", "pipe:1", "-loglevel", "quiet"],
                input=wav_bytes,
                capture_output=True,
                check=True
            )
            with open("output.opus", "wb") as f:
                f.write(process.stdout)
            return process.stdout
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"Audio conversion failed or ffmpeg not found: {e}. Returning WAV.")
            return wav_bytes 