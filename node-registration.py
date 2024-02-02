# https://blockstream.github.io/greenlight/getting-started/register/

import bip39
import secrets  # Make sure to use cryptographically sound randomness

rand = secrets.randbits(256).to_bytes(32, 'big')  # 32 bytes of randomness
phrase = bip39.encode_bytes(rand)

# Prompt user to safely store the phrase

seed = bip39.phrase_to_seed(phrase)[:32]  # Only need 32 bytes

# Store the seed on the filesystem, or secure configuration system

