from tkinter import *
from tkinter import ttk
from tkinter import font
import matplotlib.pyplot as plt
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
            
            def graafik():
                aken3.destroy()
                hind = []
                for c in range(len(eine)):
                    hind.append(summa[eine[c]])

                # Visualiseerime andmeid
                plt.figure(figsize=(8, 6))
                plt.bar(eine, hind, color=["blue", "red"])
                plt.title("Toodete hind")
                plt.xlabel("Toode")
                plt.ylabel("Hind")
                plt.show()
            
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
            arve1=0
            for i in range(len(eine)):
                silt_pwd = ttk.Label(raam, text=(summa[eine[i]],"\u20AC"))
                silt_pwd.place(x=150, y=0+50*i)
                #sõna
                silt_pwd = ttk.Label(raam, text=(eine[i]))
                silt_pwd.place(x=70, y=0+50*i)
                arve1=arve1+summa[eine[i]]
            
            nimi = ttk.Label(raam, text=(arve1,"\u20AC"))
            nimi.place(x=200, y=120, width=150)
            #command
            def arve():
                
                with open("köök.txt", "w", encoding="utf-8") as f:
                    for i in range(len(eine)):
                        f.write(eine[i]+"\n")
                    f.close()
                graafik()
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

         
        #command
        def kohv():
            eine.append("Kohv")
        # loome nupu
        nupp2 = ttk.Button(raam, text="Kohv",command=kohv)  
        nupp2.place(x=70, y=100)

        nimi = ttk.Label(raam, text=(summa["Kohv"],"\u20AC"))
        nimi.place(x=150, y=100, width=150)
        #command
        def coca_cola():
            eine.append("Coca-Cola")
        # loome nupu
        nupp2 = ttk.Button(raam, text="Coca-Cola",command=coca_cola)  
        nupp2.place(x=70, y=150)
        
        nimi = ttk.Label(raam, text=(summa["Coca-Cola"],"\u20AC"))
        nimi.place(x=150, y=150, width=150)
        #command
        def vesi():
            eine.append("Vesi")
        # loome nupu
        nupp2 = ttk.Button(raam, text="Vesi",command=vesi) 
        nupp2.place(x=70, y=200)
        
        nimi = ttk.Label(raam, text=(summa["Vesi"],"\u20AC"))
        nimi.place(x=150, y=200, width=150)
        
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
    nupp2.place(x=70, y=100)

    nimi = ttk.Label(raam, text=(summa["Laste-eine"],"\u20AC"))
    nimi.place(x=150, y=100, width=150)
    #command
    def filee():
        eine.append("Filee")
    # loome nupu
    nupp2 = ttk.Button(raam, text="Filee",command=filee)  
    nupp2.place(x=70, y=150)
    
    nimi = ttk.Label(raam, text=(summa["Filee"],"\u20AC"))
    nimi.place(x=150, y=150, width=150)
    #command
    def supp():
        eine.append("Supp")
    # loome nupu
    nupp2 = ttk.Button(raam, text="Supp",command=supp)  
    nupp2.place(x=70, y=200)
    
    nimi = ttk.Label(raam, text=(summa["Supp"],"\u20AC"))
    nimi.place(x=150, y=200, width=150)
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
