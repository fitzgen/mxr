from optparse import OptionParser

__all__ = ("parse",)

parser = OptionParser()

parser.add_option("-i", "--ignore-case", dest="ignore_case",
                  default=False,
                  action="store_true",
                  help="Ignore case distinctions")

parser.add_option("-n", "--name-only", dest="name_only",
                  default=False,
                  action="store_true",
                  help="Show only the names of files containing matches, not the matches themselves.")

parser.add_option("-d", "--identifier", dest="identifier",
                  default=False,
                  action="store_true",
                  help="The query parameter is a single identifier. Makes searching faster.")

parser.add_option("-t", "--tree", dest="tree",
                  default="mozilla-central",
                  action="store",
                  type="string",
                  help="Which repository tree to search.")

def parse():
    return parser.parse_args()
