from p2pool.bitcoin import networks

PARENT = networks.nets['Extremecoin']
SHARE_PERIOD = 10 # seconds target spacing
CHAIN_LENGTH = 3*60*60//15 # shares
REAL_CHAIN_LENGTH = 3*60*60//15 # shares
TARGET_LOOKBEHIND = 200 # shares coinbase maturity
SPREAD = 30 # blocks
IDENTIFIER = '5F08D07F3EB0ced0'.decode('hex')
PREFIX = '75AD675C0064ced0'.decode('hex')
P2P_PORT = 39966
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 8971
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net 192.168.10.101:29966 67.233.200.130'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
