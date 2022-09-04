#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-mkmeet3k.py 2015-09-18 2022-09-04 1.10
# (C) Mikhail Kolodin, 2015-2022
# format bards songs file with simplest markdown into web page for easy searching and singing
# call:    mk-mkmeet3k.py file.txt
# result:  file.html (all in one)

import sys, pprint, re

# version
ver = '1.10'
adate = '2022-09-04'

inname = outname = None
#inname  = "all-2015fall.txt"
#outname = "all-2015fall.html"

#index
index = []   # all songs list
snum = 0     # song number
title = ""   # file title

part = 0
lino = 0
total = 0

def urly (tin):
	""" make urls refs """
	return re.sub (r'(https?://[-a-zA-Z0-9:/_%()?=+.,#]+)', r'<a href="\1" target=song>\1</a>', tin)

def main():
    """ main fun """
    global inname, outname
    print ("This is mk-mkmeet.py")
    inname = inname or sys.argv[1]
    if not inname:
        print ("No good file name. Quitting.")
    else:
        if inname[-4:] == ".txt":
            outname = inname[:-4] + "-3k.html"
        else:
            outname = inname + "-3k.html"
        print ("Inname=%s, outname=%s.\nStarting." % (inname, outname))
        pass1()
        pass2()

def pass1 ():
    """collect index"""
    global inname, outname, index, snum, title, part, lino, total
    full = ""
    linefrom = 0
    print ("pass 1: making index")
    with open (inname) as infile:
        lino = 0
        was = ""
        for line in infile:
            lino += 1
        	
            if line.startswith("===="):
                # we have file title
                title = was.strip()
                print ("file: %s" % (title,))
                linefrom = lino
                continue

            if line.startswith("----"):
                # we have song title
                total += 1
                full = was.strip()
                print ("song: %s." % (full,))
                snum += 1
                index.append([snum, full, part, lino, 0])
                continue

            if line.startswith("#PART"):
	            part = int(line[6:].strip())
	            was = ""
	            lino -= linefrom - 1
	            continue

            # normal line
            if index:
                index[-1][-1] += 1
            was = line

def pass2 ():
    """output result"""
    global inname, outname, index, snum, title, total
    full = ""
    print ("pass 2: making html")
    pprint .pprint (index)

    index.sort (key=lambda x: x[1:])

    with open (outname, 'w') as outfile:
        print ("""<!DOCTYPE HTML>
<html lang='ru'>
<head>
<meta encoding=utf8>
<meta http-equiv = "content-type" content = "text/html; charset = utf-8">
<meta name="keywords" content="mikhail kolodin, bards, song, author, st.petersburg, колодин, авторская песня, барды, parties">
<meta name="description" content="mikhail kolodin bards song parties">
<title>%s</title>
<!-- program mk-mkmeet.py ver. %s of %s (C) Mikhail Kolodin -->
</head>
<body>
<h1>%s</h1>

""" % (title, ver, adate, title), file=outfile)

        print ("<a name='0'>", file=outfile)
        print ("\n<div><table frame=void rules=cols cellpadding=5mm ><tr>", file=outfile)
        for onum, song in enumerate(index):
            if onum % 90 == 0:
                print ("\n</td></tr></table></div>\n\n<div><table frame=void rules=cols cellpadding=5mm ><tr>", file=outfile)
            if onum % 30 == 0:
                print ("\n<td align=left valign=top>\n", file=outfile)
            anum, afull, part, lino, alen = song
            if part:
	            print ("<div align=left valign=top><a href='#%d'>%03d. %s.</a> (%d:%d+%d)</div>" % (anum, anum, afull, part, lino, alen), file=outfile)
            else:
	            print ("<div align=left valign=top><a href='#%d'>%03d. %s.</a> (%d+%d)</div>" % (anum, anum, afull, lino, alen), file=outfile)
        print ("\n</tr></table>\n</div>\n<br/ >\n", file=outfile)

        snum = 0
        row = 0
        with open (inname) as infile:
            was = wass = ""
            cwas = 0
            dout = 0
            for line in infile:
                if line.startswith("===="):
                    # we have file title
                    dout = 0
                    title = was.strip()
                    print ("file: %s" % (title,))
                    continue

                if line.startswith("----"):
                    # we have song title
                    dout = 1
                    full = was.strip()
                    print ("song: %s." % (full,))
                    snum += 1
                    if snum>1:
                        print ("\n</pre>\n</td></tr>\n</table>\n", file=outfile)
                    print ("\n<a href='#0'>К началу...</a>\n<hr>\n", file=outfile)
                    print ("<a name='%d'>" % (snum,), file=outfile)
                    print ("<p><b>%s.</b></p>" % (full,), file=outfile)

                    print ("\n<div>\n<table border=0 frame=void rules=cols cellpadding=5mm  ><tr><td align=left valign=top cellpadding=5mm>", file=outfile)
                    row = 0
                    cwas = 1

                    print ("\n<pre>", file=outfile)
                    continue

                if dout == 1:
                    dout = 2

                # normal line: pass
                if dout > 1 and (wass != title and wass != full):
                    if wass != "" or cwas == 0:
                        print (urly(was), file=outfile, end="")
                        dout = 3
                        row += 1
                        if row == 30:
                            row = 0
                            print ("</pre></td><td align=left valign=top cellpadding=5mm><pre>", file=outfile)
                            cwas = 1

                    if was.strip() == "":
                        cwas += 1
                    else:
                        cwas = 0

                elif dout >2 :
                    print (urly(was), file=outfile, end="")

                # end of line
                was = line
                wass = was.strip()

        print ("""
</pre>
</table>
<a href='#0'>К началу...</a>\n<hr>

<p>
<b>
Всего песен: %d.
</b>
</p>
</body>
</html>
""" % (total,), file=outfile)

# call 'em
main()

# details.

#~ input file format:

#~ name of meetimg
#~ =========================

#~ author's name and surname. song name
#~ -------------------------------------

#~ text of song (out as <pre>)
#~ ...

#~ output contains contents part first

#~ all data are in utf-8 !

# TBD: don't cut inside couplets, if possible.
