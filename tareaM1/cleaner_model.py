import mesa
import random

class Matrix:
    def __init__(self,M,N,val):
        self.matrix = [val]*(M*N)
        self.sizeY = M
        self.sizeX = N

    def changeValue(self,M,N,val):
        if M<self.sizeY and N<self.sizeX:
            self.matrix[M*self.sizeX+N] = val

    def getValue(self,M,N):
        if M < self.sizeY and N < self.sizeX:
            return self.matrix[M*self.sizeX+N]

    def printMatrix(self):
        for i in range(self.sizeY):
            print(*self.matrix[i*self.sizeX:(i+1)*self.sizeX])

class CleanerAgent(mesa.Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.position = [0,0]
    def step(self):
        if self.model.room.getValue(*self.position)==0:
            self.model.room.changeValue(*self.position,1)
        else:
            movY = random.randint(-1,1)
            newPosY = self.position[0]+movY
            movX = random.randint(-1, 1)
            newPosX = self.position[1] + movX
            while (movY==0 and movX==0) or (newPosY<0 or newPosY>=self.model.room.sizeY) or (newPosX<0 and newPosX>=self.model.room.sizeX):
                movY = random.randint(-1, 1)
                newPosY = self.position[0] + movY
                movX = random.randint(-1, 1)
                newPosX = self.position[1] + movX
            self.position = [newPosY,newPosX]




class CleanerModel(mesa.Model):

    def __init__(self, numAgents, M, N, numLimpio):
        self.num_agents = numAgents
        self.room = Matrix(M,N,0)
        for i in range(numLimpio):
            posY = random.randint(0,M-1)
            posX = random.randint(0,N-1)
            while self.room.getValue(posY,posX)==1:
                posY = random.randint(0, M - 1)
                posX = random.randint(0, N - 1)
            self.room.changeValue(posY,posX,1)
        self.schedule = mesa.time.BaseScheduler(self)
        for i in range(self.num_agents):
            a = CleanerAgent(i, self)
            self.schedule.add(a)

    def step(self):
        self.schedule.step()