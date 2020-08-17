# This module implements communication with Hashicorp Vault.

import base64
import hvac
import config


def get_dynamic_secret() -> bytes:
    vault_url = config.get_config('VAULT_URL')
    vault_token = config.get_config('VAULT_TOKEN')
    client = hvac.Client(url=vault_url, token=vault_token)

    if not client.sys.is_initialized():
        print('Vault has not been initialized.')
        return b''

    key_name = 'salesforce'

    # fetch latest version of key
    try:
        response = client.secrets.transit.read_key(name=key_name)
    except Exception as e:
        print(f'Transit key "{key_name}" cannot be read.')
        print(e)
        return b''

    try:
        latest_version = response['data']['latest_version']
    except KeyError as e:
        print(f'Cannot get latest version of key "{key_name}":')
        print(e)
        return b''

    # fetch key
    response = client.secrets.transit.export_key(
        name=key_name, key_type='encryption-key', version=latest_version)

    try:
        b64_key = response['data']['keys'][str(latest_version)]
    except KeyError as e:
        print(f'Cannot get key "{key_name}":')
        print(e)
        return b''

    return base64.b64decode(b64_key)
