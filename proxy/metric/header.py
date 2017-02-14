from re import sub


def heads( raw, opt, proc=None ):

  def all():
     h = []
     for e in str( raw ).split('\n'):
       e = str( e )
       f = ''

       if ": " in e:
           f = str( e.split(': ')[0] )
           e = str( e.split(': ')[-1] )

       if proc:
         if proc in e:
           f = str( '%s ' % proc )
           e = str( sub( f, '', e ) )
           e = str( e.split(' ')[0] )
           f = str( 'METHOD:%s' % proc )

       if '\r' in e:
         e = str( sub( '\\r', '', e ) )

       g = [ f, e ]
       h.append( g )

     return h

  def item():
     for e in str( raw ).split('\n'):
       e = str( e )
       if '-' in e:
          if '_' in e:
            itm = str( e.split('=')[0] )
            id  = str( itm.split('_')[-1] )
            if len( id ) == 25:
               if id[0].isdigit():
                 return itm

  t = eval( opt )
  return t()


def headerz( raw, opt, proc=None ):
  raw   = str( raw )
  opt  = str( opt )
  hary  = heads( raw, opt, proc )
  return hary
