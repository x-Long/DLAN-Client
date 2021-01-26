from re import compile, IGNORECASE


# https://stackoverflow.com/questions/2532053/validate-a-hostname-string
def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1]  # strip exactly one dot from the right, if present
    allowed = compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))


