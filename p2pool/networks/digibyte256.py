from p2pool.bitcoin import networks

PARENT = networks.nets['digibyte256']
SHARE_PERIOD = 10 # seconds target spacing
CHAIN_LENGTH = 12*60*60//10 # shares
REAL_CHAIN_LENGTH = 12*60*60//10 # shares
TARGET_LOOKBEHIND = 20 # shares diff regulation
SPREAD = 50 # blocks
IDENTIFIER = 'da0fa0c31b798115'.decode('hex')
PREFIX = 'c30fa076c2dd81db'.decode('hex')
P2P_PORT = 29921
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 8933
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
