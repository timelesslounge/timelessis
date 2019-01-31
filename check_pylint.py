import argparse
import sys

from pylint.lint import Run


parser = argparse.ArgumentParser(description='Run py linter')
parser.add_argument('threshold', type=int, nargs='?', default=8,
                    help='a minimal threshold for quality score')


def run_pylint(threshold):
    run = Run(['timeless'], do_exit=False)
    score = run.linter.stats['global_note']

    if score < threshold:
        sys.exit(2)


if __name__ == "__main__":
    args = parser.parse_args()
    run_pylint(args.threshold)
