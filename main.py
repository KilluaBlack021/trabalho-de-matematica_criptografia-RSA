from random import randrange


def mdc(n1, n2):
    while n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1


def gerador_chave_publica(totiente):
    while True:
        e = randrange(2, totiente)
        if mdc(totiente, e) == 1:
            return e


def gerador_chave_privada(totiente, e):
    d = 0
    while d*e % totiente != 1:
        d += 1
    return d


def cifrar(msg, e, n):
    msg_cifrada = ''
    for letra in msg:
        k = ord(letra) ** e % n
        msg_cifrada += chr(k)
    return msg_cifrada


def decifrar(msg, n, d):
    msg_decifrada = ''
    for letra in msg:
        k = ord(letra) ** d % n
        msg_decifrada += chr(k)
    return msg_decifrada


# main
msg = '''
Era uma vez os três porquinhos, 
o Bob, o Valdisney e o Pedrinho.
Bob é viciado no cigarrinho do capeta
sua casa é de palha e passa o dia na... trobeta!
Valdisney é favelado, tem um barraco de madeira 
graças ao bolsa familia não trampou a vida inteira.
O Pedrinho é diferente, designin de interiores,
tem uma casa de tijolos e limpa a ***** com flores'''

p = 17 # primo 1
q = 19 # primo 2
n = p * q
totiente = (p-1) * (q-1) # inverso multiplicativo de N

e = gerador_chave_publica(totiente)
d = gerador_chave_privada(totiente, e)


#print(f'chave publica: {e}, {n}\n chave privada: {d, n}')

msg = cifrar(msg, e, n)
print(f'msg cifrada: {msg}\n')
msg = decifrar(msg, n, d)
print(f'msg decifrada: {msg}\n')
