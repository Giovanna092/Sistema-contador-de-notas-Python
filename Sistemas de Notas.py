''' Sistemas de notas
----------------------------------------------'''

# ENTRADA DE DADOS
notaA1 = float(input("Entre com a nota da A1[0.0 a 5.0]: "))
notaA2 = float(input("Entre com a nota da A2[0.0 a 5.0]: "))

# Analise das Faltas
presenca = int(input("Entre com a presença (%): "))
if (presenca < 75):
    print("Reprovado por Falta")
else:
    print(f"Você teve um percentual de {presenca}% nesse semestre, parabéns!")

# Calculo da primeira nota final
if((notaA1 + notaA2)>= 6.0):
    print("Aprovado sem AF")
else:
    if(notaA1 >= 1 or notaA2 >= 1):
        # ENTRE COM A NOTA DO EXAME
        notaAF = float(input("Entre com a nota AF [0.0 a 5.0]: "))

        # DECIDE A MAIOR NOTA:
        if(notaA1 >= notaA2):
            notaMaior = notaA1
        else:
            notaMaior = notaA2

        # REANALISE DA NOTA FINAL
        if((notaAF + notaMaior )>= 6.0):
            print("Aprovado com AF")
        else:
            print("Reprovado com AF")
    else:
        print("Reprovado sem AF - Não tinha pelo menos 1.0 ponto")

print(f"Notas deste semestre na avaliação A1 {notaA1} e A2 {notaA2}")
