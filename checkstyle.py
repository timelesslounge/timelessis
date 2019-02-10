"""
Methods to enforce certain code style rules.
"""
import glob
import re
import sys


def double_qoutes_only():
    """ DoubleQuotesOnly; Forbid usage of single-quoted strings """
    pattern = "['](?=[^\"]*(?:\"[^\"]*\"[^\"]*)*$)"
    for filename in glob.iglob("./timeless/**/*.py", recursive=True):
        with open(filename, "r+") as f:
            # read file as string containing all the lines divided by \n
            data = f.read()
            prev_line = 0
            prev_offset = 0
            match_found = False
            for m in re.finditer(pattern, data):
                match_found = True
                start = m.start()
                # count number of \n chars from 0 to start to get line number
                current_line = data.count("\n", 0, start) + 1
                # find position of single qoute in line
                offset = start - data.rfind("\n", 0, start)
                if prev_line == current_line:
                    print(f"Found single-qoutes: {f.name}({current_line},"
                          f"{prev_offset}-{offset})")
                prev_line = current_line
                prev_offset = offset
            if match_found:
                sys.exit(2)

if __name__ == "__main__":
    double_qoutes_only()
