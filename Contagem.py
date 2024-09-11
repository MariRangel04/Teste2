## Letra maiúscula

palavra = input('Digite uma palavra:')

qtd_a = palavra.count('a')
qtd_A = palavra.count('A')

total = qtd_a + qtd_A

if total > 0:
    print(f'A letra "a" aparece {qtd_a + qtd_A} vezes')
else: 
    print('A letra "a" não aparece na palavra')
