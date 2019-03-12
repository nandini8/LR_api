# LR_api
API for linear regrassion model
Uses the Titanic dataset from kaggle.com.
For prediction json is passed in the request.
Predicts the survival probability of a passenger.

Run the following commands

$ virtualenv api -p python3

$ cd api && source bin/activate

$ git clone https://github.com/nandini8/LR_api.git

$ cd LR_api

$ pip install -r requirements.txt

$ python scripts/app.py


# Endpoints

For training: /train
For predicting: /predict

Run training before predicting.

Prediction demo data:
[
    {"Age": 85, "Sex": "male", "Embarked": "S"},
    {"Age": 24, "Sex": "female", "Embarked": "C"},
    {"Age": 3, "Sex": "male", "Embarked": "C"},
    {"Age": 21, "Sex": "male", "Embarked": "S"}
]

