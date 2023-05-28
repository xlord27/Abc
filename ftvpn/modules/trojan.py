from ftvpn import *

@bot.on(events.CallbackQuery(data=b'create-trojan'))
async def create_trojan(event):
	async def create_trojan_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Quota:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**Exp:**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(3)
		await event.edit("`Processing Crate Premium Account`")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{user}" "{exp}" "{pw}" | adtr'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			b = [x.group() for x in re.finditer("trojan://(.*)",a)]
			print(b)
			domain = re.search("@(.*?):",b[0]).group(1)
			uuid = re.search("trojan://(.*?)@",b[0]).group(1)
			msg = f"""
**━━━━━━━━━━━━━━━━━**
**⟨ ⚡Xray/Trojan Account⚡ ⟩**
**━━━━━━━━━━━━━━━━━**
**🔰 Remarks     :** `{user}`
**🔰 Host Server :** `{domain}`
**🔰 User Quota  :** `{pw} GB`
**🔰 Port TLS    :** `443`
**🔰 User ID     :** `{uuid}`
**━━━━━━━━━━━━━━━━**
**🔰 Link WS    :** 
`{b[0].replace(" ","")}`
**━━━━━━━━━━━━━━━━**
**🔰 Link GRPC  :** 
`{b[1].replace(" ","")}`
**━━━━━━━━━━━━━━━━**
**Expired Until:** `{later}`
"""
		await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_trojan_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'cek-trojan'))
async def cek_trojan(event):
	async def cek_trojan_(event):
		cmd = 'systemctl status nginx'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""

{z}

**Shows Logged In Users Trojan**
**🔰 @XLORDzXD**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cek_trojan_(event)
	else:
		await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'trial-trojan'))
async def trial_trojan(event):
	async def trial_trojan_(event):
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(3)
		await event.edit("`Processing Crate Premium Account`")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "60m" "1" | trl trojan'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today
			b = [x.group() for x in re.finditer("trojan://(.*)",a)]
			print(b)
			remarks = re.search("#(.*)",b[0]).group(1)
			domain = re.search("@(.*?):",b[0]).group(1)
			uuid = re.search("trojan://(.*?)@",b[0]).group(1)
			msg = f"""
**━━━━━━━━━━━━━━━━━**
**⟨⚡Trial Trojan Account⚡⟩**
**━━━━━━━━━━━━━━━━━**
**🔰 Remarks     :** `{remarks}`
**🔰 Host Server :** `{domain}`
**🔰 User Quota  :** `1 GB`
**🔰 Port TLS    :** `443`
**🔰 User ID     :** `{uuid}`
**━━━━━━━━━━━━━━━━**
**🔰 Link WS    :** 
`{b[0].replace(" ","")}`
**━━━━━━━━━━━━━━━━**
**🔰 Link GRPC  :** 
`{b[1].replace(" ","")}`
**━━━━━━━━━━━━━━━━**
**Expired Until:** `{later}`
"""
		await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_trojan_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'renew-trojan'))
async def renew_trojan(event):
	async def renew_trojan_(event):
		x = subprocess.check_output("cat /etc/.trojan | grep '###' | cut -d ' ' -f 2 | nl",shell=True).decode("ascii")
		print(x)
		await event.edit(x)
		async with bot.conversation(chat) as num:
			await event.respond('**Nomor:**')
			num = num.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			num = (await num).raw_text
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**Exp (Days):**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		cmd = f'printf "%s\n" "{num}" "{exp}" | ratjw'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Not Found**")
		else:
			msg = f"""
**☉━━━━━━━━━━━━━━━━━☉**
    ⚡`RENEW TROJAN`⚡
**☉━━━━━━━━━━━━━━━━━☉**
**Host   :** `{DOMAIN}`
**User   :** `{user}`
**☉━━━━━━━━━━━━━━━━━☉**
**Extend :** `{exp} Days`
**☉━━━━━━━━━━━━━━━━━☉**
"""
		await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await renew_trojan_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'trojan'))
async def trojan(event):
	async def trojan_(event):
		inline = [
[Button.inline(" TRIAL TROJAN ","trial-trojan"),
Button.inline(" CREATE TROJAN ","create-trojan")],
[Button.inline(" CHECK TROJAN ","cek-trojan"),
Button.inline(" RENEW TROJAN ","renew-trojan")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**━━━━━━━━━━━━━━━━━**
**     ⚡⟨ TROJAN MANAGER ⟩⚡**
**━━━━━━━━━━━━━━━━━**
**⚡Service:** `TROJAN`
**⚡Hostname/IP:** `{DOMAIN}`
**⚡ISP:** `{z["isp"]}`
**⚡Country:** `{z["country"]}`
**🔰 @XLORDzXD**
**━━━━━━━━━━━━━━━━━**
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trojan_(event)
	else:
		await event.answer("Access Denied",alert=True)
