import csv
import os
from pathlib import Path
import numpy as np
__all__=['Japansename','Manname','Womanname']
Data_file_path=os.path.join(Path(__file__).parent,"data")
Family_name=os.path.join(Data_file_path,"japanese_family_name.csv")
rng=np.random.default_rng(seed=42)
def getcsv(path):
    with open(path,mode="r",encoding="utf-8-sig") as f:return list(csv.reader(f))
class Japansename:
    """日本人の名前を作成する"""
    name:np.ndarray
    def __init__(self,size=None):
        self.data=rng.choice(getcsv(os.path.join(Data_file_path,"name.csv")),size=size)
        self.familyname=rng.choice(getcsv(Family_name),size=size)
        self.name=np.char.add(self.familyname,self.data)
    def __iter__(self):return iter(self.name.tolist())
class Manname:
    """日本人(男)の名前を作成する"""
    name:np.ndarray
    def __init__(self,size=None):
        self.data=rng.choice(getcsv(os.path.join(Data_file_path,"man_name.csv")),size=size)
        self.familyname=rng.choice(getcsv(Family_name),size=size)
        self.name=np.char.add(self.familyname,self.data)
    def __iter__(self):return iter(self.name.tolist())
class Womanname:
    """日本人(女)の名前を作成する"""
    name:np.ndarray
    def __init__(self,size=None):
        self.data=rng.choice(getcsv(os.path.join(Data_file_path,"woman_name.csv")),size=size)
        self.familyname=rng.choice(getcsv(Family_name),size=size)
        self.name=np.char.add(self.familyname,self.data)
    def __iter__(self):return iter(self.name.tolist())
if __name__=="__main__":
    print(list(Japansename()))
    print(list(Manname()))
    print(list(Womanname()))