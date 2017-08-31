

# 커맨드 라인 옵션 파싱


import argparse

parser = argparse.ArgumentParser(description='Search somfiles')


parser.add_argument(dest='filenames', metavar='filename', nargs='*')

parser.add_argument('-p', '--pat', metavar='pattern', required=True, dest='patterns', action='append', help='text pattern to search for')

args = parser.parse_args()

print(args.filenames)