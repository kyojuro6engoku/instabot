import re
import os
from os import environ
from pyrogram import enums
from Script import script

import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client


class evamaria(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            sleep_threshold=60
        )

# Bot information
API_ID = int(os.environ.get('API_ID', '5370426'))
API_HASH = os.environ.get('API_HASH', '9411fec0e459d57458962a3c0ee78de5')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '6390496152:AAElWXKiIeMSYJZ4InTVAexWJOkqeraEenA')



                           
