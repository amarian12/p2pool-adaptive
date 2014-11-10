import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 19976
ADDRESS_VERSION = 55
RPC_PORT = 42000
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'potcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 420*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 40 # s
SYMBOL = 'POT'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'potcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/potcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.potcoin'), 'potcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://potchain.aprikos.net/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://potchain.aprikos.net/address/'
TX_EXPLORER_URL_PREFIX = 'http://potchain.aprikos.net/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 1e8
