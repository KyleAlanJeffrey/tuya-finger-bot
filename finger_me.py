import pygatt
import hashlib
from pyfingerbot import (
    XRequest,
    Coder,
    TuyaDataPacket,
    BleReceiver,
    SecretKeyManager,
    FingerBot,
)
import time
from struct import unpack
from Crypto.Cipher import AES
from binascii import unhexlify, hexlify
import pydotenv

pydotenv.load_dotenv()

# Use https://github.com/redphx/tuya-local-key-extractor to get these values
LOCAL_KEY = pydotenv.get("LOCAL_KEY")
MAC = pydotenv.get("MAC")
UUID = pydotenv.get("UUID")
DEV_ID = pydotenv.get("DEV_ID")

if not LOCAL_KEY or not MAC or not UUID or not DEV_ID:
    print("Please set LOCAL_KEY, MAC, UUID, and DEV_ID in your .env file")
    exit(1)

fingerbot = FingerBot(MAC, LOCAL_KEY, UUID, DEV_ID)
fingerbot.connect()
