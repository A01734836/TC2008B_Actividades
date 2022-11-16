from cleaner_model import CleanerModel

M = int(input("Tamano de la habitacion(Y): "))
N = int(input("Tamano de la habitacion(X): "))
numAgentes = int(input("Numero de agentes: "))
porSucio = int(input("Porcentaje de celdas sucias: "))
tMax = int(input("Pasos maximos: "))
numCeldas = M*N
numSucio = int(numCeldas*porSucio/100)
modelo = CleanerModel(numAgentes,M,N,numCeldas-numSucio)
for c in range(tMax):
    modelo.step()
    if sum(modelo.room.matrix)==numCeldas: break
cuarto = modelo.room.matrix
print("Porcentaje de celdas limpias:",sum(cuarto)*100/numCeldas)
print("Pasos necesarios:",c+1)