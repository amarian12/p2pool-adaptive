import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'ebd0c6cb'.decode('hex')
P2P_PORT = 16050
ADDRESS_VERSION = 47
RPC_PORT = 16051
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'birdcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 1*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s targetspacing
SYMBOL = 'BRD'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Birdcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Birdcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.Birdcoin'), 'Birdcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://multifaucet.tk/index.php?blockexplorer=BRD&block='
ADDRESS_EXPLORER_URL_PREFIX = 'http://multifaucet.tk/index.php?blockexplorer=BRD&address='
TX_EXPLORER_URL_PREFIX = 'http://multifaucet.tk/index.php?blockexplorer=BRD&txid='
SANE_TARGET_RANGE = (2**256//100000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
