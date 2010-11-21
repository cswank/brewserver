from .device import Device

class Tank(object):

    def __init__(self, parent, tank):
        self.__parent__ = parent
        self.__name__ = tank.name
        self.tank = tank

    def __getitem__(self, item):
        if item not in self.tank.devices:
            raise KeyError('not found')
        device = self.tank.devices[item]
        return Device(device)

    @property
    def state(self):
        state = self.tank.state
        return state

    @property
    def name(self):
        return self.__name__
    



