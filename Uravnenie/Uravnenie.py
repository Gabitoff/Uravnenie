from tkinter import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
def save():#функция сохраняет значения переменных, которые мы ввели в первом окне и закрывает первое окно
    a=float(entA.get())#с помощью float не дадим возможности пользователю ввести текст как значение переменной
    b=float(entB.get())
    c=float(entC.get())
    f=open("abc.txt","w+")#записываем значение в файл, иначе после закрытия первого окна все введённые пользователем значения буду утеряны
    if a==0:#конвертируем значения переменных в текст и записываем в файл, каждое значение на новой строке a,b,c.
        f.write(str("1")+"\n"+str(b)+"\n"+str(c))
    else:
        f.write(str(a)+"\n"+str(b)+"\n"+str(c))
    f.close()
    win.destroy()
    win.quit()

def win2close():
    f2=open("xy.txt","w+")
    if D>0:
        f2.write(str(x0)+"\n"+str(y0)+"\n"+str(x1)+"\n"+str(y1)+"\n"+str(x2)+"\n"+str(y2))
    elif D==0:
        f2.write(str(x0)+"\n"+str(y0)+"\n"+str(x1)+"\n"+str(y1))
    else:
        f2.write(str(x0)+"\n"+str(y0))
    f2.close()
    win2.destroy()
    win2.quit()
    
#открываем первое окно, где вводим значения a,b,c
win=Tk()
win.title("Введите значения уравнения")
win.geometry("500x200")

labelF=Label(win,text="Формула: ax^2+bx+c=0",font="Arial_Bold 15")
labelA=Label(win,text="Введите значение а. При вводе 0 значение будет заменено на 1 автоматически")
entA=Entry(win)
labelB=Label(win,text="Введите значение b")
entB=Entry(win)
labelC=Label(win,text="Введите значение c")
entC=Entry(win)
btn=Button(win,text="Сохранить",font="Arial_Bold 15", command=save)

labelF.pack(side=TOP)
labelA.pack()
entA.pack()
labelB.pack()
entB.pack()
labelC.pack()
entC.pack()
btn.pack(side=BOTTOM)

entA.bind()
entB.bind()
entC.bind()
btn.bind()
win.mainloop()
#конец кода первого окна
#теперь считаем дискриминант и значения, а расчёты выводим во втором окне
f=open("abc.txt","r")#открываем файл, в который мы сохранили значения из первого окна
a=float(f.readline())#считываем значение переменной a из файла и конвертируем его обратно в дробное число
b=float(f.readline())#считываем значение переменной b из файла и конвертируем его обратно в дробное число
c=float(f.readline())#считываем значение переменной c из файла и конвертируем его обратно в дробное число
f.close()
D=b**2-(4*a*c)#считаем дискриминант
win2=Tk()
win2.title("Результаты решения квадратного уравнения")
win2.geometry("500x300")
labelD=Label(win2,text=f"Дискриминант вычисляем по формуле: D=b^2-(4*a*c),\nD={b}^2-(4*{a}*{c})={D}")
labelD.pack()
if D>0:
    sqrtD=D**0.5#вычисляем корень дикриминанта
    x1=(-1*b+sqrtD)/2*a#вычисляем первый корень уровнения
    y1=0
    x2=(-1*b-sqrtD)/2*a#вычисляем второй корень уровнения
    y2=0
    labelZ=Label(win2,text="Значение дискриминанта положительное, уравнение имеет два корня:\n"+str(x1)+" и "+str(x2))
    labelX1=Label(win2,text=f"Первый корень вычислен по формуле: -b+√D/2*a\nx1=-{b}+√{D}/2*{a}")
    labelX2=Label(win2,text=f"Второй корень вычислен по формуле: -b-√D/2*a\nx2=-{b}-√{D}/2*{a}")
    labelZ.pack()
    labelX1.pack()
    labelX2.pack()
    btn2=Button(win2,text="Строим график",font="Arial_Bold 15", command=win2close)
elif D==0:
    sqrtD=D**0.5#вычисляем корень дикриминанта
    x1=(-1*b)/2*a#вычисляем корень уровнения
    y1=0
    labelZ=Label(win2,text="Значение дискриминанта равно нулю, уравнение имеет один корень:\n"+str(x1))
    labelX1=Label(win2,text=f"Корень вычислен по формуле: -b/2*a\nx1=-{b}/2*{a}")
    labelZ.pack()
    labelX1.pack()
    btn2=Button(win2,text="Строим график",font="Arial_Bold 15", command=win2close)
else:
    labelZ=Label(win2,text="Значение дискриминанта отрицательное, у уравнения нет корней")
    labelZ.pack()
    btn2=Button(win2,text="Строим график",font="Arial_Bold 15", command=win2close)
x0=(-1*b)/(2*a)#вычисляем координаты вершины параболы, ось х
y0=a*x0**2+b*x0+c#вычисляем координаты вершины параболы, ось y
labelX0=Label(win2, text=f"Координата X для вершины параболы вычислена по формуле -b/2a:\nx0={-b}/(2*{a})={x0}")
labelY0=Label(win2, text=f"Координата Y для вершины параболы вычислена по формуле ax^2+bx+c:\ny0={a}*{x0**2}+{b}*{x0}+{c}={y0}")

labelX0.pack()
labelY0.pack()

btn2.pack(side=BOTTOM)
btn2.bind()
win2.mainloop()
#конец кода второго окна
#строим график
xrange=[]#список значений x
yrange=[]#список значений y
f2=open("xy.txt","r")#открываем файл, в который мы сохранили значения из первого окна
x0=float(f2.readline())#считываем значение переменной x0 из файла и конвертируем его обратно в дробное число
y0=float(f2.readline())#считываем значение переменной y0 из файла и конвертируем его обратно в дробное число
if D<0:
    for x in range(int(x0)-20,int(x0)+20,1):#строим график параболы отталкиваясь только от координат вершины, т.к. в данном случае пересечения с осью х нет
        y=a*x**2+b*x+c
        xrange.append(x)
        yrange.append(y)
elif D>=0:
    x1=float(f2.readline())#считываем значение переменной x1 из файла и конвертируем его обратно в дробное число
    y1=float(f2.readline())#считываем значение переменной y1 из файла и конвертируем его обратно в дробное число
    if D>0:
        x2=float(f2.readline())#считываем значение переменной x2 из файла и конвертируем его обратно в дробное число
        y2=float(f2.readline())#считываем значение переменной y2 из файла и конвертируем его обратно в дробное число
        for x in range(int(x1)-20,int(x2)+20,1):#строим график параболы отталкиваясь от координат обоих пересечений с осью х
            y=a*x**2+b*x+c
            xrange.append(x)
            yrange.append(y)
    else:
        for x in range(int(x1)-20,int(x1)+20,1):#строим график параболы отталкиваясь только от координат одного пересечени с осью х, т.к. в данном случае вершина лежит на оси х
            y=a*x**2+b*x+c
            xrange.append(x)
            yrange.append(y)
else:
    pass
f2.close()

#for x in range(-10,10,1):
#    y=a*x**2+b*x+c
#    xrange.append(x)
#    yrange.append(y)

fig= plt.figure()
axes=fig.add_subplot(111)
axes.plot(xrange,yrange)
plt.show()

