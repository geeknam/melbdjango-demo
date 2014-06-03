

def lowercase_domain(email):
    value, domain = email.split('@')
    domain = domain.lower()
    return '@'.join([value, domain])


def lowercase_name(email):
    value, domain = email.split('@')
    value = value.lower()
    return '@'.join([value, domain])