from pyrogram import Client
from pyrogram.errors import RPCError

api_id = 2675972
api_hash = "d4c1cfcea1e35a793443560545ed3318"

app = Client("+639272572955", api_id, api_hash)
target = "cnsex8"  # Target channel/supergroup sigui588

with app:
    members = app.iter_chat_members(target)
    print(f"Chanel members counts : {len(members)}")
    for i in range(0,100):
        member = members[i]
        print(f"adding :{member.user.first_name}")
        try:
            if app.add_chat_members("pyrogramdemos", member.user.id):
                print(f"success...{i}")
        except RPCError as e:
            print(f"err :{e.MESSAGE}")


