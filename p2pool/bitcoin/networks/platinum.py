import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = '28282828'.decode('hex')
P2P_PORT = 19926
ADDRESS_VERSION = 55
RPC_PORT = 10126
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue('platinumaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 78*100000000 >> (height + 1)//259200
POW_FUNC = data.hash256
BLOCK_PERIOD = 120 # s
SYMBOL = 'PT'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'platinum') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/platinum/') if platform.system() == 'Darwin' else os.path.expanduser('~/.platinum'), 'platinum.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://platinumcrypto.com/block/index.php?block_hash='
ADDRESS_EXPLORER_URL_PREFIX = 'http://platinumcrypto.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://platinumcrypto.com/block/index.php?transaction='
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
