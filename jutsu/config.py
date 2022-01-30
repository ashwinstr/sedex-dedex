# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by SedexTeam@Github, < https://github.com/SedexTeam >.
#
# This file is part of < https://github.com/SedexTeam/Sedex > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Sedex/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ["Config", "get_version"]

import os
from json.decoder import JSONDecodeError
from re import compile as comp_regex
from typing import Set

import heroku3
from git import Repo
from pyrogram import filters
from requests import Session

from jutsu import logbot, logging

from . import versions

GRepo_regex = comp_regex(
    "http[s]?://github\.com/(?P<owner>[-\w.]+)/(?P<repo>[-\w.]+)(?:\.git)?"
)

_REPO = Repo()
_LOG = logging.getLogger(__name__)
logbot.reply_last_msg("Setting Configs ...")


class Config:
    """Configs to setup SEDEX"""

    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    OWNER_ID = tuple(
        filter(lambda x: x, map(int, os.environ.get("OWNER_ID", "0").split()))
    )
    LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID"))
    DB_URI = os.environ.get("DATABASE_URL")
    LANG = os.environ.get("PREFERRED_LANGUAGE")
    DOWN_PATH = "downloads/"
    CACHE_PATH = "jutsu/xcache"
    CMD_TRIGGER = os.environ.get("CMD_TRIGGER", ";")
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR")
    UNFINISHED_PROGRESS_STR = os.environ.get("UNFINISHED_PROGRESS_STR")
    UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO")
    UPSTREAM_REMOTE = os.environ.get("UPSTREAM_REMOTE")
    TZ_NUMBER = os.environ.get("TZ_NUMBER", 1)
    GOOGLE_CHROME_DRIVER = os.environ.get("GOOGLE_CHROME_DRIVER")
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    THUMB_PATH = DOWN_PATH + "thumb_image.jpg"
    TMP_PATH = "sedex/plugins/temp/"
    MAX_MESSAGE_LENGTH = 4096
    MSG_DELETE_TIMEOUT = 120
    WELCOME_DELETE_TIMEOUT = 120
    EDIT_SLEEP_TIMEOUT = 10
    AUTOPIC_TIMEOUT = 300
    ALLOWED_CHATS = filters.chat([])
    ALLOW_ALL_PMS = True
    USE_USER_FOR_CLIENT_CHECKS = False
    SUDO_ENABLED = False
    SUDO_USERS: Set[int] = set()
    TRUSTED_SUDO_USERS: Set[int] = set()
    DISABLED_ALL = False
    DISABLED_CHATS: Set[int] = set()
    ALLOWED_COMMANDS: Set[str] = set()
    HEROKU_ENV = bool(int(os.environ.get("HEROKU_ENV", "0")))
    HEROKU_APP = (
        heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME]
        if HEROKU_ENV and HEROKU_API_KEY and HEROKU_APP_NAME
        else None
    )
    STATUS = None
    BOT_FORWARDS = False
    BOT_MEDIA = os.environ.get("BOT_MEDIA")
    TG_IDS = [777000, 1087968824, 454000]


def get_version() -> str:
    """get SEDEX version"""
    ver = f"{versions.__major__}.{versions.__minor__}.{versions.__micro__}"
    if Config.HEROKU_ENV:
        if not hasattr(Config, "HBOT_VERSION"):
            setattr(Config, "HBOT_VERSION", hbot_version(ver))
        return Config.HBOT_VERSION
    try:
        if "/code-rgb/sedex-x" in Config.UPSTREAM_REPO.lower():
            diff = list(_REPO.iter_commits(f"v{ver}..HEAD"))
            if diff:
                ver = f"{ver}|VULCAN.{len(diff)}"
        else:
            diff = list(_REPO.iter_commits(f"{Config.UPSTREAM_REMOTE}/alpha..HEAD"))
            if diff:
                ver = f"{ver}|fork-[X].{len(diff)}"
        branch = f"@{_REPO.active_branch.name}"
    except Exception as err:
        _LOG.error(err)
    else:
        ver += branch
    return ver


def hbot_version(tag: str) -> str:
    tag_name, commits, branch = None, None, None
    pref_branch = os.environ.get("PREF_BRANCH")
    if match := GRepo_regex.match(Config.UPSTREAM_REPO):
        g_api = (
            f"https://api.github.com/repos/{match.group('owner')}/{match.group('repo')}"
        )
        with Session() as req:
            try:
                if (
                    r_com := req.get(g_api + f"/compare/v{tag}...HEAD")
                ).status_code == 200:
                    rcom = r_com.json()
                    if commits := rcom.get("total_commits"):
                        commits = f".{commits}"
                    branch = rcom.get("target_commitish")
                if (
                    r_name := req.get(g_api + f"/releases/tags/v{tag}")
                ).status_code == 200:
                    tag_name = (r_name.json().get("name") or "").replace(" ", "-")
            except JSONDecodeError:
                pass
    return f"{tag}|{tag_name or ''}{commits or ''}@{pref_branch or branch or 'alpha'}"
