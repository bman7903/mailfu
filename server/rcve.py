# -*- coding: utf-8 -*-

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

from seccure import decrypt
from base64 import b64decode
from sys import exit
from re import sub
from subprocess import call, Popen, PIPE

import cgi


try:
  fd  = open( 'pvk.txt', 'r' )

  global sec
  sec = str( fd.readline().strip() )

  fd.close()

except:
   print('ERROR :  Problem reading private key!')
   exit(1)


def ppst( post ):
  ### remove, reformat post from header
  post = str( post )

  for p in post.split(", '"):
     p  = str( p )
     lp = len( p )
     if lp > 45:
        p = str( p.split("'")[0] )
        return p

  print( post )


  return

def dcry( sec, msg ):
  ### decrypt ciphertext from phrase
  dc = b64decode( msg )
  dc = decrypt( dc, b'%s' % sec )
  return dc



def smack( environ, start_response ):
  setup_testing_defaults(environ)
  
  status         = '200 OK'
  headers        = [('Server', 'Apache'),('Content-type', 'text/html')]
 
  post_env = environ.copy()
  post_env['QUERY_STRING'] = ''
  post = cgi.FieldStorage(
    fp=environ['wsgi.input'],
    environ=post_env,
    keep_blank_values=True
  )

  msg = str( ppst( post ) )
  dec = str( dcry( sec, msg ) )
  dec = str( b64decode( dec ) )

  fp  = 'out.txt'
  snd = 'snd.sh'
  fd  = open( fp, 'w' )
  fd.write( dec )
  fd.close()

  p = Popen( [ '/mnt/mailfu/server/snd.sh' ], stdout = PIPE )
  o, err = p.communicate()
  print(o)
  #call(cmd, shell='/bin/bash')
  #print(dec)

  headers        = [ ('Server', 'Apache2'),('Content-type', 'text/plain' ) ]
  start_response( status, headers )
  return status



def phew():
  try:
     from sys import argv
     port        = int( argv[1] )
  except:
     port        = 80

  httpd          = make_server('0.0.0.0', port, smack )


  print( "Accepting on port %d" % port )
  httpd.serve_forever()
  con.close()

phew()


