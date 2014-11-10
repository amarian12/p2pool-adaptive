import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = '7defaced'.decode('hex')
P2P_PORT = 19913
ADDRESS_VERSION = 35
RPC_PORT = 7913
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'frankoaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 1*10000000 >> (height + 1)//1080000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 30 # s targetspacing
SYMBOL = 'FRK'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'franko') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/franko/') if platform.system() == 'Darwin' else os.path.expanduser('~/.franko'), 'franko.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://frk.cryptocoinexplorer.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://frk.cryptocoinexplorer.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://frk.cryptocoinexplorer.com/tx/'
SANE_TARGET_RANGE = (2**256//100000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.001e8
