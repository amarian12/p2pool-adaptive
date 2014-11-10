from p2pool.bitcoin import networks

PARENT = networks.nets['darkcoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//15 # shares
REAL_CHAIN_LENGTH = 24*60*60//15 # shares
TARGET_LOOKBEHIND = 200 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 30 # blocks
IDENTIFIER = 'ef05d164bbcd7ed1'.decode('hex')
PREFIX = '3966e45ab1ed2db9'.decode('hex')
P2P_PORT = 29968
MIN_TARGET = 4
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 7903
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net drk.altmine.net drk2.altmine.net drk3.altmine.net asia01.poolhash.org asia02.poolhash.org q30.qhor.net poulpe.nirnroot.com drk.p2pool.n00bsys0p.co.uk darkcoin.kicks-ass.net darkcoin.fr cryptohasher.net coinminer.net drk.coinquarry.net drk.kopame.com 54.186.8.140 rebootcamp.de'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-drk'
VERSION_CHECK = lambda v: v >= 90411
