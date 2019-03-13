from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
import model

app = Flask(__name__)


@app.route('/predict', methods=['POST']) # Your API endpoint URL would consist /predict
def predict():
    model_file_name = 'model.pkl'
    model_columns_file_name = 'model_columns.pkl'
    lr = joblib.load(model_file_name) # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load(model_columns_file_name) # Load "model_columns.pkl"
    print ('Model columns loaded')
    if lr:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(lr.predict(query))

            return jsonify({'prediction': prediction})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')


@app.route('/train')
def train():
    flag = model.train()
    if flag:
        return "Data trained"
    else:
        return "Data not trained"


if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line argument
    except:
        port = 5000
    app.run(port=port, debug=True, host='*')
