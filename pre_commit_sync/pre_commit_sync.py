#!/usr/bin/python
import sys
import argparse
from pathlib import Path
import urllib.request

def process(fname, url):

    f = Path(fname.strip())
    with urllib.request.urlopen(url) as web:
        content = web.read()

    if f.exists():
        file_content = f.read_bytes()
    else:
        file_content = None

    if content != file_content:
        with open(f, 'wb') as fh:
            fh.write(content)
        print(f'File has been updated: {fname}\n  (source: {url})')
        return True
    return False

def main(argv=None):
    exit_code = False
    missing_from_git = []

    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='It will ignore file names.')
    parser.add_argument('--sync', action='append', default=[])
    parser.add_argument('--sync-without-git', dest='sync_without_git', action='append', default=[])
    args = parser.parse_args()
    filenames = set(args.filenames)

    for s in args.sync:
        fname, url = s.split(':',1)
        exit_code |= process(fname, url)

        if fname not in filenames:
            missing_from_git.append(fname)

    for s in args.sync_without_git:
        fname, url = s.split(':',1)
        exit_code |= process(fname, url)

    if len(missing_from_git)>0:
        exit_code = True
        if len(missing_from_git) == 1:
            print(f'This file is missing from git:', file=sys.stderr)
        else:
            print(f'These files are missing from git:', file=sys.stderr)
        for fname in missing_from_git:
            print(f'  {fname}', file=sys.stderr)

    if exit_code:
        sys.exit(1)

if __name__ == '__main__':
    main()
