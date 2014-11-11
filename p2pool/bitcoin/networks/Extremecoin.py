import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'fcd9b7dd'.decode('hex')
P2P_PORT = 19966
ADDRESS_VERSION = 55
RPC_PORT = 26666
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'Extremecoin address' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 1*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 120 # s targetspacing
SYMBOL = 'EXC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'extremecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Extremecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.Extremecoin'), 'Extremecoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://exc-blocks.pw/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://exc-blocks.pw/address/'
TX_EXPLORER_URL_PREFIX = 'http://exc-blocks.pw/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.0001e8
