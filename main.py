# VERSION 1 IS DONE, LOOKING FOR BUGS

import random
import pandas as pd

def way_one(n,mxl,chance,mon):
    print("way-1")
    if(chance>=len(mon)):
        maxch=len(mon)
    else:
        maxch=chance
    for i in range(maxch):
        g=random.choice(mon)
        print(n,g)
        if g==n:
            print("Guessed")
            flg=0
            if g in rows:
                flg=1
                print("flag")
                result=df.loc[df['no'] == g,'time'].values[0]
                result=result+1
                df.loc[df['no'] == n, 'time'] = result
                print(df)
                df.to_csv("knowledge.csv", index=False)
            else:
                flg=0
                print("flag=0 print")
                df1=pd.DataFrame({'no':[n],'time':[1]})
                df1.to_csv('knowledge.csv', mode='a', header=False, index=False)               
            return True
        else:
            print("Not Guessed")
    return False

def way_two(n,mxl,chance):
    print("way-2")
    for i in range(chance):
        g=random.randint(0,mxl)
        print(n,g)
        if g==n:
            print("Guessed")
            flg=0
            if g in rows:
                flg=1
                print("flag")
                result=df.loc[df['no'] == g,'time'].values[0]
                result=result+1
                df.loc[df['no'] == n, 'time'] = result
                print(df)
                df.to_csv("knowledge.csv", index=False)
            else:
                flg=0
                print("flag=0 print")
                df1=pd.DataFrame({'no':[n],'time':[1]})
                df1.to_csv('knowledge.csv', mode='a', header=False, index=False)               
            return True
        else:
            print("Not Guessed")
    return False

mxl=10
st="Enter your number in range (0 to "+str(mxl)+"):"
n=int(input(st))
chance=5
df=pd.read_csv("knowledge.csv")
df.dropna(inplace = True)
rows=df.loc[:,'no'].to_list()

#get max occurred no.
time_arr=df.loc[:,'time'].to_list()
mon=df.loc[df['time'] == max(time_arr),'no'].values.tolist()
print(mon)

if(way_one(n,mxl,chance,mon)):
    print("w1")
else:
    x=way_two(n,mxl,chance)
