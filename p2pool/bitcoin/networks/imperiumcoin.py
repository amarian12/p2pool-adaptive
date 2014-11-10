import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 11095
ADDRESS_VERSION = 48
RPC_PORT = 21095
RPC_CHECK = lambda v: True

SUBSIDY_FUNC = lambda height: 122*51240000 >> (height + 1)//210000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 600 # s
SYMBOL = 'IMPC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'coin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/coin/') if platform.system() == 'Darwin' else os.path.expanduser('~/'), 'coin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://blockexperts.com/impc/hash/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://blockexperts.com/impc/address/'
TX_EXPLORER_URL_PREFIX = 'http://blockexperts.com/impc/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
