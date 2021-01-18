from pyrogram import Client

api_id = 2675972
api_hash = "d4c1cfcea1e35a793443560545ed3318"

# with Client("+639272572955", api_id, api_hash) as app:
#     app.send_message("me", "Greetings from **Pyrogram**!")

# app = Client("+639272572955", api_id, api_hash)
# app.run()

app = Client("+639272572955", api_id, api_hash)
target = "pyrogramlounge"  # Target channel/supergroup

with app:
    for member in app.iter_chat_members(target):
        print(member.user.first_name)