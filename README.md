# netprot
A system-indipendent network protocol manipulation and evaluation library. 
`netprod` wants to be a library capable standardize and evaluate list of strings rappresenting Network Protocols. The idea is to provide a tool similar to `netaddr` that can help to enhance and simplify code logic wherever is required.

### Installation

```bash
pip3 install netprod
```

### HOW TO

First thing, we need to initiate an instance of `netprod` class, passing a list of string as argument. Each string should rappresent a network protocol and corresponding port. For example `TCP/443` or `UDP-53`.

