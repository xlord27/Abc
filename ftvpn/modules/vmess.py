from ftvpn import *

#CRATE VMESS
@bot.on(events.CallbackQuery(data=b'create-vmess'))
async def create_vmess(event):
	async def create_vmess_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**User harus berawalan nomor:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond('**Exp:**')
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(3)
		await event.edit("`Processing Create Premium Account`")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "1" "{user}" "1000" "2" "{exp}" | advm'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			b = [x.group() for x in re.finditer("vmess://(.*)",a)]
			print(b)
			z = base64.b64decode(b[0].replace("vmess://","")).decode("ascii")
			z = json.loads(z)
			z1 = base64.b64decode(b[1].replace("vmess://","")).decode("ascii")
			z1 = json.loads(z1)
			msg = f"""
**━━━━━━━━━━━━━━━━━**
**⟨ ⚡Xray/Vmess Account⚡ ⟩**
**━━━━━━━━━━━━━━━━━**
**🔰 Remarks        :** `{z["ps"]}`
**🔰 Domain         :** `{z["add"]}`
**🔰 port TLS       :** `443`
**🔰 Port NTLS      :** `80, 2096`
**🔰 Port GRPC      :** `443`
**🔰 AlterId          :** `0`
**🔰 Security         :** `auto`
**🔰 User ID         :** `{z["id"]}`
**🔰 NetWork        :** `(WS) or (gRPC)`
**🔰 Path            :** `/vmess, /whatever`
**🔰 ServiceName    :** `vmess`
**━━━━━━━━━━━━━━━━━**
**🔰 Link TLS     :** 
`{b[0].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**🔰 Link NTLS    :** 
`{b[1].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**🔰 Link GRPC    :** 
`{b[2].strip("'")}`
**━━━━━━━━━━━━━━━━━**
**🔰 Expired Until:** `{later}`
"""
		await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

# TRIAL VMESS
@bot.on(events.CallbackQuery(data=b'trl vmess'))
async def trial_vmess(event):
	async def trial_vmess_(event):
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(3)
		await event.edit("`Processing Create Premium Account`")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "60m" "1" | trl vmess'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today
			b = [x.group() for x in re.finditer("vmess://(.*)",a)]
			print(b)
			z = base64.b64decode(b[0].replace("vmess://","")).decode("ascii")
			z = json.loads(z)
			z1 = base64.b64decode(b[1].replace("vmess://","")).decode("ascii")
			z1 = json.loads(z1)
			msg = f"""
**━━━━━━━━━━━━━━━━━**
**⟨ ⚡Trial Vmess Account⚡ ⟩**
**━━━━━━━━━━━━━━━━━**
**🔰 Remarks        :** `{z["ps"]}`
**🔰 Domain         :** `{z["add"]}`
**🔰 port TLS       :** `443`
**🔰 Port NTLS      :** `80, 2096`
**🔰 Port GRPC      :** `443`
**🔰 AlterId          :** `0`
**🔰 Security         :** `auto`
**🔰 User ID         :** `{z["id"]}`
**🔰 NetWork        :** `(WS) or (gRPC)`
**🔰 Path            :** `/vmess, /whatever`
**🔰 ServiceName    :** `vmess`
**━━━━━━━━━━━━━━━━━**
**🔰 Link TLS     :** 
`{b[0].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**🔰 Link NTLS    :** 
`{b[1].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**🔰 Link GRPC    :** 
`{b[2].strip("'")}`
**━━━━━━━━━━━━━━━━━**
**🔰 Expired Until:** `{later}`
"""
		await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

#CEK VMESS
@bot.on(events.CallbackQuery(data=b'cek-vmess'))
async def cek_vmess(event):
	async def cek_vmess_(event):
		cmd = 'systemctl status v2ray'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""

{z}

**Shows Logged In Users Vmess**
**🔰@XLORDzXD**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cek_vmess_(event)
	else:
		await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'renew-vmess'))
async def renew_vmess(event):
	async def renew_vmess_(event):
		x = subprocess.check_output("cat /etc/.vmess | grep '###' | cut -d ' ' -f 2 | nl",shell=True).decode("ascii")
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
		cmd = f'printf "%s\n" "{num}" "{exp}"| ravm'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Not Found**")
		else:
			msg = f"""
**☉━━━━━━━━━━━━━━━━━☉**
    ⚡`RENEW VMESS`⚡
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
		await renew_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'vmess'))
async def vmess(event):
	async def vmess_(event):
		inline = [
[Button.inline(" TRIAL VMESS ","trl vmess"),
Button.inline(" CREATE VMESS ","create-vmess")],
[Button.inline(" CHECK VMESS ","cek-vmess"),
Button.inline(" RENEW VMESS ","renew-vmess")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**━━━━━━━━━━━━━━━━━**
** ⚡⟨ VMESS MANAGER ⟩⚡**
**◇━━━━━━━━━━━━━━━━━◇**
**⚡Service:** `VMESS`
**⚡Hostname/IP:** `{DOMAIN}`
**⚡ISP:** `{z["isp"]}`
**⚡Country:** `{z["country"]}`
**🔰@XLORDzXD**
**━━━━━━━━━━━━━━━━━**
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await vmess_(event)
	else:
		await event.answer("Access Denied",alert=True)
