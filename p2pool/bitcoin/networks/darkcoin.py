import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'bf0c6bbd'.decode('hex')
P2P_PORT = 19968
ADDRESS_VERSION = 76
RPC_PORT = 9998
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'darkcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda nBits, height: __import__('darkcoin_subsidy').GetBlockBaseValue(nBits, height)
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'DRK'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Darkcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Darkcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.darkcoin'), 'darkcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.darkcoin.io/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.darkcoin.io/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.darkcoin.io/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**20 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
