import sys
import os
from source_code.exception import CustomException
from source_code.logger import logging
from source_code.utils import load_obj
import pandas as pd


class PredictPipeline:
    def __init__(self) -> None:
        pass

    def predict(self, features):
        try:
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_obj(preprocessor_path)
            model = load_obj(model_path)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            logging.info(
                "Error occured in predict function in prediction_pipeline location"
            )
            raise CustomException(e, sys)


class CustomData:
    def __init__(
        self,
        Airline: str,
        Flight: float,
        AirportFrom: str,
        AirportTo: str,
        DayOfWeek: float,
        Time: float,
        Length: float,
    ):
        self.Airline = Airline
        self.Flight = Flight
        self.AirportFrom = AirportFrom
        self.AirportTo = AirportTo
        self.DayOfWeek = DayOfWeek
        self.Time = Time
        self.Length = Length

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "Airline": [self.Airline],
                "Flight": [self.Flight],
                "AirportFrom": [self.AirportFrom],
                "AirportTo": [self.AirportTo],
                "DayOfWeek": [self.DayOfWeek],
                "Time": [self.Time],
                "Length": [self.Length],
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info("Dataframe created")
            return df
        except Exception as e:
            logging.info(
                "Error occured in get_data_as_dataframe function in prediction_pipeline"
            )
            raise CustomException(e, sys)
