from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

clave_secreta = b'tu_clave_secreta_aqui'
salt = b'tu_salt_aqui'  # Un valor aleatorio utilizado como salt

# Generar una clave segura utilizando PBKDF2
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,  # Tamaño de clave de 256 bits (32 bytes)
    salt=salt,
    iterations=100000,  # Número de iteraciones para aumentar la resistencia a ataques de fuerza bruta
    backend=default_backend()
)
clave = kdf.derive(clave_secreta)

def encriptar(texto):
    """
    ESte metodo sirve para encriptar cadenas de texto
    @type texto: El campo request recibe el texto que se desea encriptar
    @rtype: DEvuelve la cadena de texto encriptada
    """
    # Generar una clave de cifrado a partir de la clave segura
    backend = default_backend()
    cipher = Cipher(algorithms.AES(clave), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()

    # Aplicar el padding al texto
    padder = padding.PKCS7(128).padder()
    texto_paddado = padder.update(texto.encode()) + padder.finalize()

    # Encriptar el texto
    texto_encriptado = encryptor.update(texto_paddado) + encryptor.finalize()

    return texto_encriptado

def desencriptar(texto_encriptado):
    """
    ESte metodo sirve para desencriptar cadenas de texto
    @type texto: El campo request recibe el texto que se desea desencriptar
    @rtype: DEvuelve la cadena de texto desencriptado
    """
    # Generar una clave de cifrado a partir de la clave segura
    backend = default_backend()
    cipher = Cipher(algorithms.AES(clave), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()

    # Desencriptar el texto
    texto_paddado = decryptor.update(texto_encriptado) + decryptor.finalize()

    # Quitar el padding del texto desencriptado
    unpadder = padding.PKCS7(128).unpadder()
    texto = unpadder.update(texto_paddado) + unpadder.finalize()

    return texto.decode()

# # Ejemplo de uso
# texto_original = "1003150602"
#
# # Encriptar el texto
# texto_encriptado = encriptar(texto_original)
# print(texto_encriptado)
#
# # Desencriptar el texto
# texto_desencriptado = desencriptar(texto_encriptado)
# print(texto_desencriptado)
