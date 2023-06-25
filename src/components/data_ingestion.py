import os
import sys
import pandas as pd


from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils import export_collection_as_dataframe
# from src.constant import MONGO_DATABASE_NAME
# from src.constant import MONGO_COLLECTION_NAME
# Two steps in data ingestion component, first is to configure it second is to generate artifacts for future reference by other components.
# Data class allows us not to explictly mention __init__ function.
@dataclass
class DataIngestionConfig:
    # I am going to create three files in artifacts where train_data_path is going to store trainining data.
    train_data_path: str = os.path.join("artifacts", "train.csv")
    # Raw_data_path is going to store raw data.
    raw_data_path: str = os.path.join("artifacts", "data.csv")
    # Test_data_path is going to store testing data.
    test_data_path: str = os.path.join("artifacts", "test.csv")


class DataIngestion:
    def __init__(self):
        # Here we are binding DataIngestionConfig variables into ingestion_config.
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")

        try:
            df: pd.DataFrame = export_collection_as_dataframe(
                db_name=MONGO_DATABASE_NAME, collection_name=MONGO_COLLECTION_NAME
            )
            # print()
            # print("This one in data_ingestion.py ", df.head())

            logging.info("Exported collection as dataframe")

            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True
            )
            # dumping raw data.
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            # dumping training and testing set.
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True
            )

            test_set.to_csv(
                self.ingestion_config.test_data_path, index=False, header=True
            )

            logging.info(
                f"Ingested data from mongodb to {self.ingestion_config.raw_data_path}"
            )

            logging.info("Exited initiate_data_ingestion method of DataIngestion class")

            return (
                # Below information will be returned to our training pipeline and will be passed to data transformation components.
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            raise CustomException(e, sys)
