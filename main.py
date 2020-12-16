import json
from sage import client, constants, catpost


def get_json_constants():
    with open("sage/constants.json", "r") as fp:
        tmp = json.load(fp)
    return tmp


if __name__ == "__main__":
    if not constants.TOKEN:
        exit()
    else:
        template = constants.JINJA_ENV.get_template("README.md")

    client.client.run(str(constants.TOKEN))

    cnts = get_json_constants()

    cat = catpost.get_from_catapi()

    with open("README.md", "w") as fp:
        fp.write(template.render(pfp_link=constants.PFP_SAUCE_LINK,
                                 catpost=cat))
