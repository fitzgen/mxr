import urllib2

__all__ = ("fetch",)

def fetch(opts, query=None, *places):
    if not query:
        raise Exception("Must pass in a query")
    if places:
        raise NotYetImplemented

    url = "http://mxr.mozilla.org/mozilla-central/search"
    url += "?string=%s" % query
    url += "&tree=%s" % opts.tree
    if not opts.ignore_case:
        url += "&case=on"
    if opts.identifier:
        raise NotYetImplemented

    return urllib2.urlopen(url)
