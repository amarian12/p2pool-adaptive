from p2pool.bitcoin import networks

PARENT=networks.nets['saffroncoinscrypt']
SHARE_PERIOD=20 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=50 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD=30 # blocks
IDENTIFIER='55984712ffff1147'.decode('hex')
PREFIX='36325418ffff2566'.decode('hex')
P2P_PORT=1716
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=1718
BOOTSTRAP_ADDRS='p2poolcoin.com ca.p2poolcoin.com'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-sfr'
VERSION_CHECK=lambda v: True

