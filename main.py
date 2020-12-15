import json
import os
from sage import client, constants


def get_json_constants():
    with open("sage/constants.json", "r") as fp:
        tmp = json.load(fp)
    return tmp


TOKEN = os.getenv("DISCORD_TOKEN", None)


if __name__ == "__main__":
    if not TOKEN:
        exit()
    else:
        template = constants.JINJA_ENV.get_template("README.md")

    client.client.run(str(TOKEN))

    cnts = get_json_constants()

    with open("README.md", "w") as fp:
        fp.write(template.render(pfp_link=constants.PFP_SAUCE_LINK,
                                 markov_channel=cnts['markov']['channel_name'],
                                 markov_string=cnts['markov']['text']))
