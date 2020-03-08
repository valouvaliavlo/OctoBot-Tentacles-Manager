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

# Tentacles files
PYTHON_INIT_FILE = "__init__.py"
CONFIG_EVALUATOR_FILE = "evaluator_config.json"
CONFIG_TRADING_FILE = "trading_config.json"

# Current minimum default tentacles version
TENTACLE_CURRENT_MINIMUM_DEFAULT_TENTACLES_VERSION = "1.2.0"
DEFAULT_TENTACLES_PACKAGE = "OctoBot-Default-Tentacles"

# Tentacles installation folders
TENTACLES_INSTALL_TEMP_DIR = "temp_tentacles"
TENTACLES_ARCHIVE_ROOT = "reference_tentacles"

# Tentacles folders
TENTACLES_PATH = "tentacles"
TENTACLES_BACKTESTING_PATH = "Backtesting"
TENTACLES_EVALUATOR_PATH = "Evaluator"
TENTACLES_INTERFACES_PATH = "Interfaces"
TENTACLES_NOTIFIERS_PATH = "Notifiers"
TENTACLES_SERVICES_PATH = "Services"
TENTACLES_TRADING_PATH = "Trading"
TENTACLES_WEBSOCKETS_PATH = "Websockets"

# Tentacles sub-folders
TENTACLE_MAX_SUB_FOLDERS_LEVEL = 3
TENTACLES_BACKTESTING_COLLECTORS_PATH = "collectors"
TENTACLES_BACKTESTING_CONVERTERS_PATH = "converters"
TENTACLES_BACKTESTING_IMPORTERS_PATH = "importers"
TENTACLES_BACKTESTING_THIRD_LEVEL_EXCHANGES_PATH = "exchanges"
TENTACLES_BACKTESTING_THIRD_LEVEL_SOCIAL_PATH = "social"
TENTACLES_EVALUATOR_REALTIME_PATH = "RealTime"
TENTACLES_EVALUATOR_TA_PATH = "TA"
TENTACLES_EVALUATOR_SOCIAL_PATH = "Social"
TENTACLES_EVALUATOR_STRATEGIES_PATH = "Strategies"
TENTACLES_EVALUATOR_UTIL_PATH = "Util"
TENTACLES_TRADING_MODE_PATH = "Mode"
TENTACLES_TRADING_EXCHANGE_PATH = "Exchange"
TENTACLES_WEBSOCKETS_FEEDS_PATH = "feeds"

# Tentacle module folders
TENTACLE_CONFIG = "config"
TENTACLE_RESOURCES = "resources"
TENTACLE_TESTS = "tests"

# Tentacles architecture
TENTACLES_FOLDERS_ARCH = {
    TENTACLES_BACKTESTING_PATH: {
        TENTACLES_BACKTESTING_COLLECTORS_PATH: [
            TENTACLES_BACKTESTING_THIRD_LEVEL_EXCHANGES_PATH,
            TENTACLES_BACKTESTING_THIRD_LEVEL_SOCIAL_PATH
        ],
        TENTACLES_BACKTESTING_CONVERTERS_PATH: [
            TENTACLES_BACKTESTING_THIRD_LEVEL_EXCHANGES_PATH
        ],
        TENTACLES_BACKTESTING_IMPORTERS_PATH: [
            TENTACLES_BACKTESTING_THIRD_LEVEL_EXCHANGES_PATH,
            TENTACLES_BACKTESTING_THIRD_LEVEL_SOCIAL_PATH
        ]
    },
    TENTACLES_EVALUATOR_PATH: [
        TENTACLES_EVALUATOR_REALTIME_PATH,
        TENTACLES_EVALUATOR_SOCIAL_PATH,
        TENTACLES_EVALUATOR_TA_PATH,
        TENTACLES_EVALUATOR_STRATEGIES_PATH,
        TENTACLES_EVALUATOR_UTIL_PATH
    ],
    TENTACLES_INTERFACES_PATH: [],
    TENTACLES_NOTIFIERS_PATH: [],
    TENTACLES_SERVICES_PATH: [],
    TENTACLES_TRADING_PATH: [
        TENTACLES_TRADING_MODE_PATH,
        TENTACLES_TRADING_EXCHANGE_PATH
    ],
    TENTACLES_WEBSOCKETS_PATH: [
        TENTACLES_WEBSOCKETS_FEEDS_PATH
    ]
}

TENTACLE_MODULE_FOLDERS = {
    TENTACLE_CONFIG,
    TENTACLE_RESOURCES,
    TENTACLE_TESTS
}

TENTACLES_TEST_PATH = "tests"


# tentacles files management
TENTACLE_TYPES = [TENTACLES_BACKTESTING_PATH,
                  TENTACLES_EVALUATOR_PATH,
                  TENTACLES_INTERFACES_PATH,
                  TENTACLES_NOTIFIERS_PATH,
                  TENTACLES_SERVICES_PATH,
                  TENTACLES_TRADING_PATH,
                  TENTACLES_WEBSOCKETS_PATH]