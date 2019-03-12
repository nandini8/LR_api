# Import dependencies
import pandas as pd
import numpy as np

#reads csv and turns to dataframes



def create_df(url, include):
    df = pd.read_csv(url)
    df_ = df[include]
    return df_


def clean_minimal_data(df_):
    #categorizes non numerical data
    categoricals = []
    for col, col_type in df_.dtypes.iteritems():
         if col_type == 'O':
              categoricals.append(col)
         else:
              df_[col].fillna(0, inplace=True)

    #Converts non numeric to numeric - One Hot encoding
    df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=False)
    return df_ohe


#Creating the model
def create_model_and_save(df_ohe):
    from sklearn.linear_model import LinearRegression
    dependent_variable = 'Survived'
    x = df_ohe[df_ohe.columns.difference([dependent_variable])]
    y = df_ohe[dependent_variable]
    lr = LinearRegression()
    lr.fit(x, y)


    #Saving the model in a pickel file
    from sklearn.externals import joblib
    joblib.dump(lr, 'model.pkl')
    model_columns = list(x.columns)
    joblib.dump(model_columns, 'model_columns.pkl')
    return 1

def train():
    url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
    include = ['Age', 'Sex', 'Embarked', 'Survived'] # Only four features
    df_ = create_df(url, include)
    df_ohe = clean_minimal_data(df_)
    flag = create_model_and_save(df_ohe)
    if flag:
        return 1
    else:
        return 0
