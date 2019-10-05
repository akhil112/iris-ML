import pickle
import numpy as np
from flask import Flask,render_template,request,request,jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/num/<int:num>',methods=['GET'])
def multiply(num):
    return jsonify({'result':num*100})

@app.route('/rest',methods=['POST'])
def rest_api():
    payload = request.get_json()
    values = [int(i) for i in payload.values()]
    final_features = [np.array(values)]
    prediction = model.predict(final_features)
    flower = {0:'setosa',1:'versicolor',2:'virginica'}
    result = flower.get(prediction[0])

    

    
    return jsonify({'class':result})




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
    app.run(debug=True,port=8090)
