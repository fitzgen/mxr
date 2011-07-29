import re

__all__ = ("parse",)

done_searching_re = re.compile(re.escape(".status.searching {display: none}"))
tree_re = re.compile(r'(/[\w-]*/source)/')

file_re = re.compile(r'href="(.+)#\d+"')
line_re = re.compile(r'line (\d+)')
match_re = re.compile(r'-- (.+)<br>')

def parse_result(opts, line):
    filename = file_re.search(line).group(1)
    filename = re.sub(tree_re, "", filename, 1)

    lineno = line_re.search(line).group(1)
    lineno = int(lineno)

    match = match_re.search(line).group(1)
    match = match.replace("&gt;", ">")
    match = match.replace("&lt;", "<")
    match = match.replace("&amp;", "&")
    match = re.sub(r"(<.*?>)", "", match)

    return (filename, lineno, match)

def parse(opts, handler):
    handler = iter(handler)

    for line in handler:
        if done_searching_re.search(line) != None:
            raise StopIteration
        try:
            yield parse_result(opts, line)
        except (ValueError, AttributeError, re.error), e:
            pass

    raise StopIteration
