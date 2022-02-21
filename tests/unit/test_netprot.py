import os
import sys

sys.path.append(f'{os.path.abspath(os.getcwd())}/netprot')

import pytest
from netprot import Netprot


expected_output = [
    'ANY',
    'ICM/1223',
    'ICM/1224',
    'ICMP',
    'TCP/1024',
    'TCP/1025',
    'TCP/1026',
    'TCP/443',
    'TCP/443',
    'TCP/65636',
    'TCPUDP/443',
    'UDP/53',
    'UDP/65535',
    'UDPC/5353'
    ]
@pytest.mark.parametrize('expected_output', [expected_output])
def test_valuate_normalizer(expected_output, mock):
    test = Netprot(mock)
    assert test.normalize() == expected_output
