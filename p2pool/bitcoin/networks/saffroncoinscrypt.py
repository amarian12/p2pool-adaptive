import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

@defer.inlineCallbacks
def check_genesis_block(bitcoind, genesis_block_hash):
    try:
        yield bitcoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)


@defer.inlineCallbacks
def get_subsidy(bitcoind, target):
    res = yield bitcoind.rpc_getblock(target)
    defer.returnValue(res)

P2P_PREFIX='cf0567ea'.decode('hex')
P2P_PORT=19217
ADDRESS_VERSION=63
RPC_PORT=19216
RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
        'saffroncoinaddress' in (yield bitcoind.rpc_help()) and
        not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC=lambda bitcoind, target: get_subsidy(bitcoind, target)
BLOCKHASH_FUNC=data.hash256
POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD=90 # s
SYMBOL='SFR'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'saffroncoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/saffroncoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.saffroncoin'), 'saffroncoin.conf')
BLOCK_EXPLORER_URL_PREFIX='http://abe.expl.io:83/block/'
ADDRESS_EXPLORER_URL_PREFIX='http://abe.expl.io:83/address/'
TX_EXPLORER_URL_PREFIX='http://abe.expl.io:83/tx/'
SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF=2**16
DUST_THRESHOLD=0.03e8
