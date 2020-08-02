import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl

def plot_data(featureOne, featureTwo):

	"""
	This function plots two features against diabetes data

	Args:
		featureOne(['']): first feature
		featureTwo(['']): second featue
	Returns:
		None
	"""

	plt.scatter(list(pos[featureOne]), list(pos[featureTwo]), color = "red" )
	plt.scatter(list(neg[featureOne]), list(neg[featureTwo]), color = "green" )
	plt.xlabel(featureOne)
	plt.ylabel(featureTwo)
	plt.show()


def get_training_set():
	"""
	This function gets training set

	Args:
		None
	Returns:
		train(Dataframe)
	"""
	return train


def get_validation_set():
 	"""
	This function gets validation set

	Args:
		None
	Returns:
		validation(Dataframe)
	"""
 	return validation


# Reading data from cvs file
data = pd.read_csv("diabetes.csv", header=0)

# Drop rows with NaN values
removeNanValues = data.dropna(axis=0, how='any', thresh=None, inplace=False)

#Drop the first row and make copy
copy_removeNanValues = removeNanValues.copy()
copy_removeNanValues = copy_removeNanValues.drop(copy_removeNanValues.columns[0], axis='columns')

#replace all neg & pos values with 0 and 1
d = {'neg':0,'pos':1}
df = copy_removeNanValues.replace(d)
#spliting data into pos and neg diabetes
mask = df['diabetes'] == 1;
pos = df[mask]
neg = df[~mask]
#getting same distrbution between pos and neg diabetes into final trainig and validation set
train = pos.sample(frac=0.8)
validation = pos.drop((train.index))
neg2 = neg.sample(frac=0.8)

#true training set with 80%
train = train.append(neg2, ignore_index = True)
#true validation set with 20%
validation = validation.append(neg.drop(neg2.index), ignore_index = True)


if __name__ == '__main__':

    plot_data('age', 'pressure')
    get_training_set()
    get_validation_set()
