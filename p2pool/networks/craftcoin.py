from p2pool.bitcoin import networks

PARENT = networks.nets['craftcoin']
SHARE_PERIOD = 10 # seconds target spacing
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares coinbase maturity
SPREAD = 30 # blocks
IDENTIFIER = '755F8AD0DD49380A'.decode('hex')
PREFIX = '31357EF0ECB3C1BC'.decode('hex')
P2P_PORT = 29903
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 8830
BOOTSTRAP_ADDRS = 'crc.xpool.net:23630 p2pool.org craftcoin.treasurequarry.com crc.prominer.org us-east1.cryptovein.com'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-crc'
VERSION_CHECK = lambda v: True
