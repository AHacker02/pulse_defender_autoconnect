from pushbullet import Pushbullet
from config import TOKEN


def get():
    pb = Pushbullet(TOKEN)
    pb.push_note("Token", body="")
    token = None
    while token is None:
        last_token = pb.get_pushes()[0]
        if last_token["title"] != "Token":
            token = last_token["title"]
    pb.delete_pushes()
    return token
