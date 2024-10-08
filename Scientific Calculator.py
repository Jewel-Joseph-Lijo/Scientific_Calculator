from tkinter import *
import math

result=False
def sevenclick():
    global result
    if result==True:
        text_input.set('7')
        result=False
    else:
        text_input.set(text_input.get()+'7')

def eightclick():
    global result
    if result==True:
        text_input.set('8')
        result=False
    else:
        text_input.set(text_input.get()+'8')

def nineclick():
    global result
    if result==True:
        text_input.set('9')
        result=False
    else:
        text_input.set(text_input.get()+'9')                

def fourclick():
    global result
    if result==True:
        text_input.set('4')
        result=False
    else:
        text_input.set(text_input.get()+'4')

def fiveclick():
    global result
    if result==True:
        text_input.set('5')
        result=False
    else:
        text_input.set(text_input.get()+'5')

def sixclick():
    global result
    if result==True:
        text_input.set('6')
        result=False
    else:
        text_input.set(text_input.get()+'6')                

def oneclick():
    global result
    if result==True:
        text_input.set('1')
        result=False
    else:
        text_input.set(text_input.get()+'1')

def twoclick():
    global result
    if result==True:
        text_input.set('2')
        result=False
    else:
        text_input.set(text_input.get()+'2')

def threeclick():
    global result
    if result==True:
        text_input.set('3')
        result=False
    else:
        text_input.set(text_input.get()+'3')

def zeroclick():
    global result
    if result==True:
        text_input.set('0')
        result=False
    else:
        text_input.set(text_input.get()+'0') 

def pointclick():
    global result
    if result==True:
        text_input.set('.')
        result=False
    else:
        text_input.set(text_input.get()+'.')

def plusclick():
    global result
    if text_input.get()=='':
        text_input.set('')
    else:
        text_input.set(text_input.get()+'+')
        result=False

def minusclick():
    global result
    text_input.set(text_input.get()+'-')  
    result=False

def mulclick():
    global result
    if text_input.get()=='':
        text_input.set('')
    else:
        text_input.set(text_input.get()+'x')
        result=False

def divclick():
    global result
    if text_input.get()=='':
        text_input.set('')
    else:
        text_input.set(text_input.get()+'÷')
        result=False

def equalclick():
    global result
    result_text=text_input.get()
    result_text1=result_text.replace('x','*')
    result_text2=result_text1.replace('÷','/')
    result_text3=result_text2.replace('^','**')
    result_text4=eval(result_text3)
    text_input.set(result_text4)
    result=True

def clearclick():
    text_input.set('')

def delclick():
    L1=list(text_input.get())
    del L1[len(L1)-1]
    str1=""
    for i in L1:
        str1+=i
    text_input.set(str1) 

def modclick():
    global result
    modulus=text_input.get().replace('÷','%')
    reminder=eval(modulus)
    text_input.set(reminder)
    result=True

def piclick():
    global result
    if result==True:
        text_input.set('3.14')
        result=False
    else:
        text_input.set(text_input.get()+'3.14')

def exclick():
    global result
    ex_result=math.exp(eval(text_input.get()))
    text_input.set(ex_result)
    result=True   

def log10clicked():
    global result
    log_10=math.log10(eval(text_input.get()))
    text_input.set(log_10)
    result=True

def logclicked():
    global result
    log_e=math.log(eval(text_input.get()))
    text_input.set(log_e)
    result=True

def sinclick():
    global result
    sinval=math.sin(eval(text_input.get()))
    text_input.set(sinval)
    result=True

def cosclick():
    global result
    cosval=math.cos(eval(text_input.get()))
    text_input.set(cosval)
    result=True

def tanclick():
    global result
    tanval=math.tan(eval(text_input.get())) 
    text_input.set(tanval)
    result=True

def cotclick():
    global result
    sinval=math.sin(eval(text_input.get()))
    cosval=math.cos(eval(text_input.get()))
    cotval=cosval/sinval
    text_input.set(cosval)
    result=True        

def cosecclick():
    global result
    sinval=math.sin(eval(text_input.get()))
    cosecval=1/sinval
    text_input.set(cosecval)
    result=True

def secclick():
    global result
    cosval=math.cos(eval(text_input.get()))
    secval=1/cosval
    text_input.set(secval)
    result=True 

def squareclick():
    global result
    val=eval(text_input.get())
    square=math.pow(val,2)
    text_input.set(square)
    result=True

def cubeclick():
    global result
    val=eval(text_input.get())
    cube=math.pow(val,3)
    text_input.set(cube)
    result=True   

def inv_powerclick():
    global result
    val=eval(text_input.get())
    inv_power=math.pow(val,-1)
    text_input.set(inv_power)
    result=True

def factclick():
    global result
    val=eval(text_input.get())
    fact=math.factorial(val)
    text_input.set(fact)
    result=True

def left_parclick():
    global result
    if result==True:
        text_input.set('(')
        result=False
    else:
        text_input.set(text_input.get()+'(') 

def right_parclick():
    global result
    if result==True:
        text_input.set(')')
        result=False
    else:
        text_input.set(text_input.get()+')') 

def sqrtclick():
    global result
    val=eval(text_input.get())
    SR=math.sqrt(val)
    text_input.set(SR)
    result=True

def cbrtclick():
    global result
    val=eval(text_input.get())
    CR=math.cbrt(val)
    text_input.set(CR)
    result=True 

