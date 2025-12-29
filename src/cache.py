from enum import Enum
import json

class Settings(Enum):
    LANGAUGE = "lang"
    VOICE = "voice"
    GENDER = "gender"

class KVStore:
    def __init__(self) -> None:
        self.store = {}
        pass

    def get(self, userId: str, key: str) -> str:
        if userId in self.store and key in self.store[userId]:
            return self.store.get(userId)[key]
        return ""

    def set(self, userId: str, key: str, value: str) -> bool:
        if userId not in self.store:
            self.store[userId] = {}
        self.store[userId][key] = value
        return True
         

    def remove(self, key: str) -> bool:

        pass 

    def remove_user(self, userId: str, key: str) -> bool:
        if userId not in self.store:
            return False
        del self.store[userId]
        

    def list_keys(self) -> list[str]:
        keys = []
        for user in self.store.keys():
            for key in self.store[user].keys():
                keys.append(f"{user}:{key}")  # or however you want to format it
        return keys

    def list_user_keys(self, userId : str) -> [str]:
        keys = []
        for key in self.store[userId]:
            keys.append(f"{userId}:{key}")
        return keys