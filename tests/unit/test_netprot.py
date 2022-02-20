import sys
from numpy import append
import pytest
from netprot import Netprot

sys.path(append('..'))

test_normalizer = (
    [
        "TCP-443",
        "UDPC-5353",
        "UDP-53",
        "UDP%65535",
        "TCP/65636",
        "TCPUDP$443-HTTPS",
        "TCP-1024-1026",
        "ICMP-123-1223",
        "TCP/443-HTTPS",
        "ICMP",
        "ANY",
    ],
    [
        "TCP/443",
        "UDPC/5353",
        "UDP/53",
        "UDP/65535",
        "TCP/65636",
        "TCPUDP/443-HTTPS",
        "TCP/1024-1026",
        "ICMP/123-1223",
        "TCP/443-HTTPS",
        "ICMP",
        "ANY",
    ],
)

@pytest.mark.parametrize("protocols, expected_output", (test_normalizer))
def evaluate_normalizer(protocols, expected_output):
    test = Netprot(protocols)
    assert test.normalize == expected_output
