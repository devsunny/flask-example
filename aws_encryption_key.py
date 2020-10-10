#sudo pip install awscli --ignore-installed six
#aws config - set access key id  and Secret access key
import boto3

client=boto3.client('kms')
key_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

plaintext = "This is the text"

response = client.encrypt(
    KeyId=key_id,
    Plaintext=plaintext.encode()
)

ciphertext = response['CiphertextBlob']

print(ciphertext )

response = client.decrypt(
    CiphertextBlob=ciphertext,
    KeyId=key_id
)

plaintext2 = response['Plaintext']

print(plaintext2)
