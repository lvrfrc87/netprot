import os
import sys
import pytest

sys.path.append(f'{os.path.abspath(os.getcwd())}/netprot')

from netprot import Netprot


expected_output = (
    (
        True,
        list(),
        [
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
    )
)
@pytest.mark.parametrize('expected_output', [expected_output])
def test_evaluate_normalizer(expected_output, mock):
    test = Netprot(mock)
    assert test.normalize(), test.protocols == expected_output


expected_output = (
    (
        False,
        [
            'ICM/1223',
            'ICM/1224',
            'TCPUDP/443',
            'UDPC/5353'
        ],
        [
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
    )
)
@pytest.mark.parametrize('expected_output', [expected_output])
def test_evaluate_valuator_false(expected_output, mock):
    test = Netprot(mock)
    test.normalize()
    assert test.validate(remove=False), test.protocols == expected_output

expected_output = (
    (
        False,
        [
            'ICM/1223',
            'ICM/1224',
            'TCPUDP/443',
            'UDPC/5353'
        ],
        [
            'ANY',
            'ICMP',
            'TCP/1024',
            'TCP/1025',
            'TCP/1026',
            'TCP/443',
            'TCP/443',
            'TCP/65636',
            'UDP/53',
            'UDP/65535',
        ]
    )
)
@pytest.mark.parametrize('expected_output', [expected_output])
def test_evaluate_valuator_true(expected_output, mock):
    test = Netprot(mock)
    test.normalize()
    assert test.validate(remove=True), test.protocols == expected_output
