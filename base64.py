# Tabela Base64 padrão global (64 caracteres + padding)
TABELA_BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def codificar(texto):
    """Codifica uma string para Base64 sem usar bibliotecas externas."""
    
    # 1. Converter cada caractere do texto em seu valor ASCII (ord(c))
    # Depois transformar esse valor em binário (8 bits) com f-string formatando '{:08b}'
    binario = ''.join(f'{ord(c):08b}' for c in texto)
    # Exemplo: "Ma" -> 'M' (77) -> '01001101', 'a' (97) -> '01100001'
    # Resultado: '0100110101100001'
    
    # 2. Ajustar: se o total de bits não for múltiplo de 6, adiciona '0's no final
    binario += '0' * ((6 - len(binario) % 6) % 6)
    # Porque Base64 agrupa de 6 em 6 bits!

    # 3. Dividir os bits completos em blocos de 6 bits
    blocos = [binario[i:i+6] for i in range(0, len(binario), 6)]
    # Exemplo: '010011010110000100' → ['010011', '010110', '000100']

    # 4. Converter cada bloco de 6 bits em número decimal (0-63)
    # E usar esse número como índice para buscar na TABELA_BASE64
    base64 = ''.join(TABELA_BASE64[int(b, 2)] for b in blocos)
    # Exemplo: '010011' → 19 → 'T', '010110' → 22 → 'W', etc.

    # 5. Adicionar padding '=' para que o tamanho final seja múltiplo de 4
    padding = '=' * ((4 - len(base64) % 4) % 4)
    
    return base64 + padding

def decodificar(base64_texto):
    """Decodifica uma string Base64 sem usar bibliotecas externas."""
    
    # 1. Remover o padding '=' (se houver)
    base64_texto = base64_texto.rstrip('=')

    # 2. Converter cada caractere Base64 em seu índice (posição na tabela)
    # Depois transformar cada índice em binário (6 bits)
    binario = ''.join(f'{TABELA_BASE64.index(c):06b}' for c in base64_texto)
    # Exemplo: 'T' → 19 → '010011', 'W' → 22 → '010110'

    # 3. Remover bits extras que não formam um byte completo (8 bits)
    binario = binario[:len(binario) - (len(binario) % 8)]

    # 4. Dividir os bits em blocos de 8 bits (1 byte)
    caracteres = [binario[i:i+8] for i in range(0, len(binario), 8)]

    # 5. Converter cada bloco de 8 bits para um caractere ASCII
    texto = ''.join(chr(int(b, 2)) for b in caracteres)
    # Exemplo: '01001101' → 77 → 'M'

    return texto

# Teste simples
if __name__ == "__main__":
    entrada = input("Digite uma palavra para codificar: ")
    codificada = codificar(entrada)
    print(f"Codificada: {codificada}")
    print(f"Decodificada: {decodificar(codificada)}")
