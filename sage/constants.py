from jinja2 import Environment, FileSystemLoader
import os

TOKEN = os.getenv("DISCORD_TOKEN", None)

JINJA_ENV = Environment(loader=FileSystemLoader('templates'))

# User Related
PFP_SAUCE_LINK = "https://www.pixiv.net/en/artworks/70160872"
DISCORD_ID = None  # 376012343777427457


# Stuff for markov
MARKOV_GUILD_ID = 527887739178188830  # Lightning Hub
MARKOV_CHANNEL_IDS = [527997150206885888,  # playground
                      527887970980724758,  # shitposting
                      528374893977403402,  # general
                      655851658773004298,  # vguide-alert
                      625474940342370324,  # webhooks-and-projects
                      788981447708508220,  # markovo
                      ]
MARKOV_LIMIT = 500
MAKROV_SEND_CHANNEL = 788981447708508220  # markovo
