from p2pool.bitcoin import networks

PARENT = networks.nets['ekrona']
SHARE_PERIOD = 10 # seconds target spacing
CHAIN_LENGTH = 12*60*60//10 # shares
REAL_CHAIN_LENGTH = 12*60*60//10 # shares
TARGET_LOOKBEHIND = 20 # shares coinbase maturity
SPREAD = 50 # blocks
IDENTIFIER = 'fe656b726f6e61fe'.decode('hex')
PREFIX = 'fc656b726f6e61fd'.decode('hex')
P2P_PORT = 29945
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 8950
BOOTSTRAP_ADDRS = 'p2pool-eu.gotgeeks.com:8344 p2pool-us.gotgeeks.com:8344 rav3n.dtdns.net:8344 taken.pl:8344'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
