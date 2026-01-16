from dremio_client import SimpleClient
import json

config = {
    "dremio": {
        "net": {
            "host": "api.dremio.cloud",
            "port": 443,
            "scheme": "https"
        },
        "auth": {
            "token": "test-token"
        }
    }
}

try:
    # Try passing dict directly?
    # SimpleClient usually expects proper confuse Config object, or maybe simple dict works if it just does lookups.
    # But error showed `config["port"]` which assumes top level keys?
    # Let's try to reverse engineer what it wants.
    pass
except Exception as e:
    print(e)
