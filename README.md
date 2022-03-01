# netprot
A system-indipendent network protocol manipulation and evaluation library. 
`netprod` wants to be a library capable standardize and evaluate list of strings rappresenting Network Protocols. The idea is to provide a tool similar to `netaddr` that can help to enhance and simplify code logic wherever is required.

### Installation

```bash
pip3 install netprod
```

### HOW TO

First thing, we need to initialize an instance of `Netprod` class, passing as arguments a list of string - where each string should rappresent a network protocol and corresponding port. `separator` argument is also possible to pass it as kwarg and will be used to standardize our strings. By default, `separator` is equal to `/` 

```python
>>> from netprot.netprot import Netprot 
>>> my_list = ['tcp-443-https', 'UDP/53', 'ICMP', 'any', 'tcp/1024-1026', 'TCPP-80']
>>> my_protocols = Netprot(my_list, separator='/')
```

Once the instance of the class is created, we can call `normalize` method which will return a tuple containing method boolena execution result (True or False), the normalized list and an empty list. The empty list is returned for consistency with the other methods - more on that later.

```python
>>> my_protocols.normalize()
(True, ['ANY', 'ICMP', 'TCP/1024', 'TCP/1025', 'TCP/1026', 'TCP/443', 'TCPP/80', 'UDP/53'], [])
```

As we can see, we have:

- Strings using the same `separator`.
- Trailing words such as `https` is removed as not needed
- Protocols defined as `tcp/1024-1026` are unpacked for each port in range defined
- All strings are upper cases
- List is sorted


Once we have normalized our protocols, we can validate them

