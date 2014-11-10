from p2pool.bitcoin import networks

PARENT = networks.nets['pwnycoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 12*60*60//30 # shares
REAL_CHAIN_LENGTH = 12*60*60//30 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 20 # blocks
IDENTIFIER = 'cdb0b4afb37d4ca6'.decode('hex')
PREFIX = 'c7a4b09e04ade234'.decode('hex')
P2P_PORT = 29967
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = True
WORKER_PORT = 8967
BOOTSTRAP_ADDRS = 'pool.broketech.tk:26661 24.10.44.25:35159 89.1.29.161:49367'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
