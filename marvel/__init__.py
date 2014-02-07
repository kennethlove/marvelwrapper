# -*- coding: utf-8 -*-

#  ___ ___   ____  ____  __ __    ___  _     
# |   |   | /    ||    \|  |  |  /  _]| |    
# | _   _ ||  o  ||  D  )  |  | /  [_ | |    
# |  \_/  ||     ||    /|  |  ||    _]| |___ 
# |   |   ||  _  ||    \|  :  ||   [_ |     |
# |   |   ||  |  ||  .  \\   / |     ||     |
# |___|___||__|__||__|\_| \_/  |_____||_____|
                                   
"""
Marvel API Library
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 by Kenneth Love.
:license: BSD, see LICENSE for more details.

"""

__title__ = 'marvel'
__version__ = '0.0.1'
__author__ = 'Kenneth Love'
__license__ = 'BSD'
__copyright__ = 'Copyright 2014 Kenneth Love'

from .api import Cerebro
from .models import Character
from .resources import CharacterResource

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
