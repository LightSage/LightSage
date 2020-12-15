"""Dumb thing to make markov"""
import random
import json

import markovify

from .constants import MARKOV_GUILD_ID, MARKOV_CHANNEL_IDS, MARKOV_LIMIT


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

    genned = await client.loop.run_in_executor(None, compile_markov)

    with open("sage/constants.json", "r") as fp:
        x = json.load(fp)

    sentence = genned.make_sentence(tries=100)
    if sentence is None:
        sentence = genned.make_sentence()

    x['markov'] = {'channel_name': channel.name, 'text': sentence}

    with open("sage/constants.json", "w") as fp:
        json.dump(x, fp)
