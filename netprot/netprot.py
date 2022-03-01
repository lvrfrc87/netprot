#!/usr/bin/env python3
"""Netprot: library for network protocols normalization and evaluation."""
import re
from collections import Counter


class Netprot:
    """Netprot Class implementation."""

    def __init__(self, protocols, separator="/"):
        """__init__ method."""
        # Validate protocols and protocols element data type.
        if not isinstance(protocols, list) and not any(isinstance(element, str) for element in protocols):
            raise TypeError(
                """Protocols must be a list of strings.
                i.e --> ['TCP/443', 'UDP/53']"""
            )
        self.protocols = protocols
        # Validate separator data type.
        if separator and not isinstance(separator, str):
            raise TypeError("Separator must be of type string. i.e. --> '/'")

        self.separator = separator

    @staticmethod
    def _cosmetic(egress_list):
        """Standardize returned list."""
        standardize_protocols = [protocol.upper() for protocol in egress_list]
        standardize_protocols.sort()

        return standardize_protocols

    @staticmethod
    def _cleaner(inggress_list):
        """Standardize argument list."""
        return [protocol.lower().lstrip().rstrip() for protocol in inggress_list]

    @staticmethod
    def _find_duplicates(string):
        elements = Counter(string)
        return [key for key, value in elements.items() if value > 1]

    def standardize(self):
        """Standardize list fo protocosl. Run normalize(), validate() and remove_duplicates()."""

        def normalize():
            """Normalize list of strings containing protocol and port."""
            normalized_protocols = list()
            for protocol in self._cleaner(self.protocols):
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
                            # Case where self.separator is used twice TCP/443/HTTPS
                            if self.separator in self._find_duplicates(protocol):
                                normalized_protocols.append(
                                    f"{self.separator}".join(protocol.split(self.separator)[0:2])
                                )
                            else:
                                index = protocol.index(result.group(4))
                                normalized_protocols.append(protocol[:index])
                        else:
                            normalized_protocols.append(protocol)
                # catch 'icmp' and 'any'
                else:
                    normalized_protocols.append(protocol)
            self.protocols = self._cosmetic(normalized_protocols)
            return True

        def validate():
            """Validate list of normalized protocols and ports."""
            invalid_services = list()
            protocols = self._cleaner(self.protocols)
            for protocol in protocols:
                if protocol not in ("icmp", "any"):
                    if protocol[3] == self.separator:
                        splitted_protocol = protocol.split(self.separator)
                        if splitted_protocol[0] not in ("tcp", "udp") and not 0 > int(splitted_protocol[1]) > 65535:
                            invalid_services.append(protocol)
                    else:
                        invalid_services.append(protocol)

            if invalid_services:
                for service in invalid_services:
                    protocols.remove(service)
                self.protocols = self._cosmetic(protocols)
                return self._cosmetic(invalid_services)

            self.protocols = self._cosmetic(protocols)
            return list()

        def remove_duplicates():
            """Remove duplicated elements."""
            setted_protocols = set()
            duplicates = [
                element for element in self.protocols if element in setted_protocols or setted_protocols.add(element)
            ]

            self.protocols = self._cosmetic(list(setted_protocols))

            if duplicates:
                return duplicates
            return list()

        if normalize():
            return (validate(), remove_duplicates(), self.protocols)

    def is_well_known(self):
        """Evaluate port if lower than 1024."""
        is_well_known = list()

        for protocol in self._cleaner(self.protocols):
            if protocol not in ("icmp", "any"):
                port_number = int(protocol.split(self.separator)[-1])
                if port_number <= 1024:
                    is_well_known.append(True)
                else:
                    is_well_known.append(False)
            else:
                is_well_known.append(False)

        if all(is_well_known):
            return (True, is_well_known)
        return (False, is_well_known)

    def is_tcp(self):
        """Evaluate protocol if TCP."""
        is_tcp = list()

        for protocol in self._cleaner(self.protocols):
            if protocol not in ("icmp", "any"):
                prot = protocol.split(self.separator)[0]
                if prot == "tcp":
                    is_tcp.append(True)
                else:
                    is_tcp.append(False)
            else:
                is_tcp.append(False)

        if all(is_tcp):
            return (True, is_tcp)
        return (False, is_tcp)

    def is_udp(self):
        """Evaluate protocol if UDP."""
        id_udp = list()

        for protocol in self._cleaner(self.protocols):
            if protocol not in ("icmp", "any"):
                prot = protocol.split(self.separator)[0]
                if prot == "udp":
                    id_udp.append(True)
                else:
                    id_udp.append(False)
            else:
                id_udp.append(False)

        if all(id_udp):
            return (True, id_udp)
        return (False, id_udp)

    def is_safe(self, safe_list):
        """Evaluate port if is safe."""
        result = list()
        for element in self.protocols:
            if element not in safe_list:
                result.append(False)
            else:
                result.append(True)

        return result

    def is_unsafe(self, unsafe_list):
        """Evaluate port if is not safe."""
        result = list()
        for element in self.protocols:
            if element in unsafe_list:
                result.append(True)
            else:
                result.append(False)

        return result
