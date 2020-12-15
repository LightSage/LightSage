"""Profile picture"""
from .constants import DISCORD_ID


async def get_pfp(client):
    if not DISCORD_ID:
        return
    user = client.get_user(DISCORD_ID) or await client.fetch_user(DISCORD_ID)
    if not user:
        return

    await user.avatar_url_as().save("sage/resources/profile_picture.png")
