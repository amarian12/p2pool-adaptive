from p2pool.bitcoin import networks

PARENT = networks.nets['casinocoin']
SHARE_PERIOD = 10 # seconds target spacing
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares coinbase maturity
SPREAD = 60 # blocks
IDENTIFIER = '5AE1F9AAEA359544'.decode('hex')
PREFIX = '43DC544D48689C0D'.decode('hex')
P2P_PORT = 29901
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 8840
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net csc.xpool.net:23640 casinocoin.mooo.com:23640 csc-useast.xpool.net:23640 bigiron.homelinux.com:23640 csc.hash.so:23640 csc.squiggie.com:23640 p2pool.org:23640 pool.hostv.pl:23640 rav3n.dtdns.net:23640 p2pool-us.gotgeeks.com:23640 p2pool-eu.gotgeeks.com:23640 '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-csc'
VERSION_CHECK = lambda v: True
