from tkinter import*
import time;
import datetime
import pygame

pygame.init()
root=Tk()
root.title("Piano")
root.geometry('1352x700+0+0')
root.configure(background="white")


ABC=Frame(root,bg="powder blue",bd=20,relief=RIDGE)
ABC.grid()

ABC1=Frame(ABC, bg="powder blue",bd=20,relief=RIDGE)
ABC1.grid()

ABC2=Frame(ABC, bg="powder blue",relief=RIDGE)
ABC2.grid()

ABC3=Frame(ABC, bg="powder blue",relief=RIDGE)
ABC3.grid()

str1 = StringVar()
str1.set("Just Like Music")
Date1=StringVar()
Time1=StringVar()

Date1.set(time.strftime("%d/%m/%y"))
Time1.set(time.strftime("%H:%M:%S"))

#=============================================================================

def value_Cs():
    str1.set("C#")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/C_s.wav")
    sound.play()

def value_Ds():
    str1.set("D#")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/D_s.wav")
    sound.play()

def value_Fs():
    str1.set("F#")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/F_s.wav")
    sound.play()

def value_Gs():
    str1.set("G#")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/G_s.wav")
    sound.play()
    return

def value_Bb():
    str1.set("Bb")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/Bb.wav")
    sound.play()
    return

def value_Cs1():
    str1.set("C#1")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/C_s1.wav")
    sound.play()
    return

def value_Ds1():
    str1.set("D#1")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/D_s1.wav")
    sound.play()
    return

def value_C():
    str1.set("C")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/C.wav")
    sound.play()
    return
    
def value_D():
    str1.set("D")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/D.wav")
    sound.play()
    return

def value_E():
    str1.set("E")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/E.wav")
    sound.play()
    return

def value_F():
    str1.set("F")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/F.wav")
    sound.play()
    return

def value_G():
    str1.set("G")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/G.wav")
    sound.play()
    return

def value_A():
    str1.set("A")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/A.wav")
    sound.play()
    return

def value_B():
    str1.set("B")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/B.wav")
    sound.play()
    return

def value_C1():
    str1.set("C1")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/C1.wav")
    sound.play()
    return

def value_D1():
    str1.set("D1")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/D1.wav")
    sound.play()
    return

    
def value_E1():
    str1.set("E1")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/E1.wav")
    sound.play()
    return

def value_F1():
    str1.set("F1")
    sound = pygame.mixer.Sound("C:/Users/RAJAN SRIVASTAVA/OneDrive/Desktop/Python Programming Classes/Z_Music_Notes/Music_Notes/F1.wav")
    sound.play()
    return



#========================= Label with Title ==================================

Label(ABC1, text="Piano Musical Keys", font=('arial',25,"bold"),padx=8,pady=8,bd=4,
      bg="powder blue",fg="coral",justify=CENTER).grid(row=0,column=0,columnspan=11)



#=============================================================================

txtDate=Entry(ABC1, textvariable=Date1, font=('arial',18,'bold'),bd=18,
bg="powder blue",fg="crimson",width=28,justify=CENTER).grid(row=1,column=0,pady=1)

txtDisplay=Entry(ABC1, textvariable=str1, font=('arial',18,'bold'),bd=18,bg="powder blue",
              fg="crimson",width=28,justify=CENTER).grid(row=1,column=1,pady=1)

txtTime=Entry(ABC1, textvariable=Time1, font=('arial',18,'bold'),bd=18,bg="powder blue",
              fg="crimson",width=28,justify=CENTER).grid(row=1,column=2,pady=1)


#==================== Upper Music Key Notes ==================================

btnCs=Button(ABC2,height=6,width=5,bd=4,text="C#",bg="black",fg="white",font=('arial',18,"bold"),command=value_Cs)
btnCs.grid(row=0,column=0,padx=5,pady=5)

