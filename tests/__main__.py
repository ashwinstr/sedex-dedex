# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by SedexTeam@Github, < https://github.com/SedexTeam >.
#
# This file is part of < https://github.com/SedexTeam/Sedex > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Sedex/blob/master/LICENSE >
#
# All rights reserved.

import os

from jutsu import sedex


async def _worker() -> None:
    chat_id = int(os.environ.get("CHAT_ID") or 0)
    type_ = 'unofficial' if os.path.exists("../sedex/plugins/unofficial") else 'main'
    await sedex.send_message(chat_id, f'`{type_} build completed !`')

if __name__ == "__main__":
    sedex.begin(_worker())
    print('SEDEX test has been finished!')
