#  Drakkar-Software OctoBot-Tentacles-Manager
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
from octobot_tentacles_manager.api.util.tentacles_management import manage_tentacles
from octobot_tentacles_manager.constants import TENTACLES_INSTALL_TEMP_DIR, TENTACLES_PATH, DEFAULT_BOT_PATH
from octobot_tentacles_manager.workers.install_worker import InstallWorker

USER_HELP = """Install or re-install the given tentacles modules with their requirements if any.
    Does not edit tentacles configuration files and creates it if missing."""


async def install_all_tentacles(tentacles_path_or_url, tentacle_path=TENTACLES_PATH,
                                bot_path=DEFAULT_BOT_PATH, aiohttp_session=None) -> int:
    return await _install_tentacles(None, tentacles_path_or_url,
                                    tentacle_path,
                                    bot_path,
                                    aiohttp_session=aiohttp_session)


async def install_tentacles(tentacle_names, tentacles_path_or_url,
                            bot_path=DEFAULT_BOT_PATH, tentacle_path=TENTACLES_PATH, aiohttp_session=None) -> int:
    return await _install_tentacles(tentacle_names, tentacles_path_or_url,
                                    tentacle_path, bot_path, aiohttp_session=aiohttp_session)


async def _install_tentacles(tentacle_names, tentacles_path_or_url, tentacle_path=TENTACLES_PATH,
                             bot_path=DEFAULT_BOT_PATH, use_confirm_prompt=False, aiohttp_session=None) -> int:
    install_worker = InstallWorker(TENTACLES_INSTALL_TEMP_DIR, tentacle_path,
                                   bot_path, use_confirm_prompt, aiohttp_session)
    return await manage_tentacles(install_worker, tentacle_names, tentacles_path_or_url, aiohttp_session)
