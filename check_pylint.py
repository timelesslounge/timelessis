import argparse
import sys

from pylint.lint import Run


parser = argparse.ArgumentParser(description='Run pylint')
parser.add_argument(
    'threshold', type=int, nargs='?', default=8,
    help='Pls set up threshold for quality score, MAX is 10. '
         'Script will exit with error if quality score is less then threshold.'
)


def run_pylint(threshold):
    run = Run(['timeless'], do_exit=False)
    score = run.linter.stats['global_note']

    if score < threshold:
        sys.exit(2)


if __name__ == "__main__":
    """This script runs pylint checker with threshold value"""
    args = parser.parse_args()
    run_pylint(args.threshold)
