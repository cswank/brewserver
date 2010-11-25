from .device import Device
from pyrobot.brewery import BreweryError

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

    def get_calibration_curve(self, device):
        device = self.tank.devices[device]
        return device.calibration_curve

    def delete_calibration_point(self, point, device):
        device = self.tank.devices[device]
        data = device.delete_calibration_point(point)

    def save_calibration_point(self, point, device):
        device = self.tank.devices[device]
        device.set_calibration_point(point);

    @property
    def name(self):
        return self.__name__
    



