import os
import sys
from src.Logger import logging
from src.Exception import CustomException
import pandas as pd

from src.Compnents.Data_ingestion import DataIngestion

if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()

    print(train_data_path,test_data_path)