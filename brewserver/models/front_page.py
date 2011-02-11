from pyramid.threadlocal import get_current_registry
from pyrobot.brewery import Factory
from .config import config
from .tank import Tank
from pyramid.security import Allow, Authenticated, Everyone
from peak.util.imports import importString

class FrontPage(object):

    __acl__ = [
        (Allow, Everyone, 'view'),
        ]

    __parent__ = None
    __name__ = ''
    
    def __init__(self):
        self._setup = None
        self._brewery = None
        self._db = None
        self._settings = None

    @property
    def settings(self):
        if self._settings is not None:
            return self._settings
        reg = get_current_registry()
        self._settings = reg.settings
        return self._settings
        
    @property
    def state(self):
        return self.brewery.json_state

    def save_setup(self, setup):
        setup['io_device'] = {
            'class': self.settings['io_device'],
            'kw': {'port': self.settings['io_port']},
            }
        factory = Factory(setup)
    
    @property
    def brewery(self):
        if self._brewery is not None:
            return self._brewery
        f = Factory(self.config)
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
        config = self.settings['config']
        return importString(config)

front_page = FrontPage()

def get_root(request):
    return front_page



