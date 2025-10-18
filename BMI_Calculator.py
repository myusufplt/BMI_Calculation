from tkinter import *

#EKRAN
Screen = Tk()
Screen.title("BMI CALCULATOR")
Screen.minsize(width=300,height=350)

#Tepe Yazisi
upText = Label(text="BMI Calculator",font=('Arial',20))
upText.pack()
upTextBrother = Label(text="please enter correcty" , font=('Arial',10))
upTextBrother.place(x=80,y=35)

#Kilo Sorma
weightLabel = Label(text="How much do you weight(kg) ?")
weightEntry = Entry()
weightLabel.place(x=50,y=70)
weightEntry.place(x=50, y=90)

#Boy Sorma
heightLabel = Label(text="How tall(cm) are you?")
heightEntry = Entry()
heightLabel.place(x=50 ,y=130)
heightEntry.place(x=50, y=150)

exceptLabel = None
fatLabel = None
errorLabel = None

def calculator():
    global exceptLabel, fatLabel, errorLabel
    if exceptLabel:
        exceptLabel.destroy()
    if fatLabel:
        fatLabel.destroy()
    if errorLabel:
        errorLabel.destroy()

    try:
        kilo = float( weightEntry.get() )
        boy = float( heightEntry.get() ) / 100
        if boy <= 0 or kilo <= 0:
            raise ValueError
        math = kilo/(boy*boy)
        exceptLabel = Label(text=f"Your BMI = {math: .2f}")
        exceptLabel.place(x=90,y=240)

        if math <= 18.4:
            fat = "Under Weight"
        elif 18.5<=math<=24.9:
            fat = "Normal"
        elif 25<=math <=29.9:
            fat = "Overweight"
        elif 30<=math<=34.9:
            fat = "Obese"
        elif 35<=math:
            fat = "Extreme Obese"
        elif math<=0:
            fat = "Please dont use negative numbers"
        else:
            fat = "? error ?"
        fatLabel = Label(text=fat)
        fatLabel.place(x=100,y=260)
    except ValueError:
        errorLabel = Label(text=("!! Please Enter A Number !!"))
        errorLabel.place(x=60,y=240)

#Hesaplama Tusu
calculatorButton = Button(text="Calculator", command=calculator)
calculatorButton.place(x=100,y=200)

Screen.mainloop()