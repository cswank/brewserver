from pyrobot.brewery.devices import Stirrer, ElectricBurner, ValveSwitch, Cooler
from pyrobot.brewery.sensors.gravity_gauge import GravityGaugeFactory, FloatMonitor, GravityMonitor, SourceMonitor, TimeMonitor,
from pyrobot.brewery.sensors import Thermometer
from .mock_driver import MockDriver

default = {
    'io_device': {
        'class': MockDriver,
        'port': None,
        },
    'devices': {
        },
    'sensors': {
        },
    'tanks' : {
        'hlt' : {
            'sensors': {
                'temperature' : {
                    'class': Thermometer,
                    'channel' : 0,
                    },
                'volume' : {
                    'factory': GravityGaugeFactory,
                    'fill_monitor_settings':{
                        'class': FloatMonitor,
                        'channel': 1,
                        'max_volume': 20.0
                        },
                    'drain_monitor_settings':{
                        'class': GravityMonitor,
                        'destination_tank_name':'tun',
                        'tank_radius': 18.0,
                        'valve_radius': 1.0,
                        'valve_coefficient': 0.6,
                        },
                    },
                },
            'devices' : {
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
            'sensors': {
                'temperature' : {
                    'class': Thermometer,
                    'channel' : 2,
                    },
                'volume' : {
                    'factory': GravityGaugeFactory,
                    'fill_monitor_settings':{
                        'class': SourceMonitor,
                        'tank_name': 'tun',
                        'source_tank_name': 'hlt',
                        },
                    'drain_monitor_settings':{
                        'class': TimeMonitor,
                        'tank_name': 'tun',
                        'destination_tank_name':'boiler',
                        'max_drain_time': 5.0,
                        },
                    },
                },
            'devices' : {
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
                },
            },
        'boiler' : {
            'sensors': {
                'temperature' : {
                    'class': Thermometer,
                    'channel' : 4,
                    },
                'volume' : {
                    'factory': GravityGaugeFactory,
                    'fill_monitor_settings':{
                        'class': SourceMonitor,
                        'tank_name': 'boiler',
                        'source_tank_name': 'tun',
                        },
                    'drain_monitor_settings':{
                        'class': TimeMonitor,
                        'tank_name': 'boiler',
                        'destination_tank_name':'fermenter',
                        'max_drain_time': 5.0,
                        },
                    },
                },
            'devices' : {
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
                },
            },
        'fermenter' : {
            'sensors': {
                },
            'devices' : {
                'fill_valve' : {
                    'class': ValveSwitch,
                    'channel' : 11,
                    }
                }
            }
        }
    }

