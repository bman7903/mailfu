# -*- coding: utf-8 -*-


from base64 import b64encode, b64decode
from seccure import passphrase_to_pubkey, encrypt, decrypt


def eky( prs ):
  ### pubkey from phrase

  ek  = str( passphrase_to_pubkey( b'%s' % prs ) )
  return ek


def ecry( ek, msg ):
  ### encrypt message
  #print('encrypting %s with %s' % ( msg, ek ) )

  cip = str( encrypt( b'%s' % msg, b'%s' % ek ) )
  b6c = str( b64encode( cip ) )
  return b6c


def dcry( sec, msg ):
  ### decrypt ciphertext from phrase
  #print('decrypting %s with %s' % (  msg, sec ) )

  dc = b64decode( msg )
  dc = decrypt( dc, b'%s' % sec )
  return dc


def zim( proc, msg ):
  ### parse arg, return ecc message

  sec = 'zimdadadin'
  ek  = eky( sec )

  if proc == 'e':
     return str( ecry( ek,msg ) ) 

  if proc == 'd':
     return str( dcry( sec, msg ) )

  return


def zang():
  ### main console  

  from sys import argv
  proc = msg = None
  la   = len( argv )  

  if la > 2:
     proc =  str( argv[1] )
     msg  =  str( argv[2] )

  z = zim( proc, msg )

  if la > 2:
    print( z )

  if la < 2:
     print( './Usage ./ecv.py {e,d} "message"' )

if __name__ == "__main__":
  zang()
