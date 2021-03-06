# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by SedexTeam@Github, < https://github.com/SedexTeam >.
#
# This file is part of < https://github.com/SedexTeam/Sedex > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Sedex/blob/master/LICENSE >
#
# All rights reserved.

from jutsu.logger import logging  # noqa
from jutsu.config import Config, get_version  # noqa
from jutsu.core import (  # noqa
    Sedex,
    filters,
    Message,
    get_collection,
    pool
)

sedex = Sedex()  # sedex is the client name
