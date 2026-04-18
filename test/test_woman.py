from _import import *
def main():
    people=int(input("表示させる人数を記載してください。"))
    if not isinstance(people,int) or (isinstance(people,int) and people<0):
        people=1
    for _ in range(people):
        print(Womanname())
if __name__=="__main__":
    main()