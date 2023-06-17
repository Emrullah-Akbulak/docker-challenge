from database.Postgres import Postgres
from database.HeatData import HeatData
from random import uniform
from time import sleep

def generateRandomData():
    return [uniform(0,100),uniform(0,100),uniform(0,100)]

if __name__ == '__main__':
    Postgres.connect()
    while True:
        randomData = generateRandomData()
        print(f"Writing new data {randomData}")
        req = HeatData(*randomData)
        req.save()
        sleep(5)


    

