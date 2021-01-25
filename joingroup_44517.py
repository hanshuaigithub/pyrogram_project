from pyrogram import Client
from pyrogram.errors import RPCError
import json

api_id = 2763716
api_hash = "d4c2d2e53efe8fbb71f0d64deb84b3da"

app = Client("+639277144517", api_id, api_hash)

with app:
    f = open("members.json")
    members_json_str = f.read()
    f.close()
    members = json.loads(members_json_str)

    for i in range(80,160):
        member = members[i]
        print(f"adding :{member['first_name']}")
        try:
            if app.add_chat_members("sexchatcn", member['id']):
                print(f"success...[{i}]")
        except RPCError as e:
            print(f"err :{e.MESSAGE}")


