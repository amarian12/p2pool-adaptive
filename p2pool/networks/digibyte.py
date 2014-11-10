from p2pool.bitcoin import networks

PARENT = networks.nets['digibyte']
SHARE_PERIOD = 10 # seconds target spacing
CHAIN_LENGTH = 12*60*60//10 # shares
REAL_CHAIN_LENGTH = 12*60*60//10 # shares
TARGET_LOOKBEHIND = 20 # shares diff regulation
SPREAD = 50 # blocks
IDENTIFIER = '48a4ebc31b798115'.decode('hex')
PREFIX = '5685a276c2dd81db'.decode('hex')
#        IDENTIFIER = 'da0fa0c30b6fab6a'.decode('hex')
#        PREFIX = 'c30fa0b60da0c3da'.decode('hex')
P2P_PORT = 29922
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 8922
BOOTSTRAP_ADDRS = 'p2p.mine.bz:8022 dgbpool.cloudapp.net:8022 p2pool-eu.gotgeeks.com:8022 128.199.245.94:8022 192.186.136.118:8022 188.226.153.233:8022 91.237.77.7:8022 46.228.205.100:8022 69.90.132.197:8022 50.135.47.39:8022 '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
