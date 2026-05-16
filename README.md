# JUSTICERS - Tool

Advanced Discord server administration tool with fluorescent terminal interface and 35+ commands.

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.11%20%7C%203.12-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macOS-green?style=for-the-badge">
</p>

---

## ⚠️ DISCLAIMER

This tool is for **educational purposes only**. Using self-bots violates Discord's Terms of Service and may result in account termination. The developers assume **no responsibility** for any misuse, damages, or account bans resulting from the use of this software.

**By using this tool, you acknowledge that you are solely responsible for your actions.**

---

## ✨ Features

- 🔥 **Server Nuke** - Delete all channels, roles, emojis, and stickers in seconds
- 👥 **Mass Actions** - Kick, ban, unban, nickname, and move all members
- ✏️ **Rename Tools** - Rename roles, channels, emojis, stickers individually or all at once
- 🏗️ **Mass Create** - Create channels, roles, and categories in bulk
- 🔌 **Webhook Manager** - Create, delete, and spam via webhooks
- 💬 **Spam Module** - Message spam, webhook spam, DM spam
- 📋 **Server Clone** - Clone server structure and paste it elsewhere
- 🧹 **Cleanup** - Purge DMs, clear friends, leave all servers
- 📊 **Audit Log** - View recent server actions
- 🎨 **Fluorescent UI** - High-visibility colored terminal interface
- 📝 **Local Logs** - All actions saved to `system_logs.dat`
- ⚡ **Ultra Fast** - Maximum speed on all operations

---

## 📋 Requirements

- **Python 3.11 or 3.12** (⚠️ NOT Python 3.13)
- Windows / Linux / macOS
- Discord user token

---

## 🚀 Installation

### Method 1: Git Clone
```bash
git clone https://github.com/nulljustice/justicers.git
cd justicers
pip install -r requirements.txt
python justice_nuke.py
```

Method 2: Download ZIP

1. Download the repository as ZIP
2. Extract to a folder
3. Open CMD/Terminal in that folder
4. Run:

```bash
pip install -r requirements.txt
python justice_nuke.py
```

Method 3: Windows (.bat)

Double-click run.bat

---

🎮 Usage

1. Run the tool
2. Enter your Discord user token
3. Enter the target server ID
4. Select a command from the menu
5. Type CONFIRM to execute destructive actions
6. Press ENTER to return to menu

---

🔑 How to Get Your Token

1. Open Discord in your browser (Chrome/Firefox)
2. Press F12 to open Developer Tools
3. Go to the Console tab
4. Paste and run:

```javascript
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```

5. Copy the output - that's your token

⚠️ Never share your token with anyone. It grants full access to your account.

---

📖 Commands Reference

# Command Description
1 NUKE Delete all channels, roles, emojis, and stickers

2 Del Channels Delete all channels

3 Del Roles Delete all roles

4 Del Emojis Delete all emojis

5 Del Stickers Delete all stickers

6 Rename Roles Rename all roles

7 Rename Chs Rename all channels

8 Rename Emojis Rename all emojis

9 Rename Stickers Rename all stickers

10 Rename ALL Rename everything at once

11 Mass Chs Create multiple channels

12 Mass Roles Create multiple roles

13 Mass Cats Create multiple categories

14 Del Webhooks Delete all webhooks

15 Kick All Kick all members

16 Ban All Ban all members

17 Unban All Unban all members

18 Nickname All Nickname all members

19 Move All VC Move all members to a voice channel

20 Spam All Spam all text channels

21 Webhook Spam Spam via webhooks

22 DM Spam Spam a user's DMs

23 Server Info Show server information

24 Rename Server Change server name

25 Server Icon Change server icon via URL

26 Leave Server Leave the current server

27 Invite Create an invite link

28 Audit Log View recent audit log entries

29 Clone Server Copy server structure (roles, channels, categories)

30 Paste Clone Paste cloned structure

31 Delete Server Destroy entire server

32 Purge DMs Delete all your messages in all DM chats

33 Clear Friends Remove all friends

34 Leave All Leave all servers

35 Local Logs View local log file


---

🎨 Color Scheme

The interface uses a fluorescent color palette inspired by Russian flag colors:

Color Usage
🔴 Red Borders, destructive actions, DMS alerts
⚪ White Headers, success messages, info
🔵 Blue Rename actions, audit log
🟡 Yellow Warnings, mass actions
🟢 Green Success confirmations
🟣 Magenta Banner title "JUSTICERS"

---

👥 Credits

Developer

· @nulljustice (brad) - Lead Developer

Contributors & Credits

· @nulloverlord
· @gangstal0ve
· @crlxs

---

📄 License

```
MIT License

Copyright (c) 2025 nulljustice

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

⚠️ Legal Notice

This tool is intended for educational and research purposes only.

· Do not use this tool on servers without explicit permission
· The developers are not responsible for any misuse
· Using self-bots violates Discord's Terms of Service
· Your account may be banned if caught

Use at your own risk.

---

🔗 Links

· https://discord.com/developers
· https://python.org/downloads
· https://github.com/nulljustice/justicers/issues

---

<p align="center">
  Made with ❤️ by the JUSTICERS team
</p>