import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Fuel.csv.', usecols=['CO2EMISSIONS', 'ENGINESIZE'],)

df.columns = ['co2_emission', 'engine_size']

df = df.head(1000)

ax1 = df.plot.scatter(x=['co2_emission'], y=['engine_size'],color='red')


########################################################################################################################

gercekhata = 999999999999999999

for a in range(50, 100):
    print("trying for a =", a)

    for b in range(50, 100):
        # print("b = ",b)
        toplam_hata = 0  # RSS
        # y = ax + b -> model

        for i in range(500):  # sample size = 500
            x = df.loc[i].at['co2_emission']
            yi = df.loc[i].at['engine_size']

            toplam_hata += (yi - (a*x+b))**2  # RSS

        if toplam_hata < gercekhata:

            gercekhata = toplam_hata
            a_gercek = a
            b_gercek = b


print("Model is = ", a_gercek, "x+", b_gercek)


x = np.linspace(1, 7, 100)
y = a_gercek*x+b_gercek
plt.plot(x, y)
plt.show()

# The number range has been kept low for demonstration purposes only,
# this method is not a good method for finding an optimal model.
