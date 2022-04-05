import os
import sys
import pytest

sys.path.append(f"{os.path.abspath(os.getcwd())}/netprot")

from netprot import Netprot

expected_output = (
    ["ICM/1223", "ICM/1224", "TCPUDP/443", "UDPC/5353"],
    ["TCP/443", "TCP/443", "TCP/443", "UDP/53"],
    [
        "ANY",
        "ICMP",
        "TCP/1024",
        "TCP/1025",
        "TCP/1026",
        "TCP/443",
        "TCP/6380",
        "TCP/65636",
        "UDP/53",
        "UDP/65535",
    ],
)


@pytest.mark.parametrize("expected_output", [expected_output])
def test_evaluate_standardize(expected_output, mock):
    test = Netprot(protocols=mock[0], exceptions=mock[1], separator="/")
    assert test.standardize() == expected_output[0:3]


expected_output = (
    False,
    [False, False, True, False, False, True, False, False, True, False],
    [
        "ANY",
        "ICMP",
        "TCP/1024",
        "TCP/1025",
        "TCP/1026",
        "TCP/443",
        "TCP/6380",
        "TCP/65636",
        "UDP/53",
        "UDP/65535",
    ],
)


@pytest.mark.parametrize("expected_output", [expected_output])
def test_evaluate_is_well_known(expected_output, mock):
    test = Netprot(protocols=mock[0], exceptions=mock[1], separator="/")
    test.standardize()
    assert test.is_well_known() == expected_output[0:2]
    assert test.protocols == expected_output[-1]


expected_output = (
    False,
    [False, False, True, True, True, True, True, True, False, False],
    [
        "ANY",
        "ICMP",
        "TCP/1024",
        "TCP/1025",
        "TCP/1026",
        "TCP/443",
        "TCP/6380",
        "TCP/65636",
        "UDP/53",
        "UDP/65535",
    ],
)


@pytest.mark.parametrize("expected_output", [expected_output])
def test_evaluate_is_tcp(expected_output, mock):
    test = Netprot(protocols=mock[0], exceptions=mock[1], separator="/")
    test.standardize()
    assert test.is_tcp() == expected_output[0:2]
    assert test.protocols == expected_output[-1]


expected_output = (
    False,
    [False, False, False, False, False, False, False, False, True, True],
    [
        "ANY",
        "ICMP",
        "TCP/1024",
        "TCP/1025",
        "TCP/1026",
        "TCP/443",
        "TCP/6380",
        "TCP/65636",
        "UDP/53",
        "UDP/65535",
    ],
)


@pytest.mark.parametrize("expected_output", [expected_output])
def test_evaluate_is_udp(expected_output, mock):
    test = Netprot(protocols=mock[0], exceptions=mock[1], separator="/")
    test.standardize()
    assert test.is_udp() == expected_output[0:2]
    assert test.protocols == expected_output[-1]


expected_output = [False, False, False, False, False, True, False, False, False, False]


@pytest.mark.parametrize("expected_output", [expected_output])
def test_evaluate_is_safe(expected_output, mock):
    test = Netprot(protocols=mock[0], exceptions=mock[1], separator="/")
    test.standardize()
    assert test.is_safe(safe_list=["TCP/443", "TCP/22"]) == expected_output


expected_output = [False, False, False, False, False, False, False, False, False, False]


@pytest.mark.parametrize("expected_output", [expected_output])
def test_evaluate_is_unsafe(expected_output, mock):
    test = Netprot(protocols=mock[0], exceptions=mock[1], separator="/")
    test.standardize()
    assert test.is_unsafe(unsafe_list=["TCP/53"]) == expected_output
