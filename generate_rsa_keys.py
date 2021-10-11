from Crypto.PublicKey import RSA

private_key = RSA.generate(2048)
public_key = private_key.public_key()
f = open('privkey.pem','wb')
f.write(private_key.export_key('PEM'))
f.close()
f = open('pubkey.pem','wb')
f.write(public_key.export_key('PEM'))
f.close()