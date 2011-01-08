from pyrobot.brewery.devices import Thermometer, LevelIndicator, Stirrer, ElectricBurner, ValveSwitch, Cooler, SignalConverter
from pyrobot.driver.arduino import Arduino


config = {
    'io_device': {
        'class': Arduino,
        'kw': {'port': '/dev/ttyUSB0'},
        },
    'devices': {
        },
    'tanks' : {
        'hlt' : {
            'input_devices': {
                'temperature' : {
                    'class': Thermometer,
                    'channel' : 1,
                    'converter': {
                        'class':SignalConverter,
                        'calibration_data':[[0, 0.0], [100.0, 100.0]],
                        'max':100.0,                        
                        }
                    },
                'volume' : {
                    'class': LevelIndicator,
                    'channel' : 3,
                    'converter': {
                        'class':SignalConverter,
                        'calibration_data' : [[5, 0.0], [1023, 10]],
                        'max':100.0,                        
                        },
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
                    'channel' : 0,
                    'converter': {
                        'class':SignalConverter,
                        'calibration_data':[[0, 0.0], [100.0, 100.0]],
                        'max':100.0,                        
                        }
                    },
                'volume' : {
                    'class': LevelIndicator,
                    'channel' : 4,
                    'converter': {
                        'class':SignalConverter,
                        'calibration_data' : [[5, 0.0], [1023, 10]],
                        'max':100.0,                        
                        },
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
                    'converter': {
                        'class':SignalConverter,
                        'calibration_data':[[0, 0.0], [100.0, 100.0]],
                        'max':100.0,                        
                        }
                    },
                'volume' : {
                    'class': LevelIndicator,
                    'channel' : 5,
                    'converter': {
                        'class':SignalConverter,
                        'calibration_data' : [[5, 0.0], [1023, 10]],
                        'max':100.0,                        
                        },
                    },
                },
            'output_devices' : {
                'fill_valve' : {
                    'class': ValveSwitch,
                    'channel' : 6,
                    },
                'burner' : {
                    'class': ElectricBurner,
                    'channel' : 7,
                    },
                'cooler' : {
                    'class': Cooler,
                    'channel' : 8,
                    },
                'stirrer' : {
                    'class': Stirrer,
                    'channel' : 9,
                    }
                }
            },
        'fermenter' : {
            'input_devices': {
                },
            'output_devices' : {
                'fill_valve' : {
                    'class': ValveSwitch,
                    'channel' : 10,
                    }
                }
            
            },
        },
    }

