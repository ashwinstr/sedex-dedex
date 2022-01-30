<h2 align="center"><b>Owner: <a href="https://telegram.dog/Kakashi_HTK">𝙺𝙰𝙺𝙰𝚂𝙷𝙸</a></b></h2>
<br>
<p align="center">
   <a href="https://github.com/ashwinstr/UX-jutsu"><img src="https://telegra.ph/file/07fd6c82047993ce244a2.png" alt="UX-jutsu" width=400px></a>
   <br>
   <br>
</p>
<h1>SEDEX</h1>
<b>Pluggable Telegram UserBot</b>
<br>
<br>

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/code-rgb/sedex-x)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg?&style=flat-square)](https://github.com/code-rgb/SEDEX#copyright--license)
[![Stars](https://img.shields.io/github/stars/code-rgb/SEDEX?&style=flat-square)](https://github.com/code-rgb/SEDEX/stargazers)
[![Forks](https://img.shields.io/github/forks/code-rgb/SEDEX?&style=flat-square)](https://github.com/code-rgb/SEDEX/network/members)
[![Issues Open](https://img.shields.io/github/issues/code-rgb/SEDEX?&style=flat-square)](https://github.com/code-rgb/SEDEX/issues)
[![Issues Closed](https://img.shields.io/github/issues-closed/code-rgb/SEDEX?&style=flat-square)](https://github.com/code-rgb/SEDEX/issues?q=is:closed)
[![PR Open](https://img.shields.io/github/issues-pr/code-rgb/SEDEX?&style=flat-square)](https://github.com/code-rgb/SEDEX/pulls)
[![PR Closed](https://img.shields.io/github/issues-pr-closed/code-rgb/SEDEX?&style=flat-square)](https://github.com/code-rgb/SEDEX/pulls?q=is:closed)
![Repo Size](https://img.shields.io/github/repo-size/code-rgb/sedex-x?style=flat-square)
[![CodeFactor](https://www.codefactor.io/repository/github/code-rgb/sedex-x/badge?&style=flat-square)](https://www.codefactor.io/repository/github/code-rgb/sedex-x)
[![DeepSource](https://deepsource.io/gh/code-rgb/sedex-x.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/code-rgb/sedex-x/?ref=repository-badge)
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod&style=flat-square)](https://gitpod.io/#https://github.com/code-rgb/sedex-x)
[![Docker Image](https://img.shields.io/docker/image-size/varietyjames1/sedex_x?color=blue&label=Docker%20Size&style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/varietyjames1/sedex_x/tags?page=1&ordering=last_updated)
<br>

**SEDEX** is a Powerful , _Pluggable_ Telegram UserBot written in _Python_ using [Pyrogram](https://github.com/pyrogram/pyrogram).
<br>
<p align="center">
    <a href="https://telegram.dog/x_xtests"><img src="https://img.shields.io/badge/Support%20Group-USERGE--%F0%9D%91%BF-blue?&logo=telegram&style=social" width=220px></a></p>

## Disclaimer
```
/**
   ⚠️Kang at your own risk⚠️          
   Your Telegram account may get banned.
   I am not responsible for any improper use of this bot
   This bot is intended for the purpose of having fun with memes,
   as well as efficiently managing groups.
   It can help you with managing yourself as well.
   You ended up spamming groups, getting reported left and right,
   and then you ended up in a Final Battle with Telegram
   and at the end the Telegram Team
   deleted your account?
   And after that, you pointed your fingers at us
   for getting your account deleted?
   We will be rolling on the floor laughing at you.
   Yes! you heard it right.
/**
```
## Requirements 
* Python 3.8 or Higher
* Telegram [API Keys](https://my.telegram.org/apps)
* Google Drive [API Keys](https://console.developers.google.com/)
* MongoDB [Database URL](https://cloud.mongodb.com/)
## How To Deploy 
* With Heroku:
<p align="center">
   <a href = "https://heroku.com/deploy?template=https://github.com/ashwinstr/MyGpack"><img src="https://telegra.ph/file/57c4edb389224c9cf9996.png" alt="Press to Takeoff" width="490px"></a>
</p>
<br>

* With Railway<br>
[![Deploy on Railway](https://railway.app/button.svg)](https://telegra.ph/How-to-deploy-UX-on-Railway-12-12)

> **NOTE** : ([Heroku] settings -> reveal config vars) ([Railway] -> variables)
* First click The Button Above.
* Fill `API_ID`, `API_HASH`, `DATABASE_URL`, `LOG_CHANNEL_ID`, `HEROKU_APP_NAME` and `HEROKU_API_KEY` (**required**)
* Then fill Dual Mode vars : `OWNER_ID`, `BOT_TOKEN` and `HU_STRING_SESSION`
* Then fill [other **non-required** vars](https://telegra.ph/Heroku-Vars-for-SEDEX-08-25) later
* Finally **hit deploy** button
## String Session
**VAR ->** `HU_STRING_SESSION`
#### By HEROKU
- [open your app](https://dashboard.heroku.com/apps/) then go to **more** -> **run console** and type `bash genStr` and click **run**.
#### On REPL
- [Generate on REPL](https://repl.it/@Leorio/stringsessiongen#main.py)
### Read more
<details>
  <summary><b>Details and Guides</b></summary>

## Other Ways

* With Docker 🐳 
    <a href="https://github.com/code-rgb/SEDEX/blob/alpha/resources/readmeDocker.md"><b>See Detailed Guide</b></a>

* With Git, Python and pip 🔧
  ```bash
  # clone the repo
  git clone https://github.com/code-rgb/sedex-x.git
  cd sedex-x

  # create virtualenv
  virtualenv -p /usr/bin/python3 venv
  . ./venv/bin/activate

  # install requirements
  pip install -r requirements.txt

  # Create config.env as given config.env.sample and fill that
  cp config.env.sample config.env

  # get string session and add it to config.env
  bash genStr

  # finally run the SEDEX ;)
  bash run
  ```


<h2>Guide to Upstream Forked Repo</h2>
<a href="https://telegra.ph/Upstream-Sedex-Forked-Repo-Guide-07-04"><b>Upstream Forked Repo</b></a>
<br>
<br>

<h3 align="center">Youtube Tutorial<h3>
<p align="center"><a href="https://youtu.be/M4T_BJvFqkc"><img src="https://i.imgur.com/VVgSk2m.png" width=250px></a>
</p>


## Features 

* Powerful and Very Useful **built-in** Plugins
  * gdrive [ upload / download / etc ] ( Team Drives Supported! ) 
  * zip / tar / unzip / untar / unrar
  * telegram upload / download
  * pmpermit / afk
  * notes / filters
  * split / combine
  * gadmin
  * plugin manager
  * ...and more
* Channel & Group log support
* Database support
* Build-in help support
* Easy to Setup & Use
* Easy to add / port Plugins
* Easy to write modules with the modified client

## Example Plugin 

```python
from sedex import sedex, Message, filters

LOG = sedex.getLogger(__name__)  # logger object
CHANNEL = sedex.getCLogger(__name__)  # channel logger object

# add command handler
@sedex.on_cmd("test", about="help text to this command")
async def test_cmd(message: Message):
   LOG.info("starting test command...")  # log to console
   # some other stuff
   await message.edit("testing...", del_in=5)  # this will be automatically deleted after 5 sec
   # some other stuff
   await CHANNEL.log("testing completed!")  # log to channel

# add filters handler
@sedex.on_filters(filters.me & filters.private)  # filter my private messages
async def test_filter(message: Message):
   LOG.info("starting filter command...")
   # some other stuff
   await message.reply(f"you typed - {message.text}", del_in=5)
   # some other stuff
   await CHANNEL.log("filter executed!")
```

</details> 

### Project Credits 
* [Pyrogram Assistant](https://github.com/pyrogram/assistant)
* [PyroGramBot](https://github.com/SpEcHiDe/PyroGramBot)
* [PaperPlane](https://github.com/RaphielGang/Telegram-Paperplane)
* [Uniborg](https://github.com/SpEcHiDe/UniBorg)
### Copyright & License 
[**GNU General Public License v3.0**](https://github.com/code-rgb/SEDEX/blob/alpha/LICENSE)
