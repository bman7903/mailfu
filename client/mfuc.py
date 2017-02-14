# -*- coding: utf-8 -*-

from base64 import b64encode
from seccure import encrypt
from requests import post


def vemail( eml ):
  ### validate email format

  eml = str( eml )

  if '@' in eml:
     fqdn = str( eml.split('@')[-1] )

     if '.' in fqdn:
       l  = str( fqdn.split('.')[0] )
       r  = str( fqdn.split('.')[-1] )
       ll = len( l )
       lr = len( r )

       if ll > 1:
          if lr > 1:
             return True

  return

def ecry( ek, msg ):
  ### encrypt message

  cip = str( encrypt( b'%s' % msg, b'%s' % ek ) )
  b6c = str( b64encode( cip ) )
  return b6c



def zang():
  ### main console

  from sys import argv
  proc = msg = None
  la   = len( argv )

  if la > 4:
     #headers = {'User-Agent': 'Mozilla/5.0'}
     headers = {u'Content-type': u'image/base64'}
     rcpt = str( argv[1] )
     sndr = str( argv[2] )
     sbjt = str( argv[3] )
     msg  = str( argv[4] )

     if vemail( rcpt ):
        if vemail( sndr ):

          fd  = open( 'pbk.txt', 'r' )
          pbk = str( fd.readline() )
          fd.close()

          fd  = open( 'pxip.txt', 'r' )
          pxp = str( fd.readline().strip() )
          fd.close()

          msg = str( 'To: %s#From: %s#Subject: %s#%s#.#' % ( rcpt, sndr, sbjt, msg ) )
          msg = str( b64encode( msg ) )
          msg =  str( ecry( pbk,msg ) )

          if not '://' in pxp:
             pxp = str( 'http://%s' % pxp )

          try:
             pst = post( pxp, headers=headers, data=msg )
             print('message sent')

          except:
             print('network error, check your connection')

          return
     print( 'Ivalid email format' )

  if la < 5:
     print( './Usage ./mfuc.py to from subject "message content"' )

if __name__ == "__main__":
  zang()
