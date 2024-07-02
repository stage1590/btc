import hashlib
import base58

def decode_base58(address):
    return base58.b58decode(address)

def convert_to_hex(data):
    return data.hex()

def ripemd160(data):
    h = hashlib.new('ripemd160')
    h.update(data)
    return h.digest()

def decode_bitcoin_address(address):
    # Passo 1: Decodificar endereço Base58 para obter o hash RIPEMD-160
    decoded = decode_base58(address)
    hash160 = decoded[1:-4]  # Remove o prefixo de versão e o checksum

    # Passo 2: Converte para formato hexadecimal
    hash160_hex = convert_to_hex(hash160)

    return hash160_hex

def main():
    bitcoin_address = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'
    hash160_hex = decode_bitcoin_address(bitcoin_address)

    print("Hash RIPEMD-160 em hexadecimal:", hash160_hex)

if __name__ == "__main__":
    main()
