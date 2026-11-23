# Apresentação
print("Consulta de temperaturas por data.")


# Entrada de dados
data = input("Informe a data (aaaa-mm-dd): ")
arquivo = open("banco-temperaturas-julho.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

# Processamento
temperaturas = []
for linha in linhas:
    partes = linha.split("\t")

    data_hora = partes[0]
    temperatura = float(partes[1])
    if data_hora.startswith(data):
        temperaturas.append(temperatura)
# Saída de dados
if len(temperaturas) > 0:
    minima = min(temperaturas)
    maxima = max(temperaturas)
    amplitude = maxima - minima

    print(f"Temperatura mínima: {minima:.2f} °C")
    print(f"Temperatura máxima: {maxima:.2f} °C")
    print(f"Amplitude térmica: {amplitude:.2f} °C")
else:
    print("A data informada não está presente no arquivo.")