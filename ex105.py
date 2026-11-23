# Apresentação
print("Análise das temperaturas do mês de julho.")

# Entrada de dados
arquivo = open("banco-temperaturas-julho.txt", "r")

# Processamento
linhas = arquivo.readlines()
arquivo.close()
temperaturas = []
primeiro_minimo = ""

for linha in linhas:
    partes = linha.split("\t")
    data_hora = partes[0]
    temperatura = float(partes[1])
    temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)
minima = min(temperaturas)
maxima = max(temperaturas)

for linha in linhas:
    partes = linha.split("\t")
    if float(partes[1]) == minima:
        primeiro_minimo = partes[0]
        break

#Saída de dados
print(f"Total de linhas: {len(linhas)}")
print(f"Média das temperaturas: {media:.2f} °C")
print(f"Temperatura mínima: {minima:.2f} °C")
print(f"Temperatura máxima: {maxima:.2f} °C")
print(f"Primeiro registro da temperatura mínima: {primeiro_minimo}")