btnDs=Button(ABC2,height=6,width=5,bd=4,text="D#",bg="black",fg="white",font=('arial',18,"bold"),command=value_Ds)
btnDs.grid(row=0,column=2, padx=5, pady=5)
btnSpace2 = Button(ABC2,state=DISABLED,width=2,height=6,bg="powder blue",relief=FLAT)
btnSpace2.grid(row=0,column=3,padx=0,pady=0)
btnFs=Button(ABC2,height=6,width=5,bd=4,text="F#",bg="black",fg="white",font=('arial',18,"bold"),command=value_Fs)
btnFs.grid(row=0,column=4,padx=5,pady=5)

btnGs=Button(ABC2,height=6,width=5,bd=4,text="G#",bg="black",fg="white",font=('arial',18,"bold"),command=value_Gs)
btnGs.grid(row=0,column=6,padx=5,pady=5)


btnBb=Button(ABC2,height=6,width=5,bd=4,text="Bb#",bg="black",fg="white",font=('arial',18,"bold"),command=value_Bb)
btnBb.grid(row=0,column=8,padx=5,pady=5)
btnSpace5 = Button(ABC2,state=DISABLED,width=2,height=6,bg="powder blue",relief=FLAT)
btnSpace5.grid(row=0,column=9,padx=0,pady=0)
btnCs1=Button(ABC2,height=6,width=5,bd=4,text="C#1",bg="black",fg="white",font=('arial',18,"bold"),command=value_Cs1)
btnCs1.grid(row=0,column=10,padx=5,pady=5)


btnDs1=Button(ABC2,height=6,width=5,bd=4,text="D#1",bg="black",fg="white",font=('arial',18,"bold"),command=value_Ds1)
btnDs1.grid(row=0,column=12,padx=5,pady=5)

#======================= Lower Music Key Notes ================================
btnC = Button(ABC3,bd=4,width=5,height=6, text="C",bg="white",fg="black",font=('arial',18,'bold'),command=value_C)
btnC.grid(row=0, column=0, padx=5, pady=5)
btnD = Button(ABC3,bd=4,width=5,height=6, text="D",bg="white",fg="black",font=('arial',18,'bold'),command=value_D)
btnD.grid(row=0, column=1, padx=5, pady=5)
btnE = Button(ABC3,bd=4,width=5,height=6, text="E",bg="white",fg="black",font=('arial',18,'bold'),command=value_E)
btnE.grid(row=0, column=2, padx=5, pady=5)
btnF = Button(ABC3,bd=4,width=5,height=6, text="F",bg="white",fg="black",font=('arial',18,'bold'),command=value_F)
btnF.grid(row=0, column=3, padx=5, pady=5)

btnG = Button(ABC3,bd=4,width=5,height=6, text="G",bg="white",fg="black",font=('arial',18,'bold'),command=value_G)
btnG.grid(row=0, column=4, padx=5, pady=5)
btnA = Button(ABC3,bd=4,width=5,height=6, text="A",bg="white",fg="black",font=('arial',18,'bold'),command=value_A)
btnA.grid(row=0, column=5, padx=5, pady=5)
btnB = Button(ABC3,bd=4,width=5,height=6, text="B",bg="white",fg="black",font=('arial',18,'bold'),command=value_B)
btnB.grid(row=0, column=6, padx=5, pady=5)
btnC1 = Button(ABC3,bd=4,width=5,height=6, text="C1",bg="white",fg="black",font=('arial',18,'bold'),command=value_C1)
btnC1.grid(row=0, column=7, padx=5, pady=5)

btnD1 = Button(ABC3,bd=4,width=5,height=6, text="D1",bg="white",fg="black",font=('arial',18,'bold'),command=value_D1)
btnD1.grid(row=0, column=8, padx=5, pady=5)
btnE1 = Button(ABC3,bd=4,width=5,height=6, text="E1",bg="white",fg="black",font=('arial',18,'bold'),command=value_E1)
btnE1.grid(row=0, column=9, padx=5, pady=5)
btnF1 = Button(ABC3,bd=4,width=5,height=6, text="F1",bg="white",fg="black",font=('arial',18,'bold'),command=value_F1)
btnF1.grid(row=0, column=10, padx=5, pady=5)



#=============================================================================


root.mainloop()






