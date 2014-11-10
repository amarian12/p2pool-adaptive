from p2pool.bitcoin import networks

PARENT = networks.nets['Birdcoin']
SHARE_PERIOD = 5 # seconds target spacing
CHAIN_LENGTH = 24*60*60//5 # shares
REAL_CHAIN_LENGTH = 24*60*60//5 # shares
TARGET_LOOKBEHIND = 200 # shares coinbase maturity
SPREAD = 30 # blocks
IDENTIFIER = 'D0DD8AD0DD49380A'.decode('hex')
PREFIX = 'D0DD7EF0ECB3755F'.decode('hex')
P2P_PORT = 29951
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 8851
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
