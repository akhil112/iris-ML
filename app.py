import pickle
import numpy as np
from flask import Flask,render_template,request

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    # final_features = final_features.reshape(1,-1)
    prediction = model.predict(final_features)
    flower = {0:'setosa',1:'versicolor',2:'virginica'}
    result = flower.get(prediction[0])

   

    return render_template('index.html', prediction_text=' The predicted flower is  {}'.format(result))




if __name__ == '__main__':
    app.run(debug=True)
