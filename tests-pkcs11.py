#!/usr/bin/env python3

import os

from jwcrypto import jwt,jwk

#with open("private.key", "rb") as pem:
#	key = jwk.JWK.from_pem(pem.read())

token = jwt.JWT(header={"alg": "RS256"},
                    claims={"info": "I'm a signed token"})
key = jwk.JWK.use_pkcs11(os.environ['PKCS11_MODULE'], 0, 'Label_test')
token.make_signed_token(key)


print(token.serialize())
