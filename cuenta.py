print('LOGIN')
print('')
print('Solo puedes ingresar 3 veces de forma incorrecta las contraseña')
print('Luego tu cuenta se inhabilitara')

user = input('USUARIO: ')
pss = input('CONTRASEÑA: ')

i = 1

while (i < 3) & (pss != 'INFO2020'):
    print('contraseña incorrecta')
    pss = input('ingrese nuevamente contraseña: ')
    i += 1
if pss == 'INFO2020':
    print('login correcto')
    print('Hola', user)
else:
    print('cuenta inhabilitada')