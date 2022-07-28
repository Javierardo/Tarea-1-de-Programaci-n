class ElementoQuimico:
    numeroAtomico = ""
    simbolo = ""
    pesoAtomico = 0
    electronesValencia = 0

carbono = ElementoQuimico()

carbono.numeroAtomico = 6
carbono.simbolo = "C"
carbono.pesoAtomico = 12
carbono.electronesValencia = 4

print("\n")
print("el objeto carbono cuenta con los siguientes atributos: ")
print("\n")
print("Numero atomico = ", carbono.numeroAtomico)
print("Simbolo = ", carbono.simbolo)
print("peso atomico = ", carbono.pesoAtomico)
print("Electrones de valencia = ", carbono.electronesValencia)
print("\n")