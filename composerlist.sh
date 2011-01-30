#!/bin/sh
cat composerlist-header.html > generated/composerlist.html
xsltproc --stringparam initial A composerlist.xsl contempworks-a.xml >> generated/composerlist.html
xsltproc --stringparam initial B composerlist.xsl contempworks-b.xml >> generated/composerlist.html
xsltproc --stringparam initial C composerlist.xsl contempworks-c.xml >> generated/composerlist.html
xsltproc --stringparam initial D composerlist.xsl contempworks-d.xml >> generated/composerlist.html
xsltproc --stringparam initial E composerlist.xsl contempworks-e.xml >> generated/composerlist.html
xsltproc --stringparam initial F composerlist.xsl contempworks-f.xml >> generated/composerlist.html
xsltproc --stringparam initial G composerlist.xsl contempworks-g.xml >> generated/composerlist.html
xsltproc --stringparam initial H composerlist.xsl contempworks-h.xml >> generated/composerlist.html
xsltproc --stringparam initial I composerlist.xsl contempworks-i.xml >> generated/composerlist.html
xsltproc --stringparam initial J composerlist.xsl contempworks-j.xml >> generated/composerlist.html
xsltproc --stringparam initial K composerlist.xsl contempworks-k.xml >> generated/composerlist.html
xsltproc --stringparam initial L composerlist.xsl contempworks-l.xml >> generated/composerlist.html
xsltproc --stringparam initial M composerlist.xsl contempworks-m.xml >> generated/composerlist.html
xsltproc --stringparam initial N composerlist.xsl contempworks-n.xml >> generated/composerlist.html
xsltproc --stringparam initial O composerlist.xsl contempworks-o.xml >> generated/composerlist.html
xsltproc --stringparam initial P composerlist.xsl contempworks-p.xml >> generated/composerlist.html
xsltproc --stringparam initial Q composerlist.xsl contempworks-q.xml >> generated/composerlist.html
xsltproc --stringparam initial R composerlist.xsl contempworks-r.xml >> generated/composerlist.html
xsltproc --stringparam initial S composerlist.xsl contempworks-s.xml >> generated/composerlist.html
xsltproc --stringparam initial T composerlist.xsl contempworks-t.xml >> generated/composerlist.html
xsltproc --stringparam initial U composerlist.xsl contempworks-u.xml >> generated/composerlist.html
xsltproc --stringparam initial V composerlist.xsl contempworks-v.xml >> generated/composerlist.html
xsltproc --stringparam initial W composerlist.xsl contempworks-w.xml >> generated/composerlist.html
xsltproc --stringparam initial X composerlist.xsl contempworks-x.xml >> generated/composerlist.html
xsltproc --stringparam initial Y composerlist.xsl contempworks-y.xml >> generated/composerlist.html
xsltproc --stringparam initial Z composerlist.xsl contempworks-z.xml >> generated/composerlist.html
cat composerlist-footer.html >> generated/composerlist.html