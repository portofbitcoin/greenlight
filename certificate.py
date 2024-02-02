# https://blockstream.github.io/greenlight/getting-started/certs/

# Store certificates client.crt and client-key.pem locally alongside the code

# client-key.pem is effectively the API key

from glclient import TlsConfig, Signer, Scheduler
tls = TlsConfig().identity(res.device_cert, res.device_key)

# Only mainnet, testnet, regtest networks are supported

signer = Signer(seed, network="testnet", tls=tls)

node = Scheduler(node_id=signer.node_id(), network="testnet", tls=tls).node()

