from p2pool.bitcoin import networks

PARENT = networks.nets['magi']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 12*60*60//10 # shares
REAL_CHAIN_LENGTH = 12*60*60//10 # shares
TARGET_LOOKBEHIND = 100 # shares
SPREAD = 20 # blocks
IDENTIFIER = '05c1a0cfe46bc9cb'.decode('hex')
PREFIX = 'ecfe4cafcc0a04c9'.decode('hex')
P2P_PORT = 29982
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 8835
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
