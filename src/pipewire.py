from dataclasses import dataclass
from typing import List

@dataclass
class Device:
    id : str
    hidden: bool
    name: str

input_devices: List[Device] = [
    Device('dev-1', False, 'Device 1'),
    Device('dev-2', False, 'Device 2'),
    Device('dev-3', True, 'Device 3'),
    Device('dev-4', False, 'Device 4'),
    Device('dev-5', True, 'Device 5'),
]

output_devices: List[Device] = [
    Device('dev-6', False, 'Device 6'),
    Device('dev-7', False, 'Device 7'),
    Device('dev-8', True, 'Device 8'),
    Device('dev-9', False, 'Device 9'),
    Device('dev-10', True, 'Device 10'),
    Device('dev-11', True, 'Device 11'),
    Device('dev-12', False, 'Device 12'),
    
]

active_input_devices = filter(lambda d : not d.hidden, input_devices )
disabled_input_devices = filter(lambda d : d.hidden, input_devices )

active_output_devices = filter(lambda d : not d.hidden, output_devices )
disabled_output_devices = filter(lambda d : d.hidden, output_devices )