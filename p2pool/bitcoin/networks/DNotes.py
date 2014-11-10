import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'f4c0aec9'.decode('hex') #chainparams.cpp pchMessageStart
P2P_PORT = 19923
ADDRESS_VERSION = 31 #PUBKEY_ADDRESS
RPC_PORT = 11223
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'DNotesaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 250*100000000 >> (height + 1)//25900
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'NOTE'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'DNotes') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/DNotes/') if platform.system() == 'Darwin' else os.path.expanduser('~/.DNotes'), 'DNotes.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://cryptoblox.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://cryptoblox.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://cryptoblox.com/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
