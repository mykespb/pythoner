#!/usr/bin/env python3

# rekode
# (C) Mikhail Kolodin
# 2021-04-29 2021-05-02 0.2
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
# -v --version
# -r --recurse
# -l --level 5   (max depth of recursion)
# -d --doit

import sys, getopt

def main(argv):

    try:
        opts, args = getopt.getopt (argv, 'hf:t:n:x:u:rl:adv',
            ["from=" "to=", "name=", "ext=", "unlist=", "help", "default", "version"])
    except:
        print('errors, check params')
        sys.exit(1)

    fromenc  = 'cp1251'
    toenc = 'utf8'
    exts   = {'txt', 'bbs', 'ion'}
    flist = set()
    recurse = False
    levels = 0
    doit = False

    for opt, agr in opts:

        if opt in ('-h', '--help'):
            print("""
            Good program to recode it all.
            -h --help    help
            -f --from    from encoding ...
            -t --to      to encoding ...
            -a --all     all files
            -x --ext     add extension ... to list
            -u --unlist  unlist extension ...
            -n --name    add file ...
            -r --remove  remove file ... from list
            -d --doit    run even in default mode
	    -r --recurse do recursive processing
	    -l --level   ...levels in depth max
            -v --version show version
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

        elif opt in ('-x', '--ext'):
            print(f"do convert extension {arg}")

        elif opt in ('-u', '--unlist'):
            print(f"do not convert extension {arg}")

        elif opt in ('-v', '--version'):
            print(f"show version and exit")

        else:
            print("whatever else...")

    print(f"here we process something as {doit=}, {fromenc=}, {toenc=}, {exts=}, {flist=}, {recurse=}, {levels=}")

if __name__ == "__main__":
    main(sys.argv[1:])
