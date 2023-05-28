from ftvpn import *

@bot.on(events.CallbackQuery(data=b'renew-ssh'))
async def renew_ssh(event):
	async def renew_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username For Renewal**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond('**Exp(days):**')
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
			cmd = f'printf "%s\n" "{user}" "{exp}"| rasdo'
		try:
	            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{user}` **Not Found**")
		else:
		    msg = f"""
**☉━━━━━━━━━━━━━━━━━☉**
        ⚡`RENEW SSH`⚡
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
		await renew_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'create-ssh'))
async def create_ssh(event):
	async def create_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Password:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as lim:
			await event.respond("**Limit ip:**")
			lim = lim.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			lim = (await lim).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond('**Exp:**')
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
		cmd = f'useradd -e `date -d "{exp} days" +"%Y-%m-%d"` -s /bin/false -M {user} && echo "{pw}\n{pw}" | passwd {user} | tmux new-session -d -s {user} "Create ssh {user} {exp}"'
		try:
			subprocess.check_output(cmd,shell=True)
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			msg = f"""
**━━━━━━━━━━━━━━━━━**
⟨  ⚡SSH OVPN Account⚡⟩
**━━━━━━━━━━━━━━━━━**
**🔰 Username         :** `{user.strip()}`
**🔰 Password         :** `{pw.strip()}`
━━━━━━━━━━━━━━━━━
**🔰 Host              :** `{DOMAIN}`
**🔰 Host Slowdns     :** `{HOST}`
**🔰 Pub Key          :** `{PUB}`
**🔰 Port OpenSSH    :** `80, 2222, 444`
**🔰 Port DNS         :** `53, 5300`
**🔰 Port Dropbear      :** `443`
**🔰 Port Dropbear WS  :** `80, 90, 69, 143`
**🔰 Port SSH WS       :** `80`
**🔰 Port SSH SSL WS  :** `443`
**🔰 Port SSL/TLS       :** `443, 8443`
**🔰 Port OVPN WS SSL :** `7443`
**🔰 Port OVPN SSL     :** `443`
**🔰 Port OVPN TCP    :** `80, 1194`
**🔰 Port OVPN UDP    :** `25000`
**🔰 Proxy Squid        :** `8080`
**🔰 BadVPN UDP       :** `7100-7600`
**━━━━━━━━━━━━━━━━━**
**🔰 Payload WSS      :** `GET wss://BUG.COM/ HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Connection: Keep-Alive[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]]`
**━━━━━━━━━━━━━━━━━**
**🔰 `http://{DOMAIN}:81/{DOMAIN}-tcp`
**🔰 `http://{DOMAIN}:81/{DOMAIN}-ovpn`
**🔰 `http://{DOMAIN}:81/{DOMAIN}-udp.ovpn`
━━━━━━━━━━━━━━━━━
**🔰 Expired Until:** `{later}`
"""
		await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'trial-ssh'))
async def trial_ssh(event):
	async def trial_ssh_(event):
		async with bot.conversation(chat) as exp:
			await event.respond('**Exp (30m)**')
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		user = "Trial-SSH" + str(random.randint(100,1000))
		pw = "1"
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(3)
		await event.edit("`Processing Crate Premium Account`")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{user}" "{pw}" "{exp}" | trlsh'
		try:
			subprocess.check_output(cmd,shell=True)
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today
			msg = f"""
**━━━━━━━━━━━━━━━━━**
⟨⚡Trial SSH OVPN Account⚡⟩
**━━━━━━━━━━━━━━━━━**
**🔰 Username         :** `{user.strip()}`
**🔰 Password         :** `{pw.strip()}`
━━━━━━━━━━━━━━━━━
**🔰 Host              :** `{DOMAIN}`
**🔰 Host Slowdns     :** `{HOST}`
**🔰 Pub Key          :** `{PUB}`
**🔰 Port OpenSSH    :** `80, 2222, 444`
**🔰 Port DNS         :** `53, 5300`
**🔰 Port Dropbear      :** `443`
**🔰 Port Dropbear WS  :** `80, 90, 69, 143`
**🔰 Port SSH WS       :** `80`
**🔰 Port SSH SSL WS  :** `443`
**🔰 Port SSL/TLS       :** `443, 8443`
**🔰 Port OVPN WS SSL :** `7443`
**🔰 Port OVPN SSL     :** `443`
**🔰 Port OVPN TCP    :** `80, 1194`
**🔰 Port OVPN UDP    :** `25000`
**🔰 Proxy Squid        :** `8080`
**🔰 BadVPN UDP       :** `7100-7600`
**━━━━━━━━━━━━━━━━━**
**🔰 Payload WSS      :** `GET wss://BUG.COM/ HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Connection: Keep-Alive[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]]`
**━━━━━━━━━━━━━━━━━**
**🔰 `http://{DOMAIN}:81/{DOMAIN}-tcp`
**🔰 `http://{DOMAIN}:81/{DOMAIN}-ovpn`
**🔰 `http://{DOMAIN}:81/{DOMAIN}-udp-ovpn`
━━━━━━━━━━━━━━━━━
**🔰 Expired Until:** `{later}`
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'ssh'))
async def ssh(event):
	async def ssh_(event):
		inline = [
[Button.inline(" TRIAL SSH ","trial-ssh"),
Button.inline(" CREATE SSH ","create-ssh")],
[Button.inline(" RENEW SSH ","renew-ssh"),
Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**     ◇☘️⟨ SSH OVPN MANAGER ⟩☘️◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» 🔰Service:** `SSH OVPN`
**» 🔰Hostname/IP:** `{DOMAIN}`
**» 🔰ISP:** `{z["isp"]}`
**» 🔰Country:** `{z["country"]}`
**» @XLORDzXD**
**◇━━━━━━━━━━━━━━━━━◇**
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)
