peso= float(input('insira seu peso:'))
altura= float(input('insira sua altura:'))
IMC = peso / (altura ** 2)
print (f'seu imc é:{IMC:.2f}')
if IMC >=30.0:
    print('obesidade')
elif 25.0 <= IMC <=29.9:
    print('sobrepeso')
elif 18<= IMC <25.0:
    print ('peso normal')
else:
    print('abaixo do peso')