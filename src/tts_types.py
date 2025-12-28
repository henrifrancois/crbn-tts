from typing_extensions import Optional
from enum import Enum
from dataclasses import dataclass

@dataclass
class TTSMessageData:
    guildId: str | None
    channelId: str
    userId: str
    username: str
    displayName: str
    messageContent: str 
    timestamp: str 
    messageId: str 
    voice: str | None


@dataclass
class TTSParams:
    voice: str | None
    gender: str | None 
    language: str | None 

class LanguageOptions(Enum):
    ENGLISH = "en"
    ENGLISH_ALT = "en-alt"
    FRENCH = "fr"
    FRENCH_ALT = "fr-alt"

class GenderOptions(Enum):
    MALE = "male"
    FEMALE = "female"
    NEUTRAL = "neutral"