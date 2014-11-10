from p2pool.bitcoin import networks

PARENT = networks.nets['smartcoin']
SHARE_PERIOD = 5 # seconds
CHAIN_LENGTH = 12*60*60//5 # shares
REAL_CHAIN_LENGTH = 12*60*60//5 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 50 # blocks
IDENTIFIER = 'defadefaced0ced0'.decode('hex')
PREFIX = 'd0cededefafac0ce'.decode('hex')
P2P_PORT = 29983
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 8960
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net taken.pl:8585'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
