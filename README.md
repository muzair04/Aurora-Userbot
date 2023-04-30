<p align="center">
  <img src="./resources/extras/logo.jpg" alt="Aurora Logo">
</p>
<h1 align="center">
  <b>ᴀᴜʀᴏʀᴀ ꭙ͢ ᴜsᴇʀʙᴏᴛ</b>
</h1>

<b>A stable pluggable Telegram userbot + Voice & Video Call music bot, based on Telethon.</b>

<a href="https://github.com/muzair04/Aurora-Userbot/commits"> <img src="https://img.shields.io/github/last-commit/muzair04/Aurora-Userbot?color=red&logo=github&logoColor=blue&style=for-the-badge" /></a>
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/muzair04/Aurora-Userbot)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-blue)](https://GitHub.com/muzair04/Aurora-Userbot/graphs/commit-activity)
[![CodeQuality](https://img.shields.io/codacy/grade/a723cb464d5a4d25be3152b5d71de82d?color=blue&logo=codacy)](https://app.codacy.com/gh/muzair04/Aurora-Userbot/dashboard)
[![GitHub Forks](https://img.shields.io/github/forks/muzair04/Aurora-Userbot?&logo=github)](https://github.com/muzair04/Aurora-Userbot/fork)
[![GitHub Stars](https://img.shields.io/github/stars/muzair04/Aurora-Userbot?&logo=github)](https://github.com/muzair04/Aurora-Userbot/stargazers)
----

## Disclaimer

```
Saya tidak bertanggung jawab atas penyalahgunaan bot ini.
Bot ini dimaksudkan untuk bersenang-senang sekaligus membantu anda
mengelola grup secara efisien dan mengotomatiskan beberapa hal yang membosankan.
Gunakan bot ini dengan risiko Anda sendiri, dan gunakan userbot ini dengan bijak.
```

## DATABASE REQUIRETMENTS CHOOSE ONE :
- MONGO URI
- SQL
- REDIS

# Tutorial To Get Redis DB URL and Password
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)

## Process For Creating DB :-   
- Go To [Redis.com](Https://redis.com) and click "`Try Free`" in Top Right Corner.   
- Fill All The Required Details Like email, first and last name, password, etc.   
- Tick Below "I agree the corresponding...Privacy Policy." and Click "Get Started".   
- Now Check Your Email, and click the "Activate Now" sent by redislabs via email.   
- Now Login and Chose Free Plan in "Fixed Size" Area and Write any name in "Subscription Area".   
- On the Next Page Write Database Name and click Activate.   
   
> Congrats! Your DB has been created 🥳   
   
## Process For Getting DB Credentials:-   
- Wait 5 mins after DB creation.   
- Then There Would Be 2 Things Named "`Endpoint`" and "`Access Control & Security`".   
- Copy Both Of Them and Paste Endpoint url in `REDIS_URI` and "Access ...Security" in `REDIS_PASSWORD`.   

<details>
<summary><b>🔗 Deploy di VPS</b></summary>
<br>

### Tutorial Deploy di VPS


 • `git clone https://github.com/muzair04/Aurora-Userbot`

 • `cd Aurora*`

 • `bash installer.sh`

 • `nano .env`
  - isi vars API_ID, API_HASH, MONGO_URI, DAN SESSION
  - Jika sudah 
  - ketik ctrl + S
  - ctrl + X

 • `screen -S aurora`

 • `bash start`

</details>

<p><a href="https://heroku.com/deploy?template=https://github.com/muzair04/Aurora-Userbot"><img src="https://img.shields.io/badge/BUAT DI-HEROKU-aqua?style=plastic&logo=heroku&logoColor=gold"width="300" /></a></p>

</details>

# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
Aurora is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

---

## © Credits
* [![TeamUltroid-Devs](https://img.shields.io/static/v1?label=Teamultroid&message=devs&color=critical)](https://t.me/UltroidDevs)
* [Lonami](https://github.com/LonamiWebs/) for [Telethon.](https://github.com/LonamiWebs/Telethon)
* [MarshalX](https://github.com/MarshalX) for [PyTgCalls.](https://github.com/MarshalX/tgcalls)