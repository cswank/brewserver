from pyramid.settings import get_settings
#from pyrobot.brewery import Factory
#from .config import config
#from pyrobot.brewery.tests.mock_driver import MockDriver
from .tank import Tank
from peak.util.imports import importString
from pyramid.security import Allow, Authenticated

class FrontPage(object):

    __parent__ = None
    __name__ = ''

    __acl__ = [
        (Allow, Authenticated, 'view'),
        ]
    
    def __init__(self):
        self._brewery = None

    @property
    def state(self):
        return self.brewery.state

    @property
    def brewery(self):
        return None
        if self._brewery is not None:
            return self._brewery
        config = self.config
        f = Factory(config)
        self._brewery = f.brewery
        self._brewery.tanks['hlt'].devices['thermometer'].io_device.analog_channels[2] = 77
        return self._brewery

    def __getitem__(self, item):
        if item not in self.brewery.tanks:
            raise KeyError('not found')
        tank = self.brewery.tanks[item]
        return Tank(self, tank)

    def set_state(self, command, kw):
        self.brewery.notification_center.post_message(message=command, sender=self, **kw)

    @property
    def config(self):
        settings = get_settings()
        config = settings['config']
        return importString(config)

front_page = FrontPage()

def get_root(request):
    return front_page



