# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2

from metric.header import headers
from ecv import zim


def phd( head ):
  ### return post from header
  for h, r in head:
     r = str( r )
     if r.endswith('='):
       return r
  return


class MainPage(webapp2.RequestHandler):
  def do( self, proc ):
     raw  = self.request
     proc = str( proc )
     head = headers( raw, 'all', proc )

     pst = phd( head )
     dec = zim( 'd', pst )
     print( dec )

     self.response.headers['Content-Type'] = 'text/plain'
     self.response.write('200')

  def post( self, proc=None ):
     self.do('POST')



app = webapp2.WSGIApplication([
    ( '/', MainPage,),
    ('/(.*)', MainPage),
], debug=True,)
