# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "26797881"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "9699262c708c2e45ba18bfce925ed5ed")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7513124783:AAHNbZKlClU_5xjtLG3BZc6ffmopnwS5h1s")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@Allextract_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "6567162029"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5170349400").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002303981738"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://sevmamra01:<db_password>@cluster0.ff29e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002303981738"))

