from flask import Flask, render_template, request
import pandas as pd
from Algorithms.KNN import *
from Algorithms.One_Class_Svm import *
from Algorithms.Log_Reg import *
from Algorithms.SVM import *
from Algorithms.Kmeans import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    algorithm = None
    if request.method == 'POST':
        # Get uploaded file
        file = request.files['file']
        if file:
            # Read CSV file
            data = pd.read_csv(file)
            
            # Choose algorithm based on selection
            algorithm = request.form['algorithm']
            if algorithm == 'knn':
                result = knn(data)
            elif algorithm == 'one_class_svm':
               result = one_class_svm(data)
            elif algorithm == 'log_reg':
                result = log_reg(data)
            elif algorithm == 'svm':
                result = testSVMWithCSV(data)
            elif algorithm == 'kmeans':
                result = testKMeansWithCSV(data)
    return render_template('index.html', result=result, algorithm=algorithm) 



if __name__ == '__main__':
    app.run(debug=True)

