import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f0b9b3d6'.decode('hex') #pchmessagestart
P2P_PORT = 19982
ADDRESS_VERSION = 20 #pubkey_address
RPC_PORT = 9982
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'Magiaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 0*1200000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # seconds
SYMBOL = 'XMG'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'magi') 
		if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/magi/') 
		if platform.system() == 'Darwin' else os.path.expanduser('~/.magi'), 'magi.conf')
BLOCK_EXPLORER_URL_PREFIX='https://bchain.info/XMG/block/'
ADDRESS_EXPLORER_URL_PREFIX='https://bchain.info/XMG/address/'
TX_EXPLORER_URL_PREFIX='https://bchain.info/XMG/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8

