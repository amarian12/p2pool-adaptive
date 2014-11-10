from p2pool.bitcoin import networks

PARENT=networks.nets['quarkcoin']
SHARE_PERIOD=15 # seconds
NEW_SHARE_PERIOD=15 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=50 # shares //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD=30 # blocks
NEW_SPREAD=30 # blocks
IDENTIFIER='fc70135c7a81bc6f'.decode('hex')
PREFIX='9472ef181efcd37b'.decode('hex')
P2P_PORT=29994
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=True
WORKER_PORT=8910
BOOTSTRAP_ADDRS='p2pool.e-pool.net 176.221.46.81:8371 p2pool.org:8371 qrk.mine-pool.net 0x0a.nl '.split(' ')
ANNOUNCE_CHANNEL='#p2pool'
VERSION_CHECK=lambda v: True



