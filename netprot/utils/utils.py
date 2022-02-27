def cosmetic(protocols):
    standardize_protocols = [protocol.upper() for protocol in protocols]
    standardize_protocols.sort()

    return standardize_protocols


def cleaner(protocols):
    return [protocol.lower().lstrip().rstrip() for protocol in protocols]
