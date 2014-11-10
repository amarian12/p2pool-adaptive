import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = '02030405'.decode('hex')
P2P_PORT = 19936
ADDRESS_VERSION = 28
RPC_PORT = 25536
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue('continuumcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 1*100000000 >> (height + 1)//86400
POW_FUNC = data.hash256
BLOCK_PERIOD = 30 # s
SYMBOL = 'CTM'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'continuumcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/continuumcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.continuumcoin'), 'continuumcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://ctminsight.buddylabsapps.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://ctminsight.buddylabsapps.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://ctminsight.buddylabsapps.com/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.03e8
