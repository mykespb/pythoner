#!/usr/bin/env python3

# rekode
# (C) Mikhail Kolodin
# 2021-04-29 2021-04-29 0.1
# not ready yet

# recode file f from encoding1 to encoding2
# params:
# -n --name file
# -f --from enc1  [cp1251]
# -t --to enc2    [utf8]
# -a --all
# -x --ext extension_to_add
# -u --unlist extension_to_exclude
# -h --help

import sys, getopt

def main(argv):

    try:
        opts, args = getopt.getopt (argv, 'hf:t:n:x:u:a',
            ["from=" "to=", "name=", "ext=", "unlist=", "help"])
    except:
        print('erros, check params')
        sys.exit(1)

    for opt, agr in opts:

        if opt in ('-h', '--help'):
            print("""
            Good program to recode it all
            """)
            sys.exit(0)

        elif opt in ('-f', '--from'):
            print(f"convert from {arg}")

        elif opt in ('-t', '--to'):
            print(f"convert to {arg}")

        elif opt in ('-n', '--name'):
            print(f"use file {opt}")

        elif opt in ('-a', '--all'):
            print("convert all files")

        elif opt in ('x', '--ext'):
            print(f"convert extension {arg}")

        else:
            print("whatever else...")

    print("here we process something...")

if __name__ == "__main__":
    main(sys.argv[1:])
