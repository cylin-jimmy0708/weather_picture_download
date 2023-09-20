import requests
from datetime import datetime, timedelta

class Scarp:
    '''
    主要處理天氣學中天氣分析可能所需之資料
    不過過程中仍有許多部分仍待改進(例如或許爬圖片的部分可以利用function直接寫成procedure)
    目前可爬資料包含溫度、降水量、雷達資料(CV1無地形)、天氣圖(KMA之surf、850、700、500hpa、500hpa極投影)、
    雷達(CV1)、探空圖(台北)、衛星(真實色及色調強化)、剖風儀、閃電
    '''
    #today = datetime.now()
    #init_time = datetime(2023, 4, 18, 15, 0, 0)

    def __init__(self, today, init_time, root):
        self.today = today
        self.init_time = init_time
        self.root = root
        #pass

    def scrap_radar(self):
        run_time = self.init_time
        delta = timedelta(minutes=10)
        while (self.today-run_time).days != -1:
            run_time_str = f"{run_time.month:02d}{run_time.day:02d}"
            file_procedure(self.root, "雷達", run_time_str)

            str_time = f"{run_time.year:04d}{run_time.month:02d}{run_time.day:02d}{run_time.hour:02d}{run_time.minute:02d}"
            url = "https://www.cwa.gov.tw/Data/radar/CV1_3600_"+str_time+".png"
            filename = self.root+"//"+str_time[4:8]+"//雷達//CV1_3600_"+str_time+".png"

            save_fig(url, filename)
            
            run_time = run_time + delta
    
    def scrap_temperature(self):
        run_time = self.init_time
        delta = timedelta(hours=1)
        while (self.today-run_time).days != -1:
            run_time_str = f"{run_time.month:02d}{run_time.day:02d}"
            file_procedure(self.root, "氣溫", run_time_str)
            
            str_time = f"{run_time.year:04d}-{run_time.month:02d}-{run_time.day:02d}_{run_time.hour:02d}{run_time.minute:02d}"
            url = f"https://www.cwa.gov.tw/Data/temperature/{str_time}.GTP8w.jpg"
            filename = self.root+"//"+str_time[5:7]+str_time[8:10]+"//氣溫//Temperature_"+str_time+".jpg"

            save_fig(url, filename)
            
            run_time = run_time + delta
    
    def scrap_rainfall(self):
        run_time = self.init_time
        delta = timedelta(minutes=30)
        while (self.today-run_time).days != -1:
            run_time_str = f"{run_time.month:02d}{run_time.day:02d}"
            file_procedure(self.root, "降水", run_time_str)

            str_time = f"{run_time.year:04d}-{run_time.month:02d}-{run_time.day:02d}_{run_time.hour:02d}{run_time.minute:02d}"
            url = f"https://www.cwa.gov.tw/Data/rainfall/{str_time}.QZJ8.jpg"
            filename = self.root+"//"+str_time[5:7]+str_time[8:10]+"//降水//Rainfall_"+str_time+".jpg"

            save_fig(url, filename)
            
            run_time = run_time + delta
    
    def scrap_hour_rainfall(self):
        run_time = self.init_time
        delta = timedelta(hours=1)
        while (self.today-run_time).days != -1:
            run_time_str = f"{run_time.month:02d}{run_time.day:02d}"
            file_procedure(self.root, "逐時降水", run_time_str)

            str_time = f"{run_time.year:04d}-{run_time.month:02d}-{run_time.day:02d}_{run_time.hour:02d}{run_time.minute:02d}"
            url = f"https://www.cwa.gov.tw/Data/rainfall/{str_time}.QZT8.jpg"
            filename = self.root+"//"+str_time[5:7]+str_time[8:10]+"//逐時降水//Rainfall_per_hour_"+str_time+".jpg"

            save_fig(url, filename)
            
            run_time = run_time + delta    

    def scrap_skew_T(self):
        run_date = self.init_time - timedelta(days=1)
        run_time = datetime(run_date.year, run_date.month, run_date.day, 12, 0)
        delta = timedelta(hours=12)
        while (self.today - timedelta(hours=8) - run_time).days != -1:
            run_time_str = f"{run_time.month:02d}{run_time.day:02d}"
            file_procedure(self.root, "探空圖", run_time_str)

            str_time = f"{str(run_time.year).zfill(4)[2:]}{run_time.month:02d}{run_time.day:02d}{run_time.hour:02d}"
            url = f"https://npd.cwa.gov.tw/NPD/irisme_data/Weather/SKEWT/SKW___000_{str_time}_46692.gif"
            filename = self.root+"//"+str_time[2:6]+"//探空圖//SKEWT_"+str_time+".jpg"

            save_fig(url, filename)
            
            run_time = run_time + delta
    
    def satellite(self):
        run_time = self.init_time
        delta = timedelta(minutes=10)
        while (self.today - run_time).days != -1:
            run_time_str = f"{run_time.month:02d}{run_time.day:02d}"
            file_procedure(self.root, "真實色衛星", run_time_str)
            file_procedure(self.root, "色調強化衛星", run_time_str)

            str_time = f"{run_time.year:04d}-{run_time.month:02d}-{run_time.day:02d}-{run_time.hour:02d}-{run_time.minute:02d}"
            url1 = f"https://www.cwa.gov.tw/Data/satellite/LCC_VIS_TRGB_2750/LCC_VIS_TRGB_2750-{str_time}.jpg"
            filename1 = f"{self.root}//{str_time[5:7]}{str_time[8:10]}//真實色衛星//LCC_VIS_{str_time}.jpg"


            url2 = "https://www.cwa.gov.tw/Data/satellite/LCC_IR1_MB_2750/LCC_IR1_MB_2750-"+str_time+".jpg"
            filename2 = f"{self.root}//{str_time[5:7]}{str_time[8:10]}//色調強化衛星//LCC_IR1_{str_time}.jpg"

            save_fig(url1, filename1)
            save_fig(url2, filename2)

            run_time = run_time + delta
    
    def scrap_analysis(self):
        run_date = self.init_time - timedelta(days=1)
        run_time = datetime(run_date.year, run_date.month, run_date.day, 12, 0)
        delta = timedelta(hours=12)
        while (self.today - timedelta(hours=8) - run_time).days != -1:

            run_time_str = f"{run_time.month:02d}{run_time.day:02d}"
            file_procedure(self.root, "天氣圖", run_time_str)
            #surface
            str_time = f"{run_time.year:04d}{run_time.month:02d}{run_time.day:02d}{run_time.hour:02d}"  # 使用 f-strings 格式化字串
            url1 = f"https://www.weather.go.kr/w/repositary/image/cht/img/surf_{str_time}.png"
            filename1 = f"{self.root}//{str_time[4:8]}//天氣圖//surf_{str_time}.png"

            url2 = f"https://www.weather.go.kr/w/repositary/image/cht/img/up85_{str_time}.png"
            filename2 = f"{self.root}//{str_time[4:8]}//天氣圖//up85_{str_time}.png"

            url3 = f"https://www.weather.go.kr/w/repositary/image/cht/img/up70_{str_time}.png"
            filename3 = f"{self.root}//{str_time[4:8]}//天氣圖//up70_{str_time}.png"

            url4 = f"https://www.weather.go.kr/w/repositary/image/cht/img/up50_{str_time}.png"
            filename4 = f"{self.root}//{str_time[4:8]}//天氣圖//up50_{str_time}.png"

            url5 = f"https://www.weather.go.kr/w/repositary/image/cht/img/kim_n500_anlmod_pb4_{str_time}.gif"
            filename5 = f"{self.root}//{str_time[4:8]}//天氣圖//polar_500_{str_time}.png"
            
            save_fig(url1, filename1)
            save_fig(url2, filename2)
            save_fig(url3, filename3)
            save_fig(url4, filename4)
            save_fig(url5, filename5)

            run_time = run_time + delta        

    def scrap_lightning(self):
        run_time = self.init_time
        delta = timedelta(hours=1)
        while (self.today-run_time).days != -1:
            run_time_str = f"{run_time.month:02d}{run_time.day:02d}"
            str_time = f"{run_time.year:04d}{run_time.month:02d}{run_time.day:02d}{run_time.hour:02d}"
            url = f"https://www.cwb.gov.tw/Data/lightning/{str_time}0000_lgtl.jpg"
            filename = f"{self.root}//{run_time_str}//閃電//lightning_{str_time}.jpg"

            file_procedure(self.root, "閃電", run_time_str)
            
            save_fig(url, filename)
            
            run_time = run_time+delta

    def scrap_wind(self):
        run_time = self.init_time
        delta = timedelta(hours=1)
        while (self.today-run_time).days != -1:

            run_time_str = f"{run_time.month:02d}{run_time.day:02d}"
            file_procedure(self.root, "風", run_time_str)

            str_time = f"{run_time.year:04d}{run_time.month:02d}{run_time.day:02d}{run_time.hour:02d}"
            url1 = f"https://watch.ncdr.nat.gov.tw/00_Wxmap/5A7_CWB_WINDMAP/{str_time[0:6]}/windmap_{str_time}00.png"
            filename1 = f"{self.root}//{run_time_str}//風//windmap_{str_time}.png"
            url2 = f"https://watch.ncdr.nat.gov.tw/00_Wxmap/5A7_CWB_WINDMAP/{str_time[0:6]}/windmap_town_{str_time}00.png"
            filename2 = f"{self.root}//{run_time_str}//風//windmap_town_{str_time}.png"
            
            save_fig(url1, filename1)
            save_fig(url2, filename2)
            
            run_time = run_time+delta        

    def scrap_wind_profile(self):
        run_time = self.init_time
        delta = timedelta(hours=1)
        while (self.today-run_time).days != -1:
            run_time_str = f"{run_time.month:02d}{run_time.day:02d}"

            str_date = f"{run_time.year:04d}-{run_time.month:02d}-{run_time.day:02d}"
            str_time = f"{run_time.hour:02d}:{run_time.minute:02d}"
            str_datetime = f"{run_time.year:04d}{run_time.month:02d}{run_time.day:02d}{run_time.hour:02d}"
            url = f"https://watch.ncdr.nat.gov.tw/php/watch_plot_profiler.php?d={str_date}&t={str_time}&v=spd&m=6&num=60&tt={str_datetime}00"
            filename = f"{self.root}//{run_time_str}//剖風//profiler_{str_datetime}.jpg"

            file_procedure(self.root, "剖風", run_time_str)
            
            save_fig(url, filename)
            
            run_time = run_time+delta        

    def scrap_wissdom(self):
        run_time = self.init_time
        delta = timedelta(hours=1)
        height = ["最大回波", "0.5", "1.0", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0", "4.5", "5.0", "5.5", "6.0", "6.5", "7.0", "7.5", "8.0", "8.5", "9.0", "9.5", "10.0"]
        while (self.today-run_time).days != -1:
            run_time_str = f"{run_time.month:02d}{run_time.day:02d}"
            file_procedure(self.root, "wissdom", run_time_str)

            #str_year_month = f"{run_time.year:04d}{run_time.month:02d}"
            #str_date = f"{run_time.year:04d}{run_time.month:02d}{run_time.day:02d}"
            str_datetime = f"{run_time.year:04d}{run_time.month:02d}{run_time.day:02d}{run_time.hour:02d}{run_time.minute:02d}"

            for order in range(len(height)):
                url = f"https://watch.ncdr.nat.gov.tw/00_Wxmap/7A10_NCDR_WISSDOM_TAIWAN/{str_datetime[:6]}/{str_datetime[:8]}/{str_datetime}/WISSDOM_dbz_{order}_{str_datetime}_small.png"
                filename = f"{self.root}//{run_time_str}//wissdom//{height[order]}//WISSDOM_{height[order]}_{str_datetime}.jpg"


                create_type_folder(f"{self.root}//{run_time_str}", height[order], "wissdom")
                save_fig(url, filename)
            
            run_time = run_time+delta         



def create_date_folder(folder_root, run_time_str):
    import os
    path = f'{folder_root}//{run_time_str}'
    if os.path.exists(path) == False:
        os.mkdir(path)        

def create_type_folder(folder_root, name, run_time_str):
    import os
    path = f'{folder_root}//{run_time_str}//{name}'
    if os.path.exists(path) == False:
        os.mkdir(path)

def save_fig(url, filename):
    response = requests.get(url)

    with open(filename, "wb") as f:
        f.write(response.content)        

def file_procedure(folder_root, name, run_time_str):
    create_date_folder(folder_root, run_time_str)
    create_type_folder(folder_root, name, run_time_str)

#main=Scarp(datetime(2023, 4, 24, 12, 0, 0), datetime(2023, 4, 23, 3, 0, 0), "C://Users//User//Desktop//林啓揚//大三//天氣學//天氣實習")
#main.scrap_lightning()
#main.scrap_temperature()
#main.scrap_temperature()
#main.scrap_wissdom()