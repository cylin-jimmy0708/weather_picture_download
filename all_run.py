import scrap as sc
import requests
from datetime import datetime, timedelta
import os

def main():
    print("enter")
    now = datetime.now()
    start = now-(timedelta(days=1))
    if start.hour<21:
        start_hour = 20
    else:
        start_hour = start.hour
    path = os.getcwd()
    run = sc.Scarp(now, datetime(start.year, start.month, start.day, start_hour, 0, 0), path)
    #run.scrap_radar()
    run.scrap_rainfall()
    #run.scrap_hour_rainfall()
    #run.scrap_skew_T()
    #run.scrap_lightning()
    print("scrap half")
    #run.scrap_wind_profile()
    run.scrap_analysis()
    #run.scrap_temperature()
    #run.satellite()
    #run.scrap_wind()
    print("scrap 90%")
    #run.scrap_wissdom()


if __name__ == "__main__":
    main()