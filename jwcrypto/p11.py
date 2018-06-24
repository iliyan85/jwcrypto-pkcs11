import pkcs11
from pkcs11 import KeyType,ObjectClass,Mechanism

def sign_data(data, lib_module, slot, token_label, pin):
	lib = pkcs11.lib(lib_module)
	slot = lib.get_slots()[slot]
	token = slot.get_token()
	if str(token) != token_label:
		raise Exception('No such token with this label')
	with token.open(user_pin=pin) as session:
		priv = session.get_key(key_type=KeyType.RSA,
				object_class=ObjectClass.PRIVATE_KEY)

		digest = session.digest(data,mechanism=Mechanism.SHA256)
		signature = priv.sign(digest)
		return signature	