def powerclick():
    global result
    if text_input.get()=='':
        text_input.set('')
    else:
        text_input.set(text_input.get()+'^')
        result=False       

window=Tk()
window.geometry("447x568")
window.title("Scientific Calculator")
window.configure(bg="black")

text_input = StringVar()
display_screen = Entry(window, font=('sans-serif', 20, 'bold'), textvariable=text_input,bd=5, insertwidth=2, bg='white', justify='right').grid(columnspan=5, padx = 10, pady = 15)

button_additional = {'bd':5, 'fg':'white', 'bg':'green', 'font':('sans-serif', 20, 'bold')}
button_main = {'bd':5, 'fg':'#000', 'bg':'yellow', 'font':('sans-serif', 20, 'bold')}

modbutton = Button(window, button_additional, text='mod',command=modclick).grid(row=1, column=0, sticky="nsew")
pibutton = Button(window, button_additional, text='π',command=piclick).grid(row=1, column=1, sticky="nsew")
exbutton = Button(window, button_additional, text='e^x',command=exclick).grid(row=1, column=2, sticky="nsew")
log_base10button = Button(window, button_additional, text='log\u2081\u2080',font=('sans-serif', 16, 'bold'),command=log10clicked).grid(row=1, column=3, sticky="nsew")
log_baseebutton = Button(window, button_additional, text=' log  ',command=logclicked).grid(row=1, column=4, sticky="nsew")

sinbutton = Button(window, button_additional, text='sin',command=sinclick).grid(row=2, column=0, sticky="nsew")
cosbutton = Button(window, button_additional, text='cos',command=cosclick).grid(row=2, column=1, sticky="nsew")
tanbutton = Button(window, button_additional, text='tan',command=tanclick).grid(row=2, column=2, sticky="nsew")
cotbutton = Button(window, button_additional, text='cot',command=cotclick).grid(row=2, column=3, sticky="nsew")
cosecbutton = Button(window, button_additional, text='cosec',command=cosecclick).grid(row=2, column=4, sticky="nsew")

secbutton = Button(window, button_additional, text='sec',command=secclick).grid(row=3, column=0, sticky="nsew")
squarebutton= Button(window, button_additional, text='x\u00B2',command=squareclick).grid(row=3, column=1, sticky="nsew")
cubebutton= Button(window, button_additional, text='x\u00B3',command=cubeclick).grid(row=3, column=2, sticky="nsew")
inv_powerbutton = Button(window, button_additional, text='x\u207b\xb9',command=inv_powerclick).grid(row=3, column=3, sticky="nsew")
factorialbutton = Button(window, button_additional, text='X!',command=factclick).grid(row=3, column=4, sticky="nsew")

left_parbutton = Button(window, button_additional, text='(',command=left_parclick).grid(row=4, column=0, sticky="nsew")
right_parbutton = Button(window, button_additional, text=')',command=right_parclick).grid(row=4, column=1, sticky="nsew")   
sqrtbutton = Button(window, button_additional, text='\u221A',command=sqrtclick).grid(row=4, column=2, sticky="nsew")
cbrtbutton = Button(window, button_additional, text='\u00B3\u221A',command=cbrtclick).grid(row=4, column=3, sticky="nsew")
powerbutton = Button(window, button_additional, text='^',command=powerclick).grid(row=4, column=4, sticky="nsew")

sevenbutton = Button(window, button_main, text='7',command=sevenclick).grid(row=5, column=0, sticky="nsew")
eightbutton = Button(window, button_main, text='8',command=eightclick).grid(row=5, column=1, sticky="nsew")
ninebutton = Button(window, button_main, text='9',command=nineclick).grid(row=5, column=2, sticky="nsew")
mulbutton = Button(window, button_main, text='x',command=mulclick).grid(row=5, column=3, sticky="nsew")
divbutton = Button(window, button_main, text='÷',command=divclick).grid(row=5, column=4, sticky="nsew")

fourbutton = Button(window, button_main, text='4',command=fourclick).grid(row=6, column=0, sticky="nsew")
fivebutton = Button(window, button_main, text='5',command=fiveclick).grid(row=6, column=1, sticky="nsew")
sixbutton = Button(window, button_main, text='6',command=sixclick).grid(row=6, column=2, sticky="nsew")
plusbutton = Button(window, button_main, text='+',command=plusclick).grid(row=6, column=3, sticky="nsew")
minusbutton = Button(window, button_main, text='-',command=minusclick).grid(row=6, column=4, sticky="nsew")

onebutton = Button(window, button_main, text='1',command=oneclick).grid(row=7, column=0, sticky="nsew")
twobutton= Button(window, button_main, text='2',command=twoclick).grid(row=7, column=1, sticky="nsew")
threebutton = Button(window, button_main, text='3',command=threeclick).grid(row=7, column=2, sticky="nsew")
equalbutton = Button(window, button_main, text='=',command=equalclick).grid(row=7,columnspan=2,column=3, sticky="nsew")

zerobutton = Button(window, button_main, text='0',command=zeroclick).grid(row=8, column=0, sticky="nsew")
pointbutton = Button(window, button_main, text='.',command=pointclick).grid(row=8, column=1, sticky="nsew")
delbutton = Button(window, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),text='DEL',bg='orange',command=delclick).grid(row=8, column=2, sticky="nsew")
clearbutton = Button(window, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),text='Clear', bg='orange',command=clearclick).grid(row=8, column=3,columnspan=2, sticky="nsew")


window.mainloop()