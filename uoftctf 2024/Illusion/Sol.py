from Crypto.Cipher import AES

import hashlib
import base64
import re

KEY = hashlib.sha256(b'Tr3v0rC2R0x@nd1s@w350m3#TrevorForget').digest()

def decrypt(payload, count):
    for _ in range(count):
        payload = base64.b64decode(payload)

    enc = payload[16:]
    iv = payload[:16]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    
    return cipher.decrypt(enc), iv, enc

raw = open('traffic.pcapng', 'rb').read()
p1 = re.compile(rb'guid=([\w+/=]+)', re.S)
p2 = re.compile(rb'oldcss=([\w+/=]+)', re.S)

# matches_p1 = p1.findall(raw)
# for m in matches_p1:
#     print(m)

# matches_p2 = p2.findall(raw)
# for m in matches_p2:
#     print(m)

# for m in p1.findall(raw):
#     print(decrypt(m, 2))

# for m in p2.findall(raw):
#     print(decrypt(m, 1))


matches_p1 = p1.findall(raw)
print("Matches for p1:")
for m in matches_p1:
    decrypted_data, iv, enc = decrypt(m, 2)
    print(f"Decrypted Data: {decrypted_data}, IV: {iv}, Encrypted Data: {enc}")

matches_p2 = p2.findall(raw)
print("Matches for p2:")
for m in matches_p2:
    decrypted_data, iv, enc = decrypt(m, 1)
    print(f"Decrypted Data: {decrypted_data}, IV: {iv}, Encrypted Data: {enc}")


# C2 : 
    
# python3 trevorC2Decrypt.py File_pcap

# trevorC2Decrypt.py : 
    
# from scapy.all import *
# import argparse
# from Crypto.Cipher import AES
# import base64
# import hashlib
# from urllib.parse import unquote

# parser = argparse.ArgumentParser(description='Decrypt TrevorC2 traffic from a pcap')
# parser.add_argument('pcap', metavar='pcap', type=str, help='PCAP file')
# parser.add_argument('-k', metavar='key', type=str, help='key (default is "Tr3v0rC2R0x@nd1s@w350m3#TrevorForget")', default="Tr3v0rC2R0x@nd1s@w350m3#TrevorForget")
# args = parser.parse_args()

# pcap = rdpcap(args.pcap)
# key = args.k

# @staticmethod
# def _unpad(s):
#     return s[:-ord(s[len(s)-1:])]

# def str_to_bytes(data):
#         u_type = type(b''.decode('utf8'))
#         if isinstance(data, u_type):
#             return data.encode('utf8')
#         return data

# def decrypt(key, enc):
#         key = hashlib.sha256(str_to_bytes(key)).digest()
#         enc = base64.b64decode(enc)
#         iv = enc[:AES.block_size]
#         cipher = AES.new(key, AES.MODE_CBC, iv)
#         return _unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

# for pkt in pcap:
#     #get the commands being sent to the compromised host. Will be in html format </script><!-- oldcss=... --></body></html>
#     try:
#         if pkt[TCP].sport == 80:
#             if b"<!-- oldcss=" in pkt[Raw].load:
#                 #grab the command
#                 command = pkt[Raw].load.split(b"<!-- oldcss=")[1].split(b" --></body>")[0]
#                 #decrypt the command
#                 try:
#                     decrypted = decrypt(key, command)
#                     #print the decrypted command
#                     print("Decrypted command: " + str(decrypted))
#                 except Exception as e:
#                     print(e)
#                     pass
#     except:
#         pass

#     #go through and look for HTTP(s) GET requests containing /images?guid=
#     try:
#         if pkt[TCP].dport == 80:
#             if b"GET /images?guid=" in pkt[Raw].load:
#                 #grab the guid
#                 guid = pkt[Raw].load.split(b"guid=")[1].split(b" ")[0]
#                 #url decode the guid
#                 guid = unquote(guid)
#                 try:
#                     guid = base64.b64decode(guid)
#                     #decrypt the guid
#                     decrypted = decrypt(key, guid)
#                     #print the decrypted guid
#                     print("Decrypted response: " + str(decrypted))
#                 except Exception as e:
#                     print(e)
#                     pass
#     except:
#         pass

