A three part mail proxy using pre shared eliptic curve cryptography.  The server sits on a web facing linux node linked to bounce through gmail via postix server.  The client encrypts with the public key on any python capable machine.  The proxy is a post repeater which sits on google appengine.  The effect is you get encrypted email without paying for a SSL cert.  You can bounce as easily as you could make this a fully functional email server using googles ssl certs.
