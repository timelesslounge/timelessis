"""
Scripts to enforce certain code style rules.
"""
import glob
import re
import sys


def double_qoutes_only():
    """ DoubleQuotesOnly; Forbid usage of single-quoted strings """
    for filename in glob.iglob("./timeless/**/*.py", recursive=True):
        with open(filename, "r+") as f:
            data = f.read()
            pattern = "['](?=[^\"]*(?:\"[^\"]*\"[^\"]*)*$)"
            prev_line = -1
            prev_offset = 0
            match_found = False
            for m in re.finditer(pattern, data):
                if not match_found:
                    print("Single-quotes are forbidden in .py files!")
                    match_found = True
                start = m.start()
                lineno = data.count('\n', 0, start) + 1
                offset = start - data.rfind('\n', 0, start)
                word = m.group(0)
                if prev_line == lineno:
                    print("%s(%s,%s-%s): %s" %
                          (f.name, lineno, prev_offset, offset, word))
                prev_line = lineno
                prev_offset = offset
            if match_found:
                sys.exit(2)

double_qoutes_only()
