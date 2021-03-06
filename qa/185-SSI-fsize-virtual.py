from base import *

DIR   = "ssi4"
MAGIC = '<a href="http://www.alobbs.com/">Alvaro</a>'
INC   = "test_185.inc"
FILE  = "example.shtml"

CONF = """
vserver!1!rule!1850!match = directory
vserver!1!rule!1850!match!directory = /%s
vserver!1!rule!1850!handler = ssi
""" % (DIR)

FILE_CONTENT = """
<html>
  <head>
    <title>Cherokee QA Test: SSI file size</title>
    <!-- example -->
  </head>
  <body>
    size=<!--#fsize virtual="%s" -->
  </body>
</html>
""" % (INC)

class Test (TestBase):
    def __init__ (self):
        TestBase.__init__ (self, __file__)
        self.name              = "SSI: file size: virtual"
        self.request           = "GET /%s/%s HTTP/1.0\r\n"%(DIR, FILE)
        self.expected_error    = 200
        self.expected_content  = ['size=%d'%(len(MAGIC))]
        self.conf              = CONF

    def Prepare (self, www):
        d = self.Mkdir (www, DIR)
        self.WriteFile (d,  FILE, 0444, FILE_CONTENT)
        self.WriteFile (www, INC, 0444, MAGIC)

