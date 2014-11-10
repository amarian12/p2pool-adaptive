import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import math, pack, jsonrpc

@defer.inlineCallbacks
def get_subsidy(bitcoind, target):
    res = yield bitcoind.rpc_getblock(target)
    defer.returnValue(res)

P2P_PREFIX='e4e8e9e5'.decode('hex')
P2P_PORT=19946
ADDRESS_VERSION=8
RPC_PORT=9346
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '00000a060336cbb72fe969666d337b87198b1add2abaa59cca226820b32933a4')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC=lambda bitcoind, target: get_subsidy(bitcoind, target)
BLOCK_PERIOD=600 # s
SYMBOL='NVC'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'NovaCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/NovaCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.novacoin'), 'novacoin.conf')
BLOCK_EXPLORER_URL_PREFIX='http://explorer.novaco.in/block/'
ADDRESS_EXPLORER_URL_PREFIX='http://explorer.novaco.in/address/'
TX_EXPLORER_URL_PREFIX='http://explorer.novaco.in/tx/'
SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF=2**16
DUST_THRESHOLD=0.01e6