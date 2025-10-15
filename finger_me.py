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

# Use https://github.com/redphx/tuya-local-key-extractor to get these values
LOCAL_KEY = "yK2Ki5O8&*&T)uP?"
MAC = "DC:23:52:10:34:55"
UUID = "uuid8ec0b0bb5de0"
DEV_ID = "ebcb70uimovk0dc5"

if not LOCAL_KEY or not MAC or not UUID or not DEV_ID:
    print("Please set LOCAL_KEY, MAC, UUID, and DEV_ID in your .env file")
    exit(1)

fingerbot = FingerBot(MAC, LOCAL_KEY, UUID, DEV_ID)
fingerbot.connect()

while True:
    input("Press Enter to activate the finger bot...")
    fingerbot.finger()