from p2pool.bitcoin import networks

PARENT = networks.nets['potcoin']
SHARE_PERIOD = 10 # seconds target spacing
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares coinbase maturity
SPREAD = 10 # blocks
IDENTIFIER = 'DDA1A1D3B2F68CDD'.decode('hex')
PREFIX = 'A2C3D4D541C11DDD'.decode('hex')
P2P_PORT = 29976
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 8989
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net p2pool.name:8420 us-east1.cryptovein.com:8420 pool.orgcoin.org:8420 xpool.net:8420 p2poolmining.pl:8420'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-pot'
VERSION_CHECK = lambda v: True
