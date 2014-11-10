from p2pool.titcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['titcoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 30 # blocks
IDENTIFIER = 'fc70435c7a81bcaf'.decode('hex')
PREFIX = '2472ef111efcd16b'.decode('hex')
P2P_PORT = 8699
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = True
WORKER_PORT = 8670
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net p2tit.mupool.com 54.69.255.233 54.186.125.35'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-tit'
VERSION_CHECK = lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v
VERSION_WARNING = lambda v: 'Upgrade titcoin to >=0.8.5!' if v < 80500 else None
