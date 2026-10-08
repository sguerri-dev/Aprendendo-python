ano = int(input("Para validação informe seu ano de nascimento."))
if ano >2010:
      print("Voce ainda nao pode votar.")
elif ano >1956 and ano <2009:
      print("O seu voto é obrigatório")
else: 
      print("seu voto é opcional")
