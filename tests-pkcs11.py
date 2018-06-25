#!/usr/bin/env python3

import os

from jwcrypto import jwt,jwk

token = jwt.JWT(header={"alg": "RS512"},
                    claims={"info": "I'm a signed token"})

key = jwk.JWK.use_pkcs11(lib_path=os.environ['PKCS11_MODULE'],
					slot=0,
					key_label='aa08ce18-e927-4d53-82dd-8aa9200b7e2e')

#with open("key.priv", "rb") as pem:
#	key = jwk.JWK.from_pem(pem.read())

token.make_signed_token(key)


print(token.serialize())
