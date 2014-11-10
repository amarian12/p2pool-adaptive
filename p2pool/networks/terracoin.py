from p2pool.bitcoin import networks

PARENT = networks.nets['terracoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//30 # shares
REAL_CHAIN_LENGTH = 24*60*60//30 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 15 # blocks
IDENTIFIER = 'a41b2356a1b7d46e'.decode('hex')
PREFIX = '5623b62178d2b9b3'.decode('hex')
#	IDENTIFIER = 'a42a265ad1b6d42b'.decode('hex')
#	PREFIX = '56a3f62173d2a9b5'.decode('hex')
P2P_PORT = 29932
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = True
WORKER_PORT = 8932
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net seed1.p2pool.terracoin.org:9323 seed2.p2pool.terracoin.org:9323 seed3.p2pool.terracoin.org:9323 forre.st:9323 vps.forre.st:9323 93.97.192.93:9323 66.90.73.83:9323 67.83.108.0:9323 219.84.64.174:9323 24.167.17.248:9323 109.74.195.142:9323 83.211.86.49:9323 94.23.34.145:9323 168.7.116.243:9323 94.174.40.189:9344 89.79.79.195:9323 portals94.ns01.us:9323'.split(' ')
#	BOOTSTRAP_ADDRS = 'p2pool.e-pool.net fst.inetrader.com:23660 pool.bitcoinreactor.com:23660'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: 80002 <= v
VERSION_WARNING = lambda v: 'Upgrade Terracoin to >= 0.8.0.4!' if v < 80004 else None
