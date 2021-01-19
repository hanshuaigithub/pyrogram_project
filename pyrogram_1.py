from pyrogram import Client

api_id = 2675972
api_hash = "d4c1cfcea1e35a793443560545ed3318"

# with Client("+639272572955", api_id, api_hash) as app:
#     app.send_message("me", "Greetings from **Pyrogram**!")

# app = Client("+639272572955", api_id, api_hash)
# app.run()

app = Client("+639272572955", api_id, api_hash)
target = "sigui588"  # Target channel/supergroup

with app:
    members = app.iter_chat_members(target)
    for i in range(0,20):
        member = members[i]
        print(member.user.first_name)
        if member.user.username != "TylerMatthew":
            app.add_chat_members("pyrogramdemos", member.user.id)
    
    # app.add_chat_members("pyrogramdemos", "@jk123jk456")
    # app.add_chat_members("pyrogramdemos", "@snake9936")

