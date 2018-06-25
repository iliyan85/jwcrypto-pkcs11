import pkcs11
from pkcs11 import ObjectClass, Attribute, Mechanism

def sign_p11(sigin, alg, lib_path, slot, key_label, pin):
	lib = pkcs11.lib(lib_path)
	slot = lib.get_slots()[slot]
	token = slot.get_token()
	with token.open(user_pin=pin) as session:
		for priv in session.get_objects({Attribute.CLASS: ObjectClass.PRIVATE_KEY, Attribute.LABEL: key_label}):
			if alg == 'RS256':
				MECHANISM = Mechanism.SHA256_RSA_PKCS
			elif alg == 'RS384':
				MECHANISM = Mechanism.SHA384_RSA_PKCS
			elif alg == 'RS512':
				MECHANISM = Mechanism.SHA512_RSA_PKCS
			else:
				raise Exception('Unsupported algorithm')
			signature = priv.sign(sigin, mechanism=MECHANISM)		
	return signature