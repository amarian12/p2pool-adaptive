import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'fcd9b7dd'.decode('hex')
P2P_PORT = 19903
ADDRESS_VERSION = 57
RPC_PORT = 12123
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'craftcoin address' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 2*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s targetspacing
SYMBOL = 'CRC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'craftcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/craftcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.craftcoin'), 'craftcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://crc.cryptocoinexplorer.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://crc.cryptocoinexplorer.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://crc.cryptocoinexplorer.com/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 1e8
