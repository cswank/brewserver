from pyrobot.brewery.devices import Thermometer, LevelIndicator, Stirrer, ElectricBurner, ValveSwitch, Cooler
from pyrobot.brewery.tests.mock_driver import MockDriver

config = {
    'io_device': {
        'class': MockDriver,
        'kw': {'random': False},
        },
    'devices': {
        
        },
    'tanks' : {
        'hlt' : {
            'input_devices': {
                'temperature' : {
                    'class': Thermometer,
                    'channel' : 0,
                    'calibration_data' : None,
                    },
                'volume' : {
                    'class': LevelIndicator,
                    'channel' : 3,
                    'calibration_data' : [[31, 0.0], [1023, 50.0]],
                    },
                },
            'output_devices' : {
                'fill_valve' : {
                    'class': ValveSwitch,
                    'channel' : 0,
                    },
                'burner' : {
                    'class': ElectricBurner,
                    'channel' : 1,
                    },
                'stirrer' : {
                    'class': Stirrer,
                    'channel' : 2,
                    }
                }
            },
        'tun' : {
            'input_devices': {
                'temperature' : {
                    'class': Thermometer,
                    'channel' : 1,
                    'calibration_data' : None,
                    },
                'volume' : {
                    'class': LevelIndicator,
                    'channel' : 4,
                    'calibration_data' : [[0, 0.0], [255, 5.0]],
                    },
                },
            'output_devices' : {
                'fill_valve' : {
                    'class': ValveSwitch,
                    'channel' : 3,
                    },
                'burner' : {
                    'class': ElectricBurner,
                    'channel' : 4,
                    },
                'stirrer' : {
                    'class': Stirrer,
                    'channel' : 5,
                    },
                }
            },
        'boiler' : {
            'input_devices': {
                'temperature' : {
                    'class': Thermometer,
                    'channel' : 2,
                    'calibration_data' : None,
                    },
                'volume' : {
                    'class': LevelIndicator,
                    'channel' : 5,
                    'calibration_data' : [[0, 0.0], [255, 5.0]],
                    },
                },
            'output_devices' : {
                'fill_valve' : {
                    'class': ValveSwitch,
                    'channel' : 7,
                    },
                'burner' : {
                    'class': ElectricBurner,
                    'channel' : 8,
                    },
                'cooler' : {
                    'class': Cooler,
                    'channel' : 9,
                    },
                'stirrer' : {
                    'class': Stirrer,
                    'channel' : 10,
                    }
                }
            },
        'fermenter' : {
            'input_devices': {
                },
            'output_devices' : {
                'fill_valve' : {
                    'class': ValveSwitch,
                    'channel' : 11,
                    }
                }
            
            },
        },
    }

