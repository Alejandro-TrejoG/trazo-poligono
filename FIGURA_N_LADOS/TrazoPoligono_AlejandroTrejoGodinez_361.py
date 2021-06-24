import math
import matplotlib.pylab as plt


def metodo_DDA(arregloX, arregloY, lados):
    j = 0
    while j < lados:
        if j == (lados - 1):
            x1 = arregloX[j]
            y1 = arregloY[j]
            x2 = arregloX[0]
            y2 = arregloY[0]
        else:
            x1 = arregloX[j]
            y1 = arregloY[j]
            x2 = arregloX[j + 1]
            y2 = arregloY[j + 1]
        dx = x2 - x1
        dy = y2 - y1
        if abs(dx) > abs(dy):
            steps = abs(dx)
            print("steps = dx = ", dx)
        else:
            steps = abs(dy)
            print("steps = dy = ", dy)

        xinc = float(dx / steps)
        yinc = float(dy / steps)

        i = 0
        for i in range(steps + 1):
            plt.plot(round(x1), round(y1), "bs")
            x1 += xinc
            y1 += yinc

            print("x => ", round(x1))
            print("y => ", round(y1))
        j += 1
    plt.title("FIGURA N LADOS EN DDA")
    plt.show()


def metodo_Bresenham(arregloX, arregloY, lados):
    j = 0
    while j < lados:
        if j == (lados - 1):
            x1 = arregloX[j]
            y1 = arregloY[j]
            x2 = arregloX[0]
            y2 = arregloY[0]
        else:
            x1 = arregloX[j]
            y1 = arregloY[j]
            x2 = arregloX[j + 1]
            y2 = arregloY[j + 1]
        dx = abs(x2 - x1)
        print("dx= ", dx)
        dy = abs(y2 - y1)
        print("dy= ", dy)
        p = 2 * dy - dx
        print("p ", p)
        if x1 > x2:
            x_1 = x2
            y_1 = y2
            x_2 = x1
            y_2 = y1
        else:
            x_1 = x1
            y_1 = y1
            x_2 = x2
            y_2 = y2
        if dx == 0:
            if y_1 < y_2:
                aux = y_1
                y_1 = y_2
                y_2 = aux
            while y_1 <= y_2:
                plt.plot(x_1, y_1, "bs")
                if p < 0:
                    p = p + 2 * dy
                else:
                    p = p + 2 * dy - 2 * dx
                    y_1 += 1
        else:
            while x_1 <= x_2:
                plt.plot(x_1, y_1, "bs")
                x_1 += 1
                if p < 0:
                    p = p + 2 * dy
                else:
                    p = p + 2 * dy - 2 * dx
                    y_1 += 1
        j += 1
    plt.title("FIGURA N LADOS EN BRESENHAM")
    plt.show()


lados = int(input("Ingresa el numero de lados: "))
radio = int(
    input(
        "Ingresa el tamaño del centro a los vertices (valores de 10 en 10 para mayor apreciación): "
    )
)
metodo = int(input("Ingresa el metodo a usar \n1.DDA \n2.Bresenham \n=>"))
angulo = 360 / lados
anguloXlado = 0
i = 0
arregloX = []
arregloY = []
while i < lados:
    x = math.radians(anguloXlado)
    y = math.radians(anguloXlado)
    x = radio * (math.cos(x))
    y = radio * (math.sin(y))
    x += radio
    y += radio
    arregloX.append(round(x))
    arregloY.append(round(y))
    anguloXlado += angulo
    # print("x =", x, ",y =", y)
    i += 1

print(arregloX)
print(arregloY)
if metodo == 1:
    metodo_DDA(arregloX, arregloY, lados)
else:
    metodo_Bresenham(arregloX, arregloY, lados)