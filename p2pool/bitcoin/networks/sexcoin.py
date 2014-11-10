import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack, jsonrpc

@defer.inlineCallbacks
def check_genesis_block(bitcoind, genesis_block_hash):
    try:
        yield bitcoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)

P2P_PREFIX='face6969'.decode('hex')
P2P_PORT=19961
ADDRESS_VERSION=62
RPC_PORT=9561
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, 'f42b9553085a1af63d659d3907a42c3a0052bbfa2693d3acf990af85755f2279')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))

SUBSIDY_FUNC=lambda height: 100*100000000 >> (height + 1)//600000
POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD=60 # s
SYMBOL='SXC'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Sexcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Sexcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.sexcoin'), 'sexcoin.conf')
BLOCK_EXPLORER_URL_PREFIX='http://sxcexplorer.com/block/'
ADDRESS_EXPLORER_URL_PREFIX='http://sxcexplorer.com/address/'
TX_EXPLORER_URL_PREFIX='http://sxcexplorer.com/tx/'
SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF=2**16
DUST_THRESHOLD=0.03e8
