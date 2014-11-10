from p2pool.bitcoin import networks

PARENT = networks.nets['DNotes']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'f982abb5fab5dfdb'.decode('hex')
PREFIX = 'f982abb5d5dfdbfd'.decode('hex')
P2P_PORT = 29923
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 8923
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net 107.170.35.84 note.validerrorpool.com dnotespool.com note.charityminingpools.com dnote.poolnetwork.org'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
