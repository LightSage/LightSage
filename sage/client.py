"""Client that does things"""

import discord

from .markov import do_markov
from .pfp import get_pfp

client = discord.Client(status=discord.Status.do_not_disturb,
                        activity=discord.Game("generating stuff..."))


@client.event
async def on_ready():
    await do_markov(client)
    await get_pfp(client)

    await client.close()
