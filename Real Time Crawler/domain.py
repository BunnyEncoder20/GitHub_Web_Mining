from urllib.parse import urlparse

# Getting the domain name (example.com)

def get_domain__name(url) : 
    try : 
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except :
        return ''

# Getting the sub domain name (name.example.com)

def get_sub_domain_name(url) :
    try : 
        return urlparse(url).netloc
    except :
        return ''


# print(get_domain__name('https://en.wikipedia.org/wiki/Toyota_Supra#'))