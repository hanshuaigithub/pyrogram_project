from pyrogram import Client
from pyrogram.errors import RPCError
import json

api_id = 2675972
api_hash = "d4c1cfcea1e35a793443560545ed3318"

app = Client("+639272572955", api_id, api_hash)
target = "sigui588"  # Target channel/supergroup sigui588 cnsex8

with app:
    members = app.iter_chat_members(target)
    print(f"Chanel members counts : {len(members)}")

    members_arr = []
    for i in range(0,len(members)):
        member = members[i]
        members_arr.append({'id':member.user.id, 'first_name':member.user.first_name})
    
    members_json_str = json.dumps(members_arr)
    members_open = open('members.json', 'w')
    members_open.write(members_json_str)
    members_open.close()

    # for i in range(0,100):
    #     member = members[i]
    #     print(f"adding :{member.user.first_name}")
    #     try:
    #         if app.add_chat_members("pyrogramdemos", member.user.id):
    #             print(f"success...{i}")
    #     except RPCError as e:
    #         print(f"err :{e.MESSAGE}")


