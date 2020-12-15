from jinja2 import Environment, FileSystemLoader

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
                      ]
MARKOV_LIMIT = 500
