def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string.replace(" ", ""))

def xor_decrypt(encrypted_data, key):
    decrypted_data = bytearray()
    for i, byte in enumerate(encrypted_data):
        decrypted_data.append(byte ^ key[i % len(key)])
    return bytes(decrypted_data)




key = b'\xE6\x34\xA2\x6A\xD4\x6F\x1B\xE0\xB8\xA0\x4E\x00\xBE\x72\x25\x19'  # Example 16-byte key 
encrypted_message = b'\x76\x80\x92\x3E\xF4\xF4\x35\x0F\x90\xFA\x11\x12\xCE\xB9\x7C\xFB'
# Decrypt the message
decrypted_message = xor_decrypt(encrypted_message, key)

# Print the raw bytes of the decrypted message
print("Decrypted bytes:", decrypted_message)

# Optionally try to guess and print as a string with 'latin1' which covers all byte values (0-255)
try:
    print("Decrypted message:", decrypted_message.decode('latin1'))
except UnicodeDecodeError as e:
    print("Cannot decode decrypted data as text:", str(e))
