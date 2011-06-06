import urllib

def recursive_urlencode(d):
    def recursion(d, base=None):
        pairs = []

        for key, value in d.items():
            if hasattr(value, 'values'):
                pairs += recursion(value, key)
            else:
                new_pair = None
                if base:
                    new_pair = "%s%%5B%s%%5D=%s" % (base, urllib.quote(unicode(key)), urllib.quote(unicode(value)))
                else:
                    new_pair = "%s=%s" % (urllib.quote(unicode(key)), urllib.quote(unicode(value)))
                pairs.append(new_pair)
        return pairs

    return '&'.join(recursion(d))