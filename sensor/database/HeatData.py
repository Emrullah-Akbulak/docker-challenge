from .Postgres import Postgres
from datetime import datetime

class HeatData:
    table= "api_heatdata"

    def __init__(self,firstSensor:int,secondSensor:int,thirdSensor:int):
        self.firstSensor = firstSensor
        self.secondSensor = secondSensor
        self.thirdSensor = thirdSensor

    def save(self):
        cursor = Postgres.connection.cursor()
        date = datetime.now().isoformat()
    
        cursor.execute(f"""INSERT INTO {self.table} ("updatedAt","createdAt","firstSensor", "secondSensor", "thirdSensor") VALUES ('{date}','{date}',{self.firstSensor},{self.secondSensor},{self.thirdSensor});""")
        Postgres.connection.commit()

        cursor.close()