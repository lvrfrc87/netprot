"""Utilities to standardize ingress and egres list of string."""


def cosmetic(protocols):
    """Standardize returned list."""
    standardize_protocols = [protocol.upper() for protocol in protocols]
    standardize_protocols.sort()

    return standardize_protocols


def cleaner(protocols):
    """Standardize argument list."""
    return [protocol.lower().lstrip().rstrip() for protocol in protocols]
