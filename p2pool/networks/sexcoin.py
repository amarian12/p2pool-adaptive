from p2pool.bitcoin import networks

PARENT=networks.nets['sexcoin']
SHARE_PERIOD=15 # seconds
CHAIN_LENGTH=24*60*60//30 # shares
REAL_CHAIN_LENGTH=24*60*60//30 # shares
TARGET_LOOKBEHIND=200 # shares
SPREAD=10 # blocks
IDENTIFIER='e037d5b8c6923415'.decode('hex')
PREFIX='7208c1a53ef629b0'.decode('hex')
P2P_PORT=29983
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=8881
BOOTSTRAP_ADDRS='p2pool.e-pool.net p2pool.e-pool.net:29961 sxc.outhashed.com:8698 blackgold.pro:8698 54.201.174.16:53848 162.243.228.98:55222 121.30.195.6:58992 79.183.27.74:26683 46.149.46.149:58379'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-alt'
VERSION_CHECK=lambda v: True
