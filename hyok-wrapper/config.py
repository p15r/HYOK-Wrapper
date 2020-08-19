# Loads json config

import json
import logging


def get_config_by_key(key: str) -> str:
    logger = logging.getLogger(__name__)

    try:
        with open('/opt/hyok-wrapper/config/config.json', 'r') as f:
            cfg = json.load(f)
    except FileNotFoundError as e:
        logger.error('Cannot load config file. Has "02-load-config.sh" already been executed?')
        logger.error(e)
        return ''

    # Let this raise KeyError if key does not exist
    return cfg[key]