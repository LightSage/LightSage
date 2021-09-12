"""Dumb thing to make markov"""
import random
import json

import markovify

from .constants import (MARKOV_GUILD_ID, MARKOV_CHANNEL_IDS, MARKOV_LIMIT,
                        MAKROV_SEND_CHANNEL)


async def do_markov(client):
    guild = client.get_guild(MARKOV_GUILD_ID)
    if not guild:
        # Guild is somehow missing...
        return
    channel = guild.get_channel(random.choice(MARKOV_CHANNEL_IDS))
    if not channel:
        return

    msgs = []
    async for msg in channel.history(limit=MARKOV_LIMIT):
        if msg.content:
            msgs.append(msg.content)

    def compile_markov():
        model = markovify.NewlineText('\n'.join(msgs))
        return model.compile()

    model = await client.loop.run_in_executor(None, compile_markov)

    channel = guild.get_channel(MAKROV_SEND_CHANNEL)
    if not channel:
        return

    for x in range(5):
        sentence = model.make_sentence(tries=100)
        if sentence is None:
            sentence = model.make_sentence()
        await channel.send(sentence)
