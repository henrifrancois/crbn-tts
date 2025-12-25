from typing_extensions import Optional
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
