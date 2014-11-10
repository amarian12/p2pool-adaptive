import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'fac3b6da'.decode('hex') #pchmessagestart
P2P_PORT = 19921
ADDRESS_VERSION = 30 #pubkey_address
RPC_PORT = 14023
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'digibyteaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: __import__('digibyte_subsidy').GetBlockBaseValue(height)
POW_FUNC = data.hash256
BLOCK_PERIOD = 30 # s
SYMBOL = 'DGB'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'digibyte256') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/digibyte256/') if platform.system() == 'Darwin' else os.path.expanduser('~/.digibyte256'), 'digibyte256.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.cryptopoolmining.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.cryptopoolmining.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.cryptopoolmining.com/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.0001
