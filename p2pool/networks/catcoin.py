from p2pool.bitcoin import networks

PARENT = networks.nets['catcoin']
SHARE_PERIOD = 15 # seconds target spacing
CHAIN_LENGTH = 12*60*60//15 # shares
REAL_CHAIN_LENGTH = 12*60*60//15 # shares
TARGET_LOOKBEHIND = 20 # shares coinbase maturity
SPREAD = 10 # blocks
IDENTIFIER = 'cacacacae0e0e0e0'.decode('hex')
PREFIX = 'fefecfcf0e0f3434'.decode('hex')
P2P_PORT = 29902
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9993
#        BOOTSTRAP_ADDRS = 'p2pool.e-pool.net 107.170.40.107 '.split(' ')
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net p2pool.name:9930 p2pool.thepeeps.net:41295 solidpool.org:8333 p2pool-eu.gotgeeks.com:8333 p2pool-us.gotgeeks.com:8333 rav3n.dtdns.net:8333 doge.dtdns.net:8333 pool.hostv.pl:8333 p2pool.org:8333 p2pool.gotgeeks.com:8333 p2pool.dtdns.net:8333'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
