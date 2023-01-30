from joblib import load
#from scipy.sparse import data
from sklearn.pipeline import Pipeline
from pydantic import BaseModel
from pandas import DataFrame
import os 
from io import BytesIO

def get_model() -> Pipeline:
    model_path = os.environ.get('MODEL_PATH','model/model.pkl')
    with open(model_path,'rb') as model_file:
        model = load(BytesIO(model_file.read()))
    return model

# def get_model() -> Pipeline: # creamos una funcion sin parametros que retornara un objeto de tipo Pipeline 
#     model = load("model/model.pkl")
#     return model

# toma el registro lo pasa a diccionario y luego a DataFrame, luego con get_prediction() es hecha la predicción de este registro
def transform_to_dataframe(class_model: BaseModel) -> DataFrame:
    transition_dictionary = {key:[value] for key, value in class_model.dict().items()}
    data_frame = DataFrame(transition_dictionary)
    return data_frame