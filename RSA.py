
# run this program and then just change json file in directory python file and save it



from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import json
import time
import os

def generate_keys():
    # generat your keys ( publickey and privatekey)
    key = RSA.generate(2048)

    private_key = key # Take the private key that still it is on memory
    public_key = key.publickey() # Take the public key that still it is on memory

    # save privatekey and PublicKey in format .pem
    with open ("private.pem", "wb") as prv_file: # open or creat file.pem
        private_key=private_key.exportKey(format='PEM') # take key from memory
        prv_file.write(private_key)
        prv_file.close()

    with open ("public.pem", "wb") as pub_file: # open or creat file.pem
        public_key=public_key.exportKey(format='PEM') # take key from memory
        pub_file.write(public_key)
        pub_file.close()

    return

def rsa_encrypt_decrypt(message):
    print("your text: ",message)
    generate_keys()

    with open('private.pem', 'rb') as k: # read file.pem
        key = RSA.importKey(k.read())
        private_key=key.exportKey('PEM')
 

    with open('public.pem', 'rb') as k: # read file.pem
        key = RSA.importKey(k.read())
        public_key=key.exportKey('PEM')


    print("\npublicKey:\n ",public_key)
    print("\n\nprivateKey:\n ",private_key)



    message = str.encode(message)
    # encrypt text
    rsa_public_key = RSA.importKey(public_key) # send key in memory
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(message)

    print('\n\nyour encrypted_text is : \n{}'.format(encrypted_text))

    # decrypt encrypted text
    rsa_private_key = RSA.importKey(private_key)  # send key in memory
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    decrypted_text = rsa_private_key.decrypt(encrypted_text)

    print('\n\nyour decrypted_text is : {}'.format(decrypted_text.decode()))

    return


json.dump({"enter_your_text":None}, open('text.json', 'w')) # creat json file to enter yuor text
f=0
while 1:
    time.sleep(0.05) # it for control use cpu
    try:
        if os.path.isfile("text.json"): # check if file exist in directory
            text=json.load(open('text.json')) # take json file
            if text["enter_your_text"]!=None: # check if you enter a new text
                message=text["enter_your_text"]
                rsa_encrypt_decrypt(message)
                json.dump({"enter_your_text":None}, open('text.json', 'w'))
                f=0
        if f==0:
            print("enter your text")
            f=1
    except Exception as error: #control error
        # print(error)
        pass
