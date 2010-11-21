import unittest
from brewserver.models import config, get_root
from pyrobot.brewery.tests.mock_driver import MockDriver
from pyramid.configuration import Configurator
from pyramid import testing
from pyramid.testing import registerSettings


class BaseViewTests(unittest.TestCase):
    
    def setUp(self):
        config['io_device'] = {'class': MockDriver, 'kw':{}}
        self.config = Configurator()
        self.config.begin()
        registerSettings(io_dev='')
        self.front_page = get_root(None)
        
    def tearDown(self):
        self.config.end()



