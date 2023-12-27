# try, except, else e finally
try:# try não pode ser usado sozinho
   print('Pão')
#    8/0
except ZeroDivisionError:# pode haver quantos except vc quiser
    print('Dividiu Zero')
else:
    print('DA pra usar isso aqui tbm `-`')
finally:# finally sempre e executado havendo erro ou não
   print('Pão1')