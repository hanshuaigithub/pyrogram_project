from pyrogram import Client
from pyrogram.errors import RPCError
import json

api_id = 2675972
api_hash = "d4c1cfcea1e35a793443560545ed3318"

app = Client("+639272572955", api_id, api_hash)

with app:
    f = open("members.json")
    members_json_str = f.read()
    f.close()
    members = json.loads(members_json_str)

    for i in range(60,80):
        member = members[i]
        print(f"adding :{member['first_name']}")
        try:
            if app.add_chat_members("sexchatcn", member['id']):
                print(f"success...[{i}]")
        except RPCError as e:
            print(f"err :{e.MESSAGE}")


