# 變更標籤內容
import tkinter as tk
from tkinter import ttk
import csv
import numpy as np











try:
    
    with open("歷史開獎紀錄.csv","r",encoding="utf-8-sig") as f:
        r=csv.reader(f)
        r=list(r)
    with open("本金.csv","r",encoding="utf-8-sig") as f:
        rr=csv.reader(f)
        rr=list(rr)    
    
    his=r[0]
    x=eval(rr[0][0])
    total={1:x}
except:
    his=[]
    total={1:1000}
win = tk.Tk()
win.title("楓行娛樂")

sample=["1","2","3","4","5","6"]
frame1=tk.Frame(win)
frame1.pack(fill='x')
frame2=tk.Frame(win)
frame2.pack(fill='x')


str=tk.StringVar()
bs3={"單號1":0,"單號2":0,"單號3":0,"單號4":0,"單號5":0,"單號6":0,"大":0,"小":0,"單號":0,"雙號":0,11:0}    
c=0
co=0
co1=0
co2=0    
total1=0
list=[]
def pr():
    line=""
    lb.insert("end",line)

def muru():

        btn1.config(text="目錄")


def button():
        
        lab.grid_forget()
        lb.pack(fill="x")
        btn1.destroy()
        btn2.grid(row=3,column=1)
        btn4.grid(row=3,column=2)
        btn6.grid(row=3,column=3)
        btn7.grid(row=3,column=4)
        
        text.grid(row=1,column=3)
        lab2.grid(row=1,column=1)
        lab1.grid(row=1,column=2)
        comboExample.grid(row=1,column=4)
    
def kie():
           # b.pack_forget()

            btn2.destroy()
            btn3.destroy()
            btn4.destroy()
            btn5.destroy()
            btn6.destroy()



def out():
    win.quit()
print(total)

def d1():
    lb.delete(0,"end")
    total1=int(total[1])
    d1=int(text.get())
    d3=comboExample.get()
    d2=comboExample.current()
    if  0<comboExample.current()<13:
        if d1>0:
            if total[1]>=d1:
                total[1]=total1-eval(text.get())
                bs3[d3]=bs3[d3]+d1
    line=""
    for i in bs3:
        if bs3[i]>0:
            line=f"{i}：{bs3[i]}\n"
            lb.insert("end",line)
    line2=""
    line2=line2+f"本金有:{total[1]}"
    lab2.config(text=line2)
    lb.see("end")


def total123():
            lb.delete(0,"end")
            line=""
            for i in bs3:
                if bs3[i]>0:
                    line=f"{i}：{bs3[i]}\n"
                    lb.insert("end",line)
            
            total2=0.0
            random=np.random.choice(sample,1)
            his.append(random[0])
            line=f"第{len(his)}期骰子骰出\t{random[0]}!!!\n"
            lb.insert("end",line)
            if random=="1":
               total2+=bs3["單號1"]*5+bs3["小"]*1.2+bs3["單號"]*1.2
            elif random=="2":
               total2+=bs3["單號2"]*5+bs3["小"]*1.2+bs3["雙號"]*1.2
            elif random=="3":
                total2+=bs3["單號3"]*5+bs3["小"]*1.2+bs3["單號"]*1.2
            elif random=="4":
                total2+=bs3["單號4"]*5+bs3["大"]*1.2+bs3["雙號"]*1.2
            elif random=="5":
                total2+=bs3["單號5"]*5+bs3["大"]*1.2+bs3["單號"]*1.2
            elif random=="6":
                total2+=bs3["單號6"]*5+bs3["大"]*1.2+bs3["雙號"]*1.2
            print(total2)
            if total2>0:
                line=f"恭喜你贏得了{total2}塊錢"
                lb.insert("end",line) 
            else:
                gg=0
                for i in bs3:
                    gg+=bs3[i]
                if gg>0:
                    line=f"本輪你輸了{gg}"
                    lb.insert("end",line)    

            for i in bs3:
                bs3[i]=0
            total[1]=(total[1]+total2)
            line2=""
            line2=line2+f"本金有:{total[1]}"
            lab2.config(text=line2)     
            xxx=[total[1]]
            with open("本金.csv","w",encoding="utf-8-sig") as f:
                w=csv.writer(f)
                w.writerow(xxx)
                
            with open("歷史開獎紀錄.csv","w",encoding="utf-8-sig") as f:
                w=csv.writer(f)
                w.writerow(his)
                print("程式結束")
        
def hon():
    line2=""
    line2=line2+f"本金有:{total[1]}"
    lab2.config(text=line2)


def his1():
    lb.delete(0,"end")
    for i in range(len(his)):
        line=f"第{(i+1)}期號碼為:{his[i]}\n"
        lb.insert("end",line)
    line="-"*20
    lb.insert("end",line)
    for i in sorted((set(his))):
        line=("號碼{} 機率為:{}%".format(i,round(his.count(i)/len(his),2)*100))        
        lb.insert("end",line)
    line2=""
    line2=line2+f"本金有:{total[1]}"
    lab2.config(text=line2)
    lb.see("end")

def re():
    lb.delete(0,"end")
    total[1]=1000
    for i in bs3:
        bs3[i]=0
    line2=""
    line2=line2+f"本金有:{total[1]}"
    lab2.config(text=line2)

comboExample = ttk.Combobox(frame2, 
                            values=[
                                    "請選擇號碼",
                                    "單號1", 
                                    "單號2",
                                    "單號3",
                                    "單號4",
                                    "單號5",
                                    "單號6",
                                    "大",
                                    "小",
                                    "單號",
                                    "雙號"])
comboExample.current(0)



    
btn1 = tk.Button(frame2, text = "開始", command = button,width=10)
btn2 = tk.Button(frame2, text = "下注", command = d1,width=20)
btn3 = tk.Button(frame2, text = "目前下注金額", command = button,width=10)
btn4 = tk.Button(frame2, text = "歷史開獎紀錄", command = his1,width=20)
btn5 = tk.Button(frame2, text = "本金", command = hon,width=10)
btn6 = tk.Button(frame2, text = "重製遊戲", command = re,width=20)
btn7 = tk.Button(frame2, text = "開獎", command = total123,width=20)



text = tk.Entry(frame2,width=20,text="0")
lab = tk.Label(frame2,text="歡迎來到骰子賭場\n新玩家可以擁有1000元本金\n舊玩家只能繼承上次剩下的本金\n輸完就沒了喔", fg = '#0000ff',font=100 )
lab1=tk.Label(frame2,text="下注金額:")
lab2=tk.Label(frame2,text=f"本金{total[1]}", fg = '#0000ff',font=100)
lb=tk.Listbox(frame1,height=20)


lab.grid(row=1,column=4)
btn1.grid(row=2,column=4)

win.mainloop()
