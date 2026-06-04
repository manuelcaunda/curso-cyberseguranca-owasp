#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplos Práticos de Criptografia
Parte 0: Fundamentos de Segurança
"""

import hashlib
import secrets
import bcrypt
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

print("="*60)
print("EXEMPLOS DE CRIPTOGRAFIA EM PYTHON")
print("="*60)

# ==========================================
# 1. CRIPTOGRAFIA SIMÉTRICA (Fernet)
# ==========================================
print("\n[1] CRIPTOGRAFIA SIMÉTRICA (Fernet)")
print("-" * 60)

chave = Fernet.generate_key()
print(f"Chave gerada: {chave.decode()}")

cipher = Fernet(chave)
dados_originais = "Informação muito sensível"
print(f"Dados originais: {dados_originais}")

dados_encriptados = cipher.encrypt(dados_originais.encode())
print(f"Dados encriptados: {dados_encriptados}")

dados_desencriptados = cipher.decrypt(dados_encriptados).decode()
print(f"Dados desencriptados: {dados_desencriptados}")
print(f"✅ Match: {dados_originais == dados_desencriptados}")

# ==========================================
# 2. HASH BCRYPT (Para Passwords)
# ==========================================
print("\n\n[2] HASH BCRYPT (Para Passwords)")
print("-" * 60)

password = b"minha_senha_super_forte_123!"
hash_password = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))
print(f"Password original: {password.decode()}")
print(f"Hash bcrypt: {hash_password.decode()}")

if bcrypt.checkpw(password, hash_password):
    print(f"\n✅ Password correto!")

senha_errada = b"password_errado"
if not bcrypt.checkpw(senha_errada, hash_password):
    print(f"❌ Password errado rejeitado!")

# ==========================================
# 3. SHA-256 (Hash simples)
# ==========================================
print("\n\n[3] SHA-256 (Hash Simples)")
print("-" * 60)

dados = "Informação a ser hashcada"
hash_sha256 = hashlib.sha256(dados.encode()).hexdigest()
print(f"Dados: {dados}")
print(f"SHA-256: {hash_sha256}")

hash_sha512 = hashlib.sha512(dados.encode()).hexdigest()
print(f"SHA-512: {hash_sha512}")

dados_modificado = "Informação a ser hasHcada"
hash_modificado = hashlib.sha256(dados_modificado.encode()).hexdigest()

print(f"\nDados modificado (h -> H): {dados_modificado}")
print(f"Hash novo: {hash_modificado}")
print(f"Hashes são iguais? {hash_sha256 == hash_modificado}")

# ==========================================
# 4. CRIPTOGRAFIA ASSIMÉTRICA (RSA)
# ==========================================
print("\n\n[4] CRIPTOGRAFIA ASSIMÉTRICA (RSA)")
print("-" * 60)

print("Gerando chaves RSA-2048... (pode levar alguns segundos)")
chave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
chave_publica = chave_privada.public_key()
print("✅ Chaves geradas!")

dados = b"Informacao super secreta"

dados_encriptados = chave_publica.encrypt(
    dados,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"\nDados originais: {dados}")
print(f"Dados encriptados: {dados_encriptados[:50]}... (truncado)")

dados_desencriptados = chave_privada.decrypt(
    dados_encriptados,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"Dados desencriptados: {dados_desencriptados}")
print(f"\n✅ Match: {dados == dados_desencriptados}")

# ==========================================
# 5. ASSINATURA DIGITAL (RSA)
# ==========================================
print("\n\n[5] ASSINATURA DIGITAL (RSA)")
print("-" * 60)

chave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
chave_publica = chave_privada.public_key()

documento = b"Contrato entre Pedro e Maria no valor de 5000 EUR"

assinatura = chave_privada.sign(
    documento,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print(f"Documento: {documento.decode()}")
print(f"Assinatura: {assinatura.hex()[:80]}... (truncada)")

try:
    chave_publica.verify(
        assinatura,
        documento,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("\n✅ Assinatura VÁLIDA! Documento não foi modificado.")
except:
    print("\n❌ Assinatura INVÁLIDA! Documento foi modificado.")

print("\n--- Tentando modificar documento ---")
documento_falso = b"Contrato entre Pedro e Maria no valor de 50000 EUR"

try:
    chave_publica.verify(
        assinatura,
        documento_falso,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("✅ Assinatura VÁLIDA!")
except:
    print(f"❌ FRAUDE DETECTADA! Documento foi modificado.")
    print(f"Documento original: {documento.decode()}")
    print(f"Documento modificado: {documento_falso.decode()}")

# ==========================================
# 6. PBKDF2 (Para Passwords)
# ==========================================
print("\n\n[6] PBKDF2 (Para Passwords)")
print("-" * 60)

password = "minha_senha_forte"
salt = secrets.token_hex(16)

password_hash = hashlib.pbkdf2_hmac(
    'sha256',
    password.encode(),
    salt.encode(),
    100000
)

print(f"Password: {password}")
print(f"Salt: {salt}")
print(f"Hash: {password_hash.hex()}")

password_hash_check = hashlib.pbkdf2_hmac(
    'sha256',
    password.encode(),
    salt.encode(),
    100000
)

print(f"\n✅ Hashes iguais: {password_hash == password_hash_check}")

# ==========================================
# 7. SALVAR CHAVES RSA EM ARQUIVO
# ==========================================
print("\n\n[7] SALVAR CHAVES RSA EM ARQUIVO")
print("-" * 60)

chave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
chave_publica = chave_privada.public_key()

chave_privada_pem = chave_privada.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

chave_publica_pem = chave_publica.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print("Chave Privada PEM (primeiras linhas):")
print(chave_privada_pem.decode().split('\n')[:3])
print("\nChave Pública PEM (primeiras linhas):")
print(chave_publica_pem.decode().split('\n')[:3])

print("\n" + "="*60)
print("FIM DOS EXEMPLOS")
print("="*60)
