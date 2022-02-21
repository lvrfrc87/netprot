#!/usr/bin/env python3
import re

class Netprot():

    def __init__(self, protocols, separator='/'):
        # Validate protocols and protocols element data type.
        if not isinstance(protocols, list) and not any(isinstance(element, str) for element in protocols):
            raise TypeError("Protocols must be a list of strings. i.e --> ['TCP/443', 'UDP/53']")
        else:
            # lower all elements of protocol. Will later upper.
            protocols_lower = [protocol.lower().lstrip().rstrip() for protocol in protocols]
            
        self.protocols = protocols_lower

        # Validate separator data type.
        if separator and not isinstance(separator, str):
            raise TypeError("Separator must be of type string. i.e. --> '/'")
        else:
            self.separator = separator

    def standardize(self):
        self.normalize(self)
        validation_result, failing_validation = self.validate(self) 
        if not validation_result:
            return failing_validation
        self.remove_duplicates(self)


    def normalize(self):
        normalized_protocols = list()
 
        for protocol in self.protocols:
            # https://regex101.com/r/DyKeqr/1
            result = re.search(r"\b([a-z]+)(\W|_)(\d+)(.)?(\d+)?(\w+)?", protocol)
            if result:
                # replace whatever separator with self.separator
                protocol = protocol.replace(result.group(2), self.separator, 1)
                
                splitted_protocol = protocol.split(self.separator)
                if len(splitted_protocol) > 1:
                    # Expand TCP/1024-1026 --> TCP/1024, TCP/1025, TCP/1026
                    if result.group(4) and result.group(5):
                        try:
                            start = int(result.group(3))
                            end = int(result.group(5)) + 1
                            for port in range(start, end):
                                normalized_protocols.append(f"{protocol[0:3]}/{port}")
                        except ValueError:
                            continue
                    # Normalize TCP/443-HTTPS --> TCP/443
                    elif result.group(4) and result.group(6):
                        index = protocol.index(result.group(4))
                        normalized_protocols.append(protocol[:index])
                    else:
                        normalized_protocols.append(protocol)
            # catch 'icmp' and 'any'
            else:
                normalized_protocols.append(protocol)                
 
        protocols_upper = [protocol.upper() for protocol in normalized_protocols]
        protocols_upper.sort()

        return protocols_upper


    def validate(self):
        invalid_services = list()
        
        for protocol in self.protocols:
            if protocol[4] == '/':
                splitted_protocol = protocol.split('/')
                if splitted_protocol[0] not in ('tcp', 'udp') and not 0 > int(splitted_protocol[1]) > 65535:
                    invalid_services.append(protocol)
                else:
                    continue
            else:
                invalid_services.append(protocol)

        if invalid_services:
            return (False, invalid_services)


    def remove_duplicates(self):
        self.protocols[:] = list(set(self.protocols))


    def is_well_known(self):
        pass

    def is_safe(self):
        pass

    def is_unsafe(self):
        pass

    def is_tcp(self):
        pass

    def is_udp(self):
        pass


