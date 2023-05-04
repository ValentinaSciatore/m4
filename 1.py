import random

if __name__ == '__main__':
    x, y = 0, 0
    for i in range(0, 100):
        # se il numero generato è pari
        if random.randint(0, 10) % 2 == 0:
            # se il numero sarà positivo andrà ad est se negativo ad ovest
            x = random.randint(-10, 10)
        else:
            # se il numero sarà positivo andrà a nord  se negativo a sud
            y = random.randint(-10, 10)
    print("x ", x, " y ", y)