# HYOK-Wrapper
The HYOK Wrapper provides key material, retrieved from a key service, in the JWE format ([RFC7516](https://tools.ietf.org/html/rfc7516)), to a key consumer.

Currently supported integrations:
- Key service: Hashicorp Vault
- Key consumer: Salesforce's [Cache-only Key Service](https://help.salesforce.com/articleView?id=security_pe_byok_cache.htm&type=5)

## Setup
1. Fulfill prerequisites [[docs](docs/prerequisites.md)]
2. Configure key consumer [[docs](docs/key_consumer_setup.md)]
3. Configure HYOK wrapper [[docs](docs/hyok_wrapper.md)]
4. Use HYOK Wrapper [[docs](docs/usage.md)]


### For developers
- Verify Vault deployment [[docs](docs/vault.md)]
- How to create a CA [[docs](docs/certificate_authority.md)]
- Sync source code into container `hyok-wrapper`: `./dev/sync_sc.sh`.

## Architecture
- Read more [here](docs/architecture.md)

## Further reading
- Salesforce key wrapper example: https://github.com/forcedotcom/CacheOnlyKeyWrapper
- JWE libs (not used in `HYOK Wrapper`, but good references)
  - `pyjwkest`: https://github.com/rohe/pyjwkest (no longer maintained)
  - `Authlib`: https://docs.authlib.org/en/stable/jose/jwe.html
