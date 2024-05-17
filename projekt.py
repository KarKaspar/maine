from tkinter import *
from tkinter import ttk
from tkinter import font
import random
amps=[]
app=[]
eine=[]
summa={"Filee":4,"Supp":5,"Laste-eine":6,"Vesi":1,"Coca-Cola":2,"Kohv":3}
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
            arve=0
            for i in range(len(eine)):
                silt_pwd = ttk.Label(raam, text=(summa[eine[i]]))
                silt_pwd.place(x=150, y=0+50*i)
                #sõna
                silt_pwd = ttk.Label(raam, text=(eine[i]))
                silt_pwd.place(x=70, y=0+50*i)
                arve=arve+summa[eine[i]]
            
            nimi = ttk.Label(raam, text=(arve))
            nimi.place(x=200, y=120, width=150)
            #command
            def arve():
                
                with open("köök.txt", "w", encoding="utf-8") as f:
                    for i in range(len(eine)):
                        f.write(eine[i] + "\n")
                    f.close()
                aken3.destroy()
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
        eine.append("Supp")
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
