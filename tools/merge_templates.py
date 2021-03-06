#!/usr/bin/env python

'''
I used to use this to keep the sourceforge pages up to date with the
latest documentation and I like to keep a copy of the distribution
on the web site so that it will be compatible with
The Vaults of Parnasus which requires a direct URL link to a
tar ball distribution. I don't advertise the package this way.

PEXPECT LICENSE

    This license is approved by the OSI and FSF as GPL-compatible.
        http://opensource.org/licenses/isc-license.txt

    Copyright (c) 2012, Noah Spurrier <noah@noah.org>
    PERMISSION TO USE, COPY, MODIFY, AND/OR DISTRIBUTE THIS SOFTWARE FOR ANY
    PURPOSE WITH OR WITHOUT FEE IS HEREBY GRANTED, PROVIDED THAT THE ABOVE
    COPYRIGHT NOTICE AND THIS PERMISSION NOTICE APPEAR IN ALL COPIES.
    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''
import sys, os, re
import pyed
try:
    import pexpect
except:
    # this happens if Pexpect was never installed to begin with.
    sys.path.insert(0, '.')
    import pexpect

# extract the version number from the pexpect.py source.
d = pyed.pyed()
d.read ("pexpect.py")
d.first('^__version__')
r = re.search("'([0-9]\.[0-9])'", d.cur_line)
version = r.group(1)

# Edit the index.html to update current VERSION.
d = pyed.pyed()
d.read ("doc/index.template.html")
for cl in d.match_lines('.*VERSION.*'):
    d.cur_line = d.cur_line.replace('VERSION', version)
d.write("doc/index.html")

# Edit the setup.py to update current VERSION.
d = pyed.pyed()
d.read ("setup.py.template")
for cl in d.match_lines('.*VERSION.*'):
    d.cur_line = d.cur_line.replace('VERSION', version)
d.write("setup.py")
os.chmod("setup.py", 0755)

