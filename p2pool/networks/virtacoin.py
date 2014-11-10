from p2pool.bitcoin import networks

PARENT = networks.nets['virtacoin']
SHARE_PERIOD = 5 # seconds target spacing
CHAIN_LENGTH = 24*60*60//5 # shares
REAL_CHAIN_LENGTH = 24*60*60//5 # shares
TARGET_LOOKBEHIND = 200 # shares coinbase maturity
SPREAD = 10 # blocks
IDENTIFIER = 'fefecacae0e0e1e1'.decode('hex')
PREFIX = 'cacafefe0e0fe1e1'.decode('hex')
P2P_PORT = 29995
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 8934
BOOTSTRAP_ADDRS = ' '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
