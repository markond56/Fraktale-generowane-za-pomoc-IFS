# instalacja: pip install matplotlib
import matplotlib.pyplot as plt
import random as rnd

x = [0]  # lista x z wprowadzonym x początkowym x_0 = 0
y = [0]  # lista y z wprowadzonym y początkowym y_0 = 0

for i in range(1, 100000):
    random_number = rnd.random()  # liczba rzeczywista z przedziału [0;1)
    # jeśli wylosowana liczba zawiera się w [0;0.1), to wybierany jest pierwszy układ równań
    if random_number < 0.1:
        x.append(0.14 * x[i - 1] + 0.01 * y[i - 1] - 1.31)
        y.append(0.0 * x[i - 1] + 0.51 * y[i - 1] + 0.1)
    elif random_number < 0.45:
        x.append(0.43 * x[i - 1] + 0.52 * y[i - 1] + 1.49)
        y.append(-0.45 * x[i - 1] + 0.5 * y[i - 1] - 0.75)
    elif random_number < 0.8:
        x.append(0.45 * x[i - 1] - 0.49 * y[i - 1] - 1.62)
        y.append(0.47 * x[i - 1] + 0.47 * y[i - 1] - 0.74)
    else:
        x.append(0.49 * x[i - 1] + 0.0 * y[i - 1] + 0.02)
        y.append(0.0 * x[i - 1] + 0.51 * y[i - 1] + 1.62)

plt.plot(x, y, ".", markersize=1)  # rozmiar punktu wielkości 1
plt.show()  # wyświetlenie wykresu
