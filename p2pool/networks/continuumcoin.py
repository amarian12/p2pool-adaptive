from p2pool.bitcoin import networks

PARENT = networks.nets['continuumcoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//30 # shares
REAL_CHAIN_LENGTH = 24*60*60//30 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 20 # blocks
IDENTIFIER = 'F1F0F2D3B2F68AB0'.decode('hex')
PREFIX = 'F1F3D4A540C00DF9'.decode('hex')
P2P_PORT = 29936
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 8936
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net pool.broketech.tk:7983 192.227.238.236:7983 ctm.unhinged.tk ctm.ispace.co.uk ctm.cryptohub.org ctm.coinpool.de  '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
