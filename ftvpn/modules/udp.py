from ftvpn import *

@bot.on(events.CallbackQuery(data=b'create-udp'))
async def create_udp(event):
	async def create_udp_(event):
		async with bot.conversation(chat) as pw:
			await event.respond("**user udp**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond('**Exp(days):**')
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(3)
		await event.edit("`Loading.....`")
		time.sleep(1)
		await event.edit("`Processing Create Premium UDP`")
		cmd = f'printf "%s\n" "{pw}" "{exp}"| panel-udp add'
		try:
			subprocess.check_output(cmd,shell=True)
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			msg = f"""
**☉━━━━━━━━━━━━━━━━━☉**
    ⚡`SSH UDP PREMIUM`⚡
**☉━━━━━━━━━━━━━━━━━☉**
**Host :** `{DOMAIN}`
**User :** `fsshstore`
**Pass :** `{pw}`
**Port :** `1-65535`
**Expi :** `{later}`
**☉━━━━━━━━━━━━━━━━━☉**
"""
		await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_udp_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'renew-udp'))
async def renew_udp(event):
	async def renew_udp_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Masukkan Password Akun Udp Yang Ingin Di Renew**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond('**Exp(days):**')
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(3)
		await event.edit("`Loading.....`")
		time.sleep(1)
		await event.edit("`Processing Renewal UDP Account`")
		cmd = f'printf "%s\n" "{user}" "{exp}"| panel-udp ren'
		try:
	            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{user}` **Not Found**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			msg = f"""
			
**☉━━━━━━━━━━━━━━━━━☉**
 ⚡`RENEW UDP PREMIUM`⚡
**☉━━━━━━━━━━━━━━━━━☉**
**Host   :** `{DOMAIN}`
**User   :** `fsshstore`
**Pass   :** `{user}`
**Port   :** `1-65535`
**☉━━━━━━━━━━━━━━━━━☉**
**Extend :** `{exp} Days`
**☉━━━━━━━━━━━━━━━━━☉**
"""
		await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await renew_udp_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'delete-udp'))
async def delete_udp(event):
	async def delete_udp_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Masukkan Password Akun Yang Ingin Dihapus**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
			cmd = f'printf "%s\n" "{user}" "{exp}"| panel-udp del'
		try:
	            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**Password** `{user}` **Not Found**")
		else:
			await event.respond(f"**Successfully Delete Password** `{user}`")
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_udp_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'udp'))
async def udp(event):
	async def udp_(event):
		inline = [
[Button.inline(" CREATE UDP CUSTOM ","create-udp"),
Button.inline(" DELETE UDP CUSTOM ","delete-udp")],
[Button.inline(" RENEW UDP CUSTOM ","renew-udp"),
Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**◇⚡⟨ SSH UDP MANAGER ⟩⚡◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» 🔰Service:** `SSH UDP CUSTOM`
**» 🔰Hostname/IP:** `{DOMAIN}`
**» 🔰ISP:** `{z["isp"]}`
**» 🔰Country:** `{z["country"]}`
**» @fahmisshstore**
**◇━━━━━━━━━━━━━━━━━◇**
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await udp_(event)
	else:
		await event.answer("Access Denied",alert=True)
		
