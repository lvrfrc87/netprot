import pytest


@pytest.fixture
def mock():
    mock_data = [
        "TCP-443",
        "UDPC-5353",
        "UDP-53",
        "UDP=53",
        "TCP-443",
        "UDP%65535",
        "TCP/65636",
        "TCPUDP$443-HTTPS",
        "TCP-1024-1026",
        "ICMP-1223-1224",
        "TCP/443-HTTPS",
        "ICMP",
        "ANY",
    ]
    return mock_data
