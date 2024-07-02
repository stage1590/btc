import base58
import hashlib
import ecdsa

# Endereço Bitcoin fornecido
endereco_bitcoin = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"

# Decodificar o endereço Bitcoin de Base58 para bytes
endereco_bytes = base58.b58decode(endereco_bitcoin)

# Remover o prefixo de versão (primeiro byte)
endereco_sem_prefixo = endereco_bytes[1:]

# Calcular o checksum
checksum_calculado = hashlib.sha256(hashlib.sha256(endereco_sem_prefixo).digest()).digest()[:4]

# Verificar se o checksum no endereço corresponde ao checksum calculado
if endereco_bytes[-4:] != checksum_calculado:
    raise ValueError("Endereço Bitcoin inválido")

# Extrair o hash RIPEMD-160 do endereço
ripemd160 = endereco_sem_prefixo[:-4]

# Construir a chave pública a partir do hash RIPEMD-160
chave_publica = ripemd160.hex()

print("Chave pública (HEX):", chave_publica)
