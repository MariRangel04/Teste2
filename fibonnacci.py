##fibonacci

def fibonnacci(n):
    a, b = 0, 1
    
    while b< n:
        a, b = b, a + b
    return b == n or n == 0

num = int(input('Digite um número:'))

if fibonnacci(num):
    print(f'{num} pertence a sequência')
else:
    print(f'{num} não pertence a sequência')
