from pyrogram import Client
import json

api_id = 2763716
api_hash = "d4c2d2e53efe8fbb71f0d64deb84b3da"

app = Client("+639277144517", api_id, api_hash)
target = "cnsex8"  # Target channel/supergroup sigui588 cnsex8

with app:
    members = app.iter_chat_members(target)
    print(f"Chanel members counts : {len(members)}")

    members_arr = []
    for i in range(0,len(members)):
        member = members[i]
        members_arr.append({'id':member.user.id, 'first_name':member.user.first_name})
    
    members_json_str = json.dumps(members_arr)
    members_open = open('members_44517.json', 'w')
    members_open.write(members_json_str)
    members_open.close()


