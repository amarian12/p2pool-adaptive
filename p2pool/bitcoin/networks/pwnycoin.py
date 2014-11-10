import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = '04040404'.decode('hex') #messagestart
P2P_PORT = 19967
ADDRESS_VERSION = 55 #pubkey_address
RPC_PORT = 26667
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'pwnycoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 6144*100000000 if height<8640 else 2048*100000000 >> (height * 1)//172800
POW_FUNC = data.hash256
BLOCK_PERIOD = 30 # s
SYMBOL = 'PWNY'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'pwnycoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/pwnycoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.pwnycoin'), 'pwnycoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://www.pwnycoin.com/?'
ADDRESS_EXPLORER_URL_PREFIX = 'http://www.pwnycoin.com/?'
TX_EXPLORER_URL_PREFIX = 'http://www.pwnycoin.com/?'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 1e8
