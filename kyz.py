from seccure import passphrase_to_pubkey
from os import path, getcwd, rename
from re import sub

join  = path.join
sep   = path.sep


def eky( prs ):
  ### pubkey from phrase
  ek  = str( passphrase_to_pubkey( b'%s' % prs ) )
  return ek


def pconf( lines ):
  ### parse conf, return server/proxy ip

  sip = pip = None

  for line in lines:
      line = str( line ).strip()

      if 'server_ip' in line:
        print(line)
        sip = str( line.split(' ')[-1] ).strip()

      if 'proxy_ip' in line:
        print( line )
        pip = str( line.split(' ')[-1] ).strip()

  return sip, pip


def zang():
  ### parse conf, gen keys, place items  

  from sys import argv
  sec = ubi = None
  
  if len( argv ) > 1:
     ### define resources
     cnf = str( 'mailfu.conf' )
     prs = str( argv[1] )
     ubi = str( eky( prs ) )
     cwd = str( getcwd() )

     pbk = str( join( sep, cwd, 'client' ) )
     pxi = str( join( sep, pbk, 'pxip.txt' ) )
     pbk = str( join( sep, pbk, 'pbk.txt' ) )
     pbk = open( pbk, 'w' )
     pbk.write( ubi )
     pbk.close()

     pvk = str( join( sep, cwd, 'server' ) )
     pvk = str( join( sep, pvk, 'pvk.txt' ) )
     pvk = open( pvk, 'w' )
     pvk.write( prs )
     pvk.close()

     ### parse conf
     fd  = open( cnf, 'r' )
     lns = fd.readlines()
     cf  = pconf( lns )
     print(cf)
     fd.close()

     sip = str( cf[0] )
     pip = str( cf[1] )

     ### server ip 2 proxy dir
     pxd = str( join( sep, cwd, 'proxy' ) )
     vip = str( join( sep, pxd, 'main.py' ) )
     vnw = str( join( sep, pxd, 'new.txt' ) )

     fd  = open( vip, 'r' )
     lns = fd.readlines()
     fd.close()


     fd = open( vnw, 'w' )
     fd.write('')
     fd.close()

     fd = open( vnw, 'w' )

     for line in lns:
       line = str( line )
       if 'sip' in line:
         if '//' in line:
            ip   = str( line.split("=")[-1] ).strip()
            ip   = str( sub( "'", "", ip ) )
            line = str( sub( ip, sip, line ) )
       fd.write( line )
     fd.close()

     rename( vnw, vip )

     ### proxy ip 2 client dir
     fd  = open( pxi, 'w' )
     fd.write( pip )
     fd.close()

     print( 'Generate Keys' )

  else:
     print( 'Usage ./kyz.py "super secret passphrase"' )

if __name__ == "__main__":
  zang()


