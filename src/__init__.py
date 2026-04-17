import csv
import os
import random
from pathlib import Path
__all__=['Japansename','Manname','Womanname']
Data_file_path=os.path.join(Path(__file__).parent,"data")
Family_name=os.path.join(Data_file_path,"japanese_family_name.csv")
def getcsv(path):
    with open(path,mode="r",encoding="utf-8-sig") as f:return list(csv.reader(f))
class Japansename:
    """日本人の名前を作成する"""
    def __init__(self):
        self.data=random.choice(getcsv(os.path.join(Data_file_path,"name.csv")))
        self.familyname=random.choice(getcsv(Family_name))
        self.name=f"{self.familyname[0]} {self.data[0]}"
        self.namek=f"{self.familyname[1]} {self.data[1]}"
        self.nameh=f"{self.familyname[2]} {self.data[2]}"
        self.nameR=f"{self.familyname[3]} {self.data[3]}"
    def __iter__(self):return iter([self.name,self.namek,self.nameh,self.nameR])
    def __str__(self):return self.name
class Manname:
    """日本人(男)の名前を作成する"""
    def __init__(self):
        self.data=random.choice(getcsv(os.path.join(Data_file_path,"man_name.csv")))
        self.familyname=random.choice(getcsv(Family_name))
        self.name=f"{self.familyname[0]} {self.data[0]}"
        self.namek=f"{self.familyname[1]} {self.data[1]}"
        self.nameh=f"{self.familyname[2]} {self.data[2]}"
        self.nameR=f"{self.familyname[3]} {self.data[3]}"
    def __iter__(self):return iter([self.name,self.namek,self.nameh,self.nameR])
    def __str__(self):return self.name
class Womanname:
    """日本人(女)の名前を作成する"""
    def __init__(self):
        self.data=random.choice(getcsv(os.path.join(Data_file_path,"woman_name.csv")))
        self.familyname=random.choice(getcsv(Family_name))
        self.name=f"{self.familyname[0]} {self.data[0]}"
        self.namek=f"{self.familyname[1]} {self.data[1]}"
        self.nameh=f"{self.familyname[2]} {self.data[2]}"
        self.nameR=f"{self.familyname[3]} {self.data[3]}"
    def __iter__(self):return iter([self.name,self.namek,self.nameh,self.nameR])
    def __str__(self):return self.name
if __name__=="__main__":
    japanese_name=Japansename()
    man_name=Manname()
    woman_name=Womanname()
    print(str(japanese_name))
    print(list(japanese_name))
    print(str(man_name))
    print(list(man_name))
    print(str(woman_name))
    print(list(woman_name))