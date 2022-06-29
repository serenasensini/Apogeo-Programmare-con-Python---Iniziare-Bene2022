import pandas as pd

# leggi da file .csv
wine_measurements = pd.read_csv("winequality-red.csv")
# wine_measurements = pd.read_csv("winequality-red.csv", header=None)

# stampa le prime e ultime 5 righe
print(wine_measurements.head())
# print(wine_measurements.tail())

# stampa le prime e ultime 10 righe
# print(wine_measurements.head(10))
# print(wine_measurements.tail(10))

# print(wine_measurements.shape)

# print(wine_measurements.info())

# print(wine_measurements.describe())

# print(wine_measurements.count())

# fixed_ac = wine_measurements["fixed_acidity"]
# print(fixed_ac)

# fixed_ac = wine_measurements.fixed_acidity
# print(fixed_ac)

# seleziona le due colonne specifiche
# indexes = ["citric_acid", "alcohol"]
# two_columns = wine_measurements[indexes]

# print(two_columns)

# rows = wine_measurements.loc[1]
#
# print(rows)

# stampa la riga dalla 1 alla 4 compresa
# rows = wine_measurements[1:4]
# print(rows)

# stampa le righe 1, 3 e 5
# rows_list = [1, 3, 5]
# rows = wine_measurements.loc[rows_list]

# print(rows)

rows_list = [1, 3, 5]
columns_list = ["alcohol", "quality"]
rows = wine_measurements.loc[rows_list, columns_list]

# print(rows)

# check intervalli specifici
intervalli = [[2,4], [6,8]]
#
# for intervallo in intervalli:
#     print(intervallo)
#     df = wine_measurements.loc[intervallo[0]:intervallo[1]]
#     print(df)

# stringa = "testo di prova"
#
# for intervallo in intervalli:
#     print(stringa[intervallo[0]:intervallo[1]])

# wine_measurements.loc[:, ["pH"]].plot()

import matplotlib.pyplot as plt


# plt.bar(wine_measurements.alcohol, wine_measurements.quality)
# plt.bar(wine_measurements['alcohol'], wine_measurements['quality'])

# plt.savefig("bar.png")

plt.hist(wine_measurements.alcohol)

plt.savefig("histogram.png")