#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# build_html.py - html generator for HUMA docs
#
# Copyright (C) 2011 Homin Lee <ff4500@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

import os
import glob
import re
from BeautifulSoup import BeautifulSoup as BS

addr = 'http://www.eleparts.co.kr/front/productsearch.php?s_check=all&search='

if __name__ == '__main__':
    for md in glob.glob("*.md"):
        os.system('pandoc %s > %s'%(md, md.replace('.md', '.html')))

    ptn = re.compile(r'(EPX.....)')
    for html in glob.glob('*.html'):
        lines = open(html).readlines()
        newHtml = ''
        for line in lines:
            newHtml += ptn.sub(r'<a href=%s\1>\1<a>'%addr, line)

        soup = BS(newHtml)
        print html
        wp = open(html, 'w')
        wp.write(soup.prettify())

            

# vim: et sw=4 fenc=utf-8:

