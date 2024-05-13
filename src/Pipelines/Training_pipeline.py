import os
import sys
from src.Logger import logging
from src.Exception import CustomException
import pandas as pd

from src.Compnents.Data_ingestion import DataIngestion
from src.Compnents.Data_transformation import DataTransformation
from src.Compnents.Model_trainer import ModelTrainer


if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)

    data_transformation=DataTransformation()

    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    model_trainer=ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)


