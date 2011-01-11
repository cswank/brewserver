from pyramid.settings import get_settings
from pyrobot.brewery import Factory
from .config import config
from pyrobot.brewery.tests.mock_driver import MockDriver
from .tank import Tank
from peak.util.imports import importString
from pyramid.security import Allow, Authenticated, Everyone

class FrontPage(object):

    __acl__ = [
        (Allow, Everyone, 'view'),
        ]

    __parent__ = None
    __name__ = ''
    
    def __init__(self):
        self._brewery = None
        self._db = None

    @property
    def state(self):
        return self.brewery.json_state

    @property
    def brewery(self):
        if self._brewery is not None:
            return self._brewery
        config = self.config
        f = Factory(config)
        brewery = f.brewery
        self._brewery = brewery
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



