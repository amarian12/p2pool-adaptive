from p2pool.bitcoin import networks

PARENT = networks.nets['franko']
SHARE_PERIOD = 15 # seconds target spacing
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares coinbase maturity
SPREAD = 30 # blocks
IDENTIFIER = 'be43F5b8c6924210'.decode('hex')
PREFIX = 'b587192ba6d4729a'.decode('hex')
P2P_PORT = 39913
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 8901
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net us-east1.cryptovein.com:18125 next.afraid.org:18125 coinminer.net 88.161.131.83:29913 37.140.24.83:9639 23.92.27.131:44131 p2pool.org 192.186.133.74:29913 188.227.230.221:29913 162.243.251.98:35141 97.94.98.195:33762 79.2.130.60:11417 113.105.248.35:45651 88.161.131.83:18125 '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
