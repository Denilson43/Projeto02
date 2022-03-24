print ('Em que ano vc nasceu?')
nascimento = input ()
nascimento = int (nascimento)
print ('Para qual ano você quer saber sua idade?')
ano = input ()
ano = int (ano)
idade = ano - nascimento
print('No ano' , ano , 'você terá' , idade , 'anos!')