import threading, requests
Token = ""
Guild_ID = ""
Member_ID = ""
while True:
    r = requests.patch(f"https://ptb.discord.com/api/v9/guilds/{Guild_ID}/members/{Member_ID}", headers={"accept": "*/*","accept-language": "en-US,th;q=0.9","authorization": Token,"content-type": "application/json","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","x-debug-options": "bugReporterEnabled","x-discord-locale": "en-GB","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJwdGIiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC4xMDEzIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDQiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTIzNzk2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==","cookie": "__dcfduid=9d4f1aa0912411ec80b4c57f2f0abc7d; __sdcfduid=9d4f1aa1912411ec80b4c57f2f0abc7d2d3f44b70736dab34731678c84532038ab8ebf3a0bfa1ea429ae29640ef1cce0; __stripe_mid=e0cee31e-f293-41c7-91a6-944ea13c03e4133477; locale=en-GB; __cfruid=50a0e16aadc6c3e17c0f039fb43d5791601b7968-1649852223"}, json={"channel_id":None})
    print(r.text)