# LR_api
API for linear regrassion model
Uses the Titanic dataset from kaggle.com.
For prediction json is passed in the request.
Predicts the survival probability of a passenger.

# Run the following commands:

```
$ virtualenv api -p python3

$ cd api && source bin/activate

$ git clone https://github.com/nandini8/LR_api.git

$ cd LR_api

$ pip install -r requirements.txt

$ python scripts/app.py
```

# Endpoints
```
For training: /train
For predicting: /predict
```
Run training before predicting.

Prediction demo data:

    [{"Age": 85, "Sex": "male", "Embarked": "S"},
    
    {"Age": 24, "Sex": "female", "Embarked": "C"},
    
    {"Age": 3, "Sex": "male", "Embarked": "C"},
    
    {"Age": 21, "Sex": "male", "Embarked": "S"}]
    

# Docker
```
docker build -t tag-name .
docker run -d -p 5000:5000 tag-name
```

# EC2 setup
1. Create an EC2 instance
1. To launch an existing EC2 instance. Note down:
    1. image id ami-xxxxxx
    1. instance type
    1. key-name xxx.pem
    1. security group id sg-xxxxx
    1. subnet id subnet-xxxxx
    1. ```aws ec2 run-instances --image-id ami-xxxx --count 1 --instance-type t2.micro --key-name file-name --security-group-ids sg-xxxx --subnet-id subnet-xxxx```
1. Connect to the instance
    1. ```ssh -i "path/to/xxx.pem" user@public-dns.compute.amazonaws.com```
1. ```apt-get update```
1. ```apt-get install docker.io``` or ```apt-get install docker```
1. ```git clone https://github.com/nandini8/LR_api```
1. ```cd LR_api```
1. ```docker build -t ml_api .```
1. ```docker run -d -p 80:5000 ml_api```

# Future Enhancement
1. Will make the /train endpoint POST method too so that custom dataset can be passed for training
1. Can be done for multiple ML models and not restricted to just one.
