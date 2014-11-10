from p2pool.bitcoin import networks

PARENT = networks.nets['solcoin']
SHARE_PERIOD = 20 # seconds target spacing
CHAIN_LENGTH = 12*60*60//20 # shares
REAL_CHAIN_LENGTH = 12*60*60//20 # shares
TARGET_LOOKBEHIND = 15 # shares
SPREAD = 20 # blocks
IDENTIFIER = 'e0f0b08e5af1e89a'.decode('hex')
PREFIX = 'a6f2b07e0ac18b6e'.decode('hex')
P2P_PORT =7360
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 8360
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net p2pool.solcoin.net p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com rav3n.dtdns.net doge.dtdns.net pool.hostv.pl p2pool.org p2pool.gotgeeks.com p2pool.dtdns.net solidpool.org'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
