from p2pool.bitcoin import networks

PARENT = networks.nets['tigercoin']
SHARE_PERIOD = 5 # seconds
CHAIN_LENGTH = 12*60*60//5 # shares
REAL_CHAIN_LENGTH = 12*60*60//5 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 50 # blocks
IDENTIFIER = 'fad5fab5dbfdfdd5'.decode('hex')
PREFIX = 'fad5df5bb5faaffd'.decode('hex')
P2P_PORT = 29971
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 8938
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
