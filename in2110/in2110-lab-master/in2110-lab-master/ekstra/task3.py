# -*- coding: utf-8 -*-
import pandas as pd
import sklearn
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt


df = pd.read_csv("insekter_fra_Ecuador.csv", index_col=0)
train_df, test_df = sklearn.model_selection.train_test_split(df, shuffle=False)

X = train_df.loc[:, 'Number of tokens':'Number of links']
y = train_df.loc[:, 'Ecuadors insekter']
X_test = test_df.loc[:, 'Number of tokens':'Number of links']
y_test = test_df.loc[:, 'Ecuadors insekter']


logReg = LogisticRegression(solver="lbfgs", multi_class='ovr')

fitted = logReg.fit(X, y)
logReg.coef_
logReg.intercept_

score = logReg.score(X_test, y_test)
print(score)

sushi = X.loc[y == True]
taco = X.loc[y == False]
plt.scatter(sushi.loc[:, 'Number of tokens'], sushi.loc[:, 'Number of links'], color='g')
plt.scatter(taco.loc[:, 'Number of tokens'], taco.loc[:, 'Number of links'], color='r')

# getting the x co-ordinates of the decision boundary
plot_x = np.array([min(X.loc[:, 'Number of tokens']) - 2, max(X.loc[:, 'Number of tokens']) + 2])
# getting corresponding y co-ordinates of the decision boundary
coef = logReg.coef_[0]
intr = logReg.intercept_
print(coef, intr)
plot_y = (-1/coef[1]) * (coef[0] * plot_x + intr[0])
plt.plot(plot_x, plot_y)
plt.show()


#ax = plt.gca()
#ax.autoscale(False)
#x_vals = np.array(ax.get_xlim())
#y_vals = -(x_vals * sushi.loc[:, 'Number of tokens'] + taco.loc[:, 'Number of tokens'])/ sushi.loc[:, 'Number of links']
#plt.plot(x_vals, y_vals, '--', c="red")
#plt.show()

# plt.scatter(x_np[:,0], x_np[:,1], c=y_np.reshape(-1),cmap=mpl.colors.ListedColormap(colors))
# ax = plt.gca()
# ax.autoscale(False)
# x_vals = np.array(ax.get_xlim())
# y_vals = -(x_vals * w_guess[0] + b_guess[0])/w_guess[1]
# plt.plot(x_vals, y_vals, '--', c="red")



# read_data = pd.read_csv("insekter_fra_Ecuador.csv", sep=',', index_col=0)
# list_of_rows = [list(row) for row in read_data.values]
# column_names = list(read_data.columns.values.tolist())
#distances    = np.array(list_of_rows)

#print(list_of_rows)
#print(train_df)

# for t in train_df:
#     print(t)
# print("----------------------------")
# for t in test_df:
#     print(t)


# logReg = LogisticRegression(solver="lbfgs")
# fitted = logReg.fit(x, y)
# print(fitted)




# Oppgave (A)
#   Tren en logistisk regresjonsmodell på train_df (uten regularisering) som predikerer om wiki-siden handler
#   om et insekt fra Ecuador basert på to numeriske trekk (features), nemlig antall tokens og antall lenker på siden.
#   Hvilke accuracy oppnår du på testsettet test_df?



# Oppgave (B) Forklar hvorfor verdien du oppnådde for accuracy er så lav, basert på det du vet om logistisk regresjon. For
#   å støtte din forklaring, tegn en scatter plot (du kan bruke funksjonen scatterplot i Seaborn1) hvor de to
#   aksene står for de to numeriske trekkene, og fargen (hue) representerer outputklassen (insekt fra Ecuador eller
#   ikke). Tegn deretter beslutningslinjen som er assosiert med den logistiske regresjonsmodellen du nettopp har
#   trent.
