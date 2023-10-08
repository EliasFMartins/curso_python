primeiro_valor = input('digite um valor ')
segundo_valor = input('digite outro valor ')

if(primeiro_valor>segundo_valor):
    print(f'primeiro valor {primeiro_valor=} e maior que segundo valor{segundo_valor=}')
elif(segundo_valor> primeiro_valor):
    print(f'segundo valor {segundo_valor=} e maior que primeiro valor{primeiro_valor=}')
elif(primeiro_valor==segundo_valor):
    print(f'os valores {primeiro_valor=} e segundo valor{segundo_valor=} são inguais')
  #n precisa de parentesses pra fazer condições e e necessario usar : 