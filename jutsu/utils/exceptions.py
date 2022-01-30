# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by SedexTeam@Github, < https://github.com/SedexTeam >.
#
# This file is part of < https://github.com/SedexTeam/Sedex > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Sedex/blob/master/LICENSE >
#
# All rights reserved.


class StopConversation(Exception):
    """raise if conversation has terminated"""


class ProcessCanceled(Exception):
    """raise if thread has terminated"""


class SedexBotNotFound(Exception):
    """raise if sedex bot not found"""
