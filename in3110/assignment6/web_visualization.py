import sys
sys.path.insert(1,'../')
from flask import Flask
from flask import render_template, request, send_from_directory, current_app
import os
import matplotlib.pyplot as plt
import matplotlib
from visualize import plot
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def plot_visulization():

	"""
	This function calls web_visualization.html when requested. 

	User can set two features and one classifier in order to calculate a new graph.

	Args:
		None
	Returns
		flask.render_template(): rendering of the page
	"""
	# If user accesses through the form/POST:
	if request.method == 'POST':
		req = request.form
		features=['glucose','mass']
		if 'first_feature' in request.form:
			first =  request.form.get('first_feature')
			features[0]=first
			
		if 'second_feature' in request.form:
			second = req.get('second_feature')

			features[1]=second
		
		if 'classifier' in request.form:
			classifier =  request.form.get('classifier')

		if classifier is ('knn'):
				selected_classifier =  KNeighborsClassifier()
		else:
			selected_classifier =  QuadraticDiscriminantAnalysis()
	# If the page is not accessed through the form:
	else:
		classifier ='knn'
		selected_classifier = KNeighborsClassifier()
		features = ['glucose','mass']

	# Sets plot name
	plot_name='static/images/'+str(features[0])+str(features[1])+str(classifier)+'.png'
	# Plots the data
	pl = plot(features, selected_classifier)
	# Saves the figure
	pl.savefig(plot_name)

	# Renders the page
	return render_template('web_visualization.html', url=plot_name, classifier=classifier, first=features[0], second=features[1])

# Help pages
@app.route("/help")
def help():
    return render_template('help.html')

@app.route("/help/visualize")
def visualize():
    return render_template('help/visualize.html')

@app.route("/help/fitting")
def fitting():
    return render_template('help/fitting.html')

@app.route("/help/data")
def data():
    return render_template('help/data.html')

# A better-looking pydoc I created with a module called "pdoc"
@app.route("/help2/index.html")
def help2_index():
    return current_app.send_static_file('help2/index.html')

@app.route("/help2/data.html")
def data2():
    return current_app.send_static_file('help2/data.html')

@app.route("/help2/visualize.html")
def visualize2():
    return current_app.send_static_file('help2/visualize.html')

@app.route("/help2/fitting.html")
def fitting2():
    return current_app.send_static_file('help2/fitting.html')

@app.route("/help2/web_visualization.html")
def web_visualization():
    return current_app.send_static_file('help2/web_visualization.html')



if __name__ == "__main__":
	app.run(debug=True,port=5001)
