# impordi tk vidinad ja konstandid
from tkinter import *
from tkinter import ttk
from tkinter import font
import random
amps=[]
app=[]
eine=[]
summa=[random.randint(1, 10),random.randint(1, 10)]
aken = Tk()

def toit():
    aken.destroy()
    aken1 = Tk()
    def jook():
        aken1.destroy()
        aken2 = Tk()
        def maksa():
            aken2.destroy()
            aken3 = Tk()
            aken3.title("tellimine")
            aken3.geometry("450x300")
            #stiil
            s = ttk.Style()
            s.configure('Danger.TFrame',
                    borderwidth=5,
                    relief='raised')
            #raame
            raam = ttk.Frame(aken3,width=450,height=300,style='Danger.TFrame').grid()

            
            #sõna
            for i in range(len(eine)):
                silt_pwd = ttk.Label(raam, text=(random.randint(1, 10)))
                silt_pwd.place(x=150, y=0+50*i)
                #sõna
                silt_pwd = ttk.Label(raam, text=(eine[i]))
                silt_pwd.place(x=70, y=0+50*i)
            
            nimi = ttk.Entry(raam)
            nimi.place(x=200, y=120, width=150)
            #command
            def arve():
                ak=nimi.get()
                if ak=="":
                    ak="0"
                #print(type(ak))
                print((summa[0]+summa[1]),int(float(ak)))
                print(type((summa[0]+summa[1])),type(str(float(ak))))
                #ab=(list(ak))
                #try:
                #    print(ab)
                #except:
                #    pass
                
                if ak.isnumeric()==True and (summa[0]*10)<=int(ak):
                    with open("köök.txt", "w", encoding="utf-8") as f:
                        f.write(eine[0]+ "\n"+eine[1]+ "\n")
                        f.close()
                    aken3.destroy()
                else:
                    print("proovi uuesti")
            # loome nupu
            nupp2 = ttk.Button(raam, text="Telli",command=arve)  
            nupp2.place(x=200, y=150)
            aken3.mainloop()
        
        
        aken2.title("tellimine")
        aken2.geometry("450x300")
        #stiil
        s = ttk.Style()
        s.configure('Danger.TFrame',
                borderwidth=5,
                relief='raised')
        #raame
        raam = ttk.Frame(aken2,width=450,height=300,style='Danger.TFrame').grid()

        #pilt
        #command
        def kohv():
            eine.append("Kohv")
        # loome nupu
        nupp2 = ttk.Button(raam, text="Kohv",command=kohv)  
        nupp2.place(x=70, y=150)

        #pilt
        #command
        def coca_cola():
            eine.append("Coca-Cola")
        # loome nupu
        nupp2 = ttk.Button(raam, text="Coca-Cola",command=coca_cola)  
        nupp2.place(x=200, y=150)
        
        #pilt
        #command
        def vesi():
            eine.append("Vesi")
        # loome nupu
        nupp2 = ttk.Button(raam, text="Vesi",command=vesi) 
        nupp2.place(x=330, y=150)
        
        def edasi():
            maksa()
        nupp2 = ttk.Button(raam, text="Edasi",command=edasi) 
        nupp2.place(x=350, y=200)
        
        aken2.mainloop()
    
    aken1.title("tellimine")
    aken1.geometry("450x300")
    #stiil
    s = ttk.Style()
    s.configure('Danger.TFrame',
            borderwidth=5,
            relief='raised')
    #raame
    raam = ttk.Frame(aken1,width=450,height=300,style='Danger.TFrame').grid()

    #pilt
    #command
    def laste_eine():
        eine.append("Laste-eine")
    # loome nupu
    nupp2 = ttk.Button(raam, text="Laste-eine",command=laste_eine)  
    nupp2.place(x=70, y=150)

    #pilt
    #command
    def filee():
        eine.append("Filee")
    # loome nupu
    nupp2 = ttk.Button(raam, text="Filee",command=filee)  
    nupp2.place(x=200, y=150)
    
    #pilt
    #command
    def supp():
        eine.append("supp")
    # loome nupu
    nupp2 = ttk.Button(raam, text="Supp",command=supp)  
    nupp2.place(x=330, y=150)
    #command
    def edasi():
        jook()
    # loome nupu
    nupp2 = ttk.Button(raam, text="Edasi",command=edasi)  
    nupp2.place(x=350, y=200)
    aken1.mainloop()

#aken

aken.title("Koduleht")
aken.geometry("450x300")
#stiil
s = ttk.Style()
s.configure('Danger.TFrame',
        borderwidth=5,
        relief='raised')
#raame
raam = ttk.Frame(aken,width=450,height=300,style='Danger.TFrame').grid()

#sõna
silt_pwd = ttk.Label(raam, text="Koduleht")
silt_pwd.place(x=200, y=120)

# loome nupu
nupp2 = ttk.Button(raam, text="Telli", command=toit)  
nupp2.place(x=200, y=150)

aken.mainloop()
