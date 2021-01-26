from pyrogram import Client
from pyrogram.errors import RPCError
import json
import sys
import time

api_id = 2250010
api_hash = "d18a91b8061ea48c5b536745a396d09a"
app = Client("+639277142732", api_id, api_hash)

fromIndex = 0
toIndex = 0

if len(sys.argv) == 3:
    fromIndex = int(sys.argv[1])
    toIndex = int(sys.argv[2])
else:
    print("please input index range.")
    sys.exit()


with app:
    f = open("members.json")
    members_json_str = f.read()
    f.close()
    members = json.loads(members_json_str)

    for i in range(fromIndex,toIndex):
        member = members[i]
        print(f"adding :{member['first_name']}")
        try:
            if app.add_chat_members("sexchatcn", member['id']):
                print(f"success...[{i}]")
                time.sleep(10)
        except RPCError as e:
            print(f"err :{e.MESSAGE}")
            if e.MESSAGE == 'The method can\'t be used because your account is currently limited':
                print("[sleep 30 mins...]")
                time.sleep(1*60*30)
            else:
                time.sleep(10)


