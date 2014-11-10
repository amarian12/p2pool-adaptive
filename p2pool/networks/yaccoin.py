from p2pool.bitcoin import networks

PARENT = networks.nets['yaccoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e138d6b9c7933511'.decode('hex')
PREFIX = '6298b1952ee619a0'.decode('hex')
P2P_PORT = 10099
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 10001
BOOTSTRAP_ADDRS = 'p2pool.yaccoin.org 174.70.129.192'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-yaccoin'
VERSION_CHECK = lambda v: True
VERSION_WARNING = lambda v: 'Upgrade Yaccoin to >=0.9.2.2!' if v < 90202 else None
