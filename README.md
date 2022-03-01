# netprot
A system-indipendent network protocol manipulation and evaluation library. 
`netprod` wants to be a library capable standardize and evaluate list of strings rappresenting Network Protocols. The idea is to provide a tool similar to `netaddr` that can help to enhance and simplify code logic wherever is required.

### Installation

```bash
pip3 install netprod
```

Package available [here](https://pypi.org/project/netprot/)

### HOW TO

First thing, we need to initialize an instance of `Netprod` class, passing as arguments a list of string - where each string should rappresent a network protocol and corresponding port. `separator` argument is also possible to pass it as kwarg and will be used to standardize our strings. By default, `separator` is equal to `/` 

```python
>>> from netprot.netprot import Netprot 
>>> my_list = ['tcp-443-https', 'UDP/53', 'ICMP', 'any', 'tcp/1024-1026', 'TCPP-80', 'tcp/443']
>>> my_protocols = Netprot(my_list, separator='/')
```

Once the instance of the class is created, we can call `standardize` method which will return a tuple containing pontential unlegal protocols and ports, duplicates - if any, and a standardize list of protocols and port.

```python
>>> my_protocols.standardize()
(['TCPP/80'], ['TCP/443'], ['ANY', 'ICMP', 'TCP/1024', 'TCP/1025', 'TCP/1026', 'TCP/443', 'UDP/53'])
```

As we can see, we have:

- Strings using the same `separator`.
- Trailing words such as `https` is removed as not needed
- Protocols defined as `tcp/1024-1026` are unpacked for each port in range defined
- Unlegal protocosl such as `TCPP/80` are removed
- Duplicates are also removed
- All strings are upper cases
- List is sorted
- `ICMP` and `ANY` are recognized as legal tring and paased through


`Netprod` not only standardize data, but also evaluate them. Let's have a look to the other methods 

:warning:
List of protocols must be standardized first.

Let's check if the ports are part of well known range of ports (0 to 1024)

```python
>>> my_protocols.is_well_known()
(False, [False, False, True, False, False, True, True])
```

As we can see, some ports are failing to be lower than 1024, hence we return `False` plus a list of bools for each ports.

What about if we want to find those are `TCP`...

```python
>>> my_protocols.is_tcp()
(False, [False, False, True, True, True, True, False])
```

... or `UDP`?
```python
>>> my_protocols.is_udp()
(False, [False, False, False, False, False, False, True])
```

Great! What if we want figure out if our port and protocols are safe or not?
Let's define a list of safe - or unsafe - ports and protocols and paased them to `is_safe` or `is_unsafe` method.

```python
>>> my_safe_applications = ['TCP/443', 'UDP/53']
>>> my_protocols.is_safe(my_safe_applications)
[False, False, False, False, False, True, True]
>>> my_unsafe_applications = ['ICMP', 'ANY']
>>> my_protocols.is_unsafe(my_unsafe_applications)
[True, True, False, False, False, False, False]
```

And that's all, folks!