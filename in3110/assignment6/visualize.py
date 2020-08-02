from sklearn import neighbors, datasets, linear_model
import pylab as pl
import numpy as np
from matplotlib.colors import ListedColormap
from data import get_training_set
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

cmap_light = ListedColormap(['#90ee90', '#ffcccb', '#ffcccb'])
cmap_bold = ListedColormap(['green', 'red', 'red'])


def plot(features, model):
    """
    This function plots data for 2 features for a certain model/clasifier

    Args:
        features(['']): features to plot for
        model(classifier): a clasisfier to fit for
    Returns:
        pl(plot): returns plot

    """
    #Getting training set, setting it up and fitting it
    training_set = get_training_set()
    # Change: removed the pop because it only worked half of the time I used web_visualize
    target = training_set['diabetes']
    training_set = training_set[features]
    model.fit(training_set, target)

    #Setting up range for the plots
    x_min, x_max = training_set.iloc[:, 0].min() - .1, training_set.iloc[:, 0].max() + .1
    y_min, y_max = training_set.iloc[:, 1].min() - .1, training_set.iloc[:, 1].max() + .1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    pl.figure()
    pl.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    pl.scatter(training_set.iloc[:, 0], training_set.iloc[:, 1], c=target, cmap=cmap_bold)
    pl.xlabel(features[0])
    pl.ylabel(features[1])
    pl.axis('tight')

    
    return pl


if __name__ == '__main__':

    knn = KNeighborsClassifier()
    features = ['age','pressure']
    pl = plot(features, knn)
    pl.show()
