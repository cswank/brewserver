
class Device(object):

    def __init__(parent, tank):
        self.__parent__ = parent
        self.__name__ = tank.name
        self.tank = tank

    def __getitem__(self, item):
        raise KeyError('not found')

    

