import os, base64, qrcode
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
print("###--------------------------------------------------------###")
text = input("Enter text: ")

# Generate key + IV
key = os.urandom(32)              # 256‑bit
iv = os.urandom(12)               # 96‑bit

# Encrypt AES‑GCM
aes = AESGCM(key)
ct = aes.encrypt(iv, text.encode(), None)

# Make Base64 payloads
payload_b64 = base64.urlsafe_b64encode(iv + ct).decode()
key_b64 = base64.urlsafe_b64encode(key).decode()

# Make QR
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M)
qr.add_data(payload_b64)
qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white").save("qr_Secret.png")
print("###---------------------QR file created--------------------###")
print("QR file created: qr_Secret.png")
print("###-------------------------Key----------------------------###")
print("Key (Base64):", key_b64)
print("###-----------------------Payload--------------------------###")
print("Payload (Base64):", payload_b64)
print("###--------------------------------------------------------###")
