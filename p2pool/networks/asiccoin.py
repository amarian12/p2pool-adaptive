from p2pool.bitcoin import networks

PARENT = networks.nets['asiccoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = '2c80035c7a81bc6f'.decode('hex')
PREFIX = '2472ef181efcd37c'.decode('hex')
P2P_PORT = 29934
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = True
WORKER_PORT = 8980
BOOTSTRAP_ADDRS = 'japool.com:13432 rav3n.dtdns.net:7432 '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-asc'
VERSION_CHECK = lambda v: True
