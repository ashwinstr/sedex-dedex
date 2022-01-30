#!/bin/bash
#
# Copyright (C) 2020-2021 by SedexTeam@Github, < https://github.com/SedexTeam >.
#
# This file is part of < https://github.com/SedexTeam/Sedex > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/SedexTeam/Sedex/blob/master/LICENSE >
#
# All rights reserved.

. init/logbot/logbot.sh
. init/utils.sh
. init/checks.sh

trap handleSigTerm TERM
trap handleSigInt INT
trap 'echo hi' USR1

initSedex() {
    printLogo
    assertPrerequisites
    sendMessage "Initializing SEDEX ..."
    assertEnvironment
    editLastMessage "Starting SEDEX ..."
    printLine
}

startSedex() {
    startLogBotPolling
    runPythonModule sedex "$@"
}

stopSedex() {
    sendMessage "Exiting SEDEX ..."
    endLogBotPolling
}

handleSigTerm() {
    log "Exiting With SIGTERM (143) ..."
    stopSedex
    exit 143
}

handleSigInt() {
    log "Exiting With SIGINT (130) ..."
    stopSedex
    exit 130
}

runSedex() {
    initSedex
    startSedex "$@"
    local code=$?
    stopSedex
    return $code
}
