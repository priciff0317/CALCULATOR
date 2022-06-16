
import tkinter
import math 
from decimal import *


#calcular frame

cframe = tkinter.Tk()

cframe.title("Calculator")

cframe.geometry("550x550")

cframe.resizable(0,0)

output = ""
output2 = ' '
fnum = 0

open_button = 0

counter = 0
tempory_plus = 0
tempory_multiply = 1
tempory_subtract = 0
tempory_division = 1

plus_open = 0
subtract_open = 0
multiply_open = 0
division_open = 0
equal_open = 0
calulate_open = 0

zero_open = 0

point_open = False

operator = " "

flash_zero = 0


# calcular click 

def insert0():

    tx.configure(state = "normal")

    btn10.configure(state = "normal")
    btn12.configure(state = "normal")
    btn11.configure(state = "normal")
    btn13.configure(state = "normal")

    global plus_open
    global subtract_open
    global multiply_open
    global division_open
    global calulate_open

    global equal_open

    global zero_open

    global point_open

    global flash_zero

    point_open = True


    calulate_open = 1

    flash_zero += 1


 
    if plus_open == 1 or subtract_open == 1 or multiply_open == 1 or division_open == 1:

        tx.delete(0.0 , "end" )

        if zero_open == 0:
            
            tx.insert('end','0')
            btn14.configure(state = "disable")
        elif point_open == True:

            tx.insert('end', '0')

        plus_open = 0
        subtract_open = 0
        multiply_open = 0
        division_open = 0
    else:

        reflash()

        if zero_open == 0:
             
            tx.insert('end','0')

            btn14.configure(state = "disable")
        else:

            tx.insert('end', '0')


     
    
    tx.configure(state = "disable")

def insert1():
    
    tx.configure(state = "normal")

    btn10.configure(state = "normal")
    btn12.configure(state = "normal")
    btn11.configure(state = "normal")
    btn13.configure(state = "normal")

    global plus_open
    global subtract_open
    global multiply_open
    global division_open
    global calulate_open

    global equal_open

    global zero_open

    global point_open

    global flash_zero

    calulate_open = 1

    zero_open = 1

    point_open = True


    btn14.configure(state = "normal")

    if plus_open == 1 or subtract_open == 1 or multiply_open ==1 or division_open == 1:

        tx.delete(0.0 , "end" )

        tx.insert('end','1')

        plus_open = 0
        subtract_open = 0
        multiply_open = 0
        division_open = 0
    elif  flash_zero == 1 :
        tx.delete(0.0,  "end")

        flash_zero -= 999999999999

        tx.insert('end', '1')
    
        
    else:
        reflash()

        flash_zero -= 999999999999

        tx.insert('end','1')
    

    tx.configure(state = "disable")

def insert2():

    tx.configure(state = "normal")

    btn10.configure(state = "normal")
    btn12.configure(state = "normal")
    btn11.configure(state = "normal")
    btn13.configure(state = "normal")

    global plus_open
    global subtract_open
    global multiply_open
    global division_open
    global calulate_open

    global equal_open

    global zero_open

    global point_open

    global flash_zero

    calulate_open = 1

    zero_open = 1

    point_open = True

    btn14.configure(state = "normal")

    if plus_open == 1 or subtract_open == 1 or multiply_open ==1 or division_open == 1:

        tx.delete(0.0 , "end" )

        tx.insert('end','2')

        plus_open = 0
        subtract_open = 0
        multiply_open = 0
        division_open = 0
    elif flash_zero == 1:

        tx.delete(0.0, "end")

        flash_zero -= 99999999

        tx.insert('end', '2')

    else:

        reflash()

        flash_zero -= 99999999

        tx.insert('end','2')

    tx.configure(state = "disable")

def insert3():

    tx.configure(state = "normal")

    btn10.configure(state = "normal")
    btn12.configure(state = "normal")
    btn11.configure(state = "normal")
    btn13.configure(state = "normal")

    global plus_open
    global subtract_open
    global multiply_open
    global division_open
    global calulate_open

    global equal_open

    global zero_open

    global point_open

    global flash_zero

    calulate_open = 1

    zero_open = 1

    point_open = True

    btn14.configure(state = "normal")

    if plus_open == 1 or subtract_open == 1 or multiply_open ==1 or division_open == 1:

        tx.delete(0.0 , "end" )

        tx.insert('end','3')

        plus_open = 0
        subtract_open = 0
        multiply_open = 0
        division_open = 0
    elif flash_zero == 1:
        
        tx.delete(0.0, "end")

        flash_zero -= 99999999

        tx.insert('end', '3')


    else:

        reflash()

        flash_zero -= 99999999

        tx.insert('end','3')

    tx.configure(state = "disable")


def insert4():

    tx.configure(state = "normal")

    btn10.configure(state = "normal")
    btn12.configure(state = "normal")
    btn11.configure(state = "normal")
    btn13.configure(state = "normal")

    global plus_open
    global subtract_open
    global multiply_open
    global division_open
    global calulate_open

    global equal_open

    global zero_open

    global point_open

    global flash_zero

    calulate_open = 1

    zero_open = 1

    point_open = True

    btn14.configure(state = "normal")

    if plus_open == 1 or subtract_open == 1 or multiply_open ==1 or division_open == 1:

        tx.delete(0.0 , "end" )

        tx.insert('end','4')

        plus_open = 0
        subtract_open = 0
        multiply_open = 0
        division_open = 0
    elif flash_zero == 1:

        tx.delete(0.0,"end")

        flash_zero  -= 99999999

        tx.insert('end', '4')

    else:

        reflash()

        flash_zero -= 99999999

        tx.insert('end','4')

    tx.configure(state = "disable")

def insert5():

    tx.configure(state = "normal")

    btn10.configure(state = "normal")
    btn12.configure(state = "normal")
    btn11.configure(state = "normal")
    btn13.configure(state = "normal")

    global plus_open
    global subtract_open
    global multiply_open
    global division_open
    global calulate_open

    global equal_open

    global zero_open

    global point_open

    global flash_zero

    calulate_open = 1

    zero_open = 1

    point_open = True

    btn14.configure(state="normal")

    if plus_open == 1 or subtract_open == 1 or multiply_open ==1 or division_open == 1:

        tx.delete(0.0 , "end" )

        tx.insert('end','5')

        plus_open = 0
        subtract_open = 0
        multiply_open = 0
        division_open = 0
    elif flash_zero == 1:

        tx.delete(0.0, "end")
        
        flash_zero -= 99999999

        tx.insert('end', '5')

    else:

        reflash()

        flash_zero -= 99999999

        tx.insert('end','5')

    tx.configure(state = "disable")

def insert6():

    tx.configure(state = "normal")

    btn10.configure(state = "normal")
    btn12.configure(state = "normal")
    btn11.configure(state = "normal")
    btn13.configure(state = "normal")

    global plus_open
    global subtract_open
    global multiply_open
    global division_open
    global calulate_open

    global equal_open

    global zero_open

    global point_open

    global flash_zero

    calulate_open = 1

    zero_open = 1

    point_open = True

    btn14.configure(state = "normal")

    if plus_open == 1 or subtract_open == 1 or multiply_open ==1 or division_open == 1:

        tx.delete(0.0 , "end" )

        tx.insert('end','6')

        plus_open = 0
        subtract_open = 0
        multiply_open = 0
        division_open = 0
    elif flash_zero == 1:
        
        tx.delete(0.0,"end")

        flash_zero -= 99999999

        tx.insert('end', '6')
    else:

        reflash()

        flash_zero -= 99999999

        tx.insert('end','6')

    tx.configure(state = "disable")

def insert7():

    tx.configure(state = "normal")

    btn10.configure(state = "normal")
    btn12.configure(state = "normal")
    btn11.configure(state = "normal")
    btn13.configure(state = "normal")

    global plus_open
    global subtract_open
    global multiply_open
    global division_open
    global calulate_open

    global equal_open

    global zero_open

    global point_open

    global flash_zero

    calulate_open = 1

    zero_open = 1

    point_open = True

    btn14.configure(state = "normal")

    if plus_open == 1 or subtract_open == 1 or multiply_open ==1 or division_open == 1:

        tx.delete(0.0 , "end" )

        tx.insert('end','7')

        plus_open = 0
        subtract_open = 0
        multiply_open = 0
        division_open = 0
    elif flash_zero == 1:

        tx.delete(0.0,"end")

        flash_zero -= 99999999

        tx.insert('end', '7')
    else:

        reflash()

        flash_zero -= 99999999

        tx.insert('end','7')

    tx.configure(state = "disable")

def insert8():

    tx.configure(state = "normal")

    btn10.configure(state = "normal")
    btn12.configure(state = "normal")
    btn11.configure(state = "normal")
    btn13.configure(state = "normal")

    global plus_open
    global subtract_open
    global multiply_open
    global division_open
    global calulate_open

    global equal_open

    global zero_open

    global point_open

    global flash_zero

    calulate_open = 1

    zero_open = 1

    point_open = True

    btn14.configure(state = "normal")

    if plus_open == 1 or subtract_open == 1 or multiply_open ==1 or division_open == 1:

        tx.delete(0.0 , "end" )

        tx.insert('end','8')

        plus_open = 0
        subtract_open = 0
        multiply_open = 0
        division_open = 0
    elif flash_zero == 1:

        tx.delete(0.0,"end")

        flash_zero -= 9999999

        tx.insert('end','8')
    else:

        reflash()

        flash_zero -= 99999999

        tx.insert('end','8')

    tx.configure(state = "disable")

def insert9():

    tx.configure(state = "normal")

    btn10.configure(state = "normal")
    btn12.configure(state = "normal")
    btn11.configure(state = "normal")
    btn13.configure(state = "normal")

    global plus_open
    global subtract_open
    global multiply_open
    global division_open
    global calulate_open

    global equal_open

    global zero_open

    global point_open

    global flash_zero

    calulate_open = 1

    zero_open = 1

    point_open = True

    btn14.configure(state = "normal")

    if plus_open == 1 or subtract_open == 1 or multiply_open ==1 or division_open == 1:

        tx.delete(0.0 , "end" )

        tx.insert('end','9')

        plus_open = 0
        subtract_open = 0
        multiply_open = 0
        division_open = 0
    elif flash_zero == 1:

        tx.delete(0.0,"end")

        flash_zero -= 99999999

        tx.insert('end', '9')

    else:

        reflash()

        flash_zero -= 99999999

        tx.insert('end','9')

    tx.configure(state = "disable")

def point():

    tx.configure(state = "normal")

    global zero_open 

    global point_open

    global flash_zero

    btn14.configure(state = "normal")

    zero_open = 1

    flash_zero -= 9999999

    if point_open == True:

        tx.insert('end','.')
        btn16.configure(state = "disable")

    tx.configure(state = "disable")


# calcular operator

def plus():

    tx.configure(state = "normal")

    btn12.configure(state = "disable")
    btn11.configure(state = "disable")
    btn13.configure(state = "disable")


    firstnum = tx.get(0.0 , "end")

    global fnum
    global operator
    global plus_open
    global calulate_open
    global equal_open

    global counter
    global tempory_plus
    global tempory_multiply
    global tempory_subtract
    global tempory_division

    global zero_open

    global point_open

    global flash_zero

    global output2

    counter+=1

    zero_open = 0

    point_open = False

    flash_zero = 0


    btn16.configure(state = "normal")

    if operator == "multiply":

        calulate_open = 1
        fnum = tempory_multiply * float(firstnum)
        tempory_plus = 0
    elif operator == "subtract":

        calulate_open = 1
        fnum = tempory_subtract - float(firstnum)
        tempory_plus = 0
    elif operator == "division":

        calulate_open = 1
        try:
            fnum = tempory_division / float(firstnum)
        except ZeroDivisionError:
            output2 = "錯誤"

        tempory_plus = 0
           
    else:
        fnum = float(firstnum)


    if calulate_open == 1:

       tempory_plus = fnum + tempory_plus

       equal_open = 1
       calulate_open = 0

       if counter >= 2:

           if math.trunc(tempory_plus) == tempory_plus:

                tx.delete(0.0, "end")

                tx.insert(0.0, int(tempory_plus), "end")
           else:
                tx.delete(0.0, "end")

                tx.insert(0.0, math.floor(tempory_plus*1000000000000000000)/1000000000000000000, "end") 

           if output2 == "錯誤":
               tx.delete(0.0, "end")
               tx.insert(0.0, output2, "end")
               btn1.configure(state = "disable")
               btn2.configure(state = "disable")
               btn3.configure(state = "disable")
               btn4.configure(state = "disable")
               btn5.configure(state = "disable")
               btn6.configure(state = "disable")
               btn7.configure(state = "disable")
               btn8.configure(state = "disable")
               btn9.configure(state = "disable")
                

                
        

    operator = "plus"
    plus_open = 1

    

    tx.configure(state = "disable")


    
def subtract():

    tx.configure(state = "normal")

    btn12.configure(state = "disable")
    btn10.configure(state = "disable")
    btn13.configure(state = "disable")
    
    firstnum = float(tx.get(0.0 , "end"))

    global fnum
    global operator
    global subtract_open
    global calulate_open
    global equal_open
    
    global counter
    global tempory_subtract
    global tempory_plus
    global tempory_multiply
    global tempory_division


    global zero_open

    global point_open
    
    global flash_zero

    global output2

    counter+=1

    zero_open = 0

    point_open = False

    flash_zero = 0

    btn16.configure(state = "normal")

    if operator == "plus":

        calulate_open = 1
        fnum = -(float(firstnum) + tempory_plus)
        tempory_subtract = 0

    elif operator == "multiply":

        calulate_open = 1
        fnum = -(tempory_multiply * float(firstnum))
        tempory_subtract = 0

    elif operator == "division":

        calulate_open = 1
        try:
            fnum  = -(tempory_division / float(firstnum))
        except ZeroDivisionError:
            output2 = "錯誤"

        tempory_subtract = 0

    else:
        fnum = float(firstnum)
        

    if counter == 1:

        tempory_subtract = fnum - tempory_subtract

    if calulate_open ==1:

       equal_open = 1
       calulate_open = 0

       if counter >= 2:

           tempory_subtract = tempory_subtract - fnum

           if math.trunc(tempory_subtract) == tempory_subtract:

               tx.delete(0.0, "end")

               tx.insert(0.0, int(tempory_subtract), "end")
           else:

               tx.delete(0.0, "end")

               tx.insert(0.0, math.floor(tempory_subtract*1000000000000000000)/1000000000000000000, "end")

           if output2 == "錯誤":
               tx.delete(0.0,"end")
               tx.insert(0.0,output2)
               btn1.configure(state = "disable")
               btn2.configure(state = "disable")
               btn3.configure(state = "disable")
               btn4.configure(state = "disable")
               btn5.configure(state = "disable")
               btn6.configure(state = "disable")
               btn7.configure(state = "disable")
               btn8.configure(state = "disable")
               btn9.configure(state = "disable")

               

    operator = "subtract"
    subtract_open = 1

    tx.configure(state = "disable")


def mutiply():

    tx.configure(state = "normal")

    btn11.configure(state = "disable")
    btn10.configure(state = "disable")
    btn13.configure(state = "disable")
    
    firstnum = tx.get(0.0 , "end")

    global fnum
    global operator
    global multiply_open
    global calulate_open
    global equal_open

    global counter
    global tempory_multiply
    global tempory_plus
    global tempory_subtract
    global tempory_division

    global zero_open

    global point_open

    global flash_zero

    global output2


    counter+=1

    zero_open = 0

    point_open = False

    flash_zero = 0

    btn16.configure(state = "normal")

    if operator == "plus":

        calulate_open = 1
        fnum = float(firstnum) + tempory_plus
        tempory_multiply = 1

    elif operator == "subtract":
        calulate_open = 1
        fnum =  tempory_subtract - float(firstnum)
        tempory_multiply = 1

    elif operator =="division":
        calulate_open = 1
        try:
            fnum =  tempory_division / float(firstnum)
        except ZeroDivisionError:
            output2 = "錯誤"
            

        tempory_multiply = 1

    else:
        if calulate_open == 1:

            fnum = float(firstnum)



    if calulate_open ==1:

       tempory_multiply = fnum * tempory_multiply

       equal_open = 1
       calulate_open = 0

       if counter >= 2:


           if math.trunc(tempory_multiply) == tempory_multiply:

                tx.delete(0.0, "end")

                tx.insert(0.0, int(tempory_multiply), "end")
           else:
                tx.delete(0.0, "end")

                tx.insert(0.0, math.floor(tempory_multiply*1000000000000000000)/1000000000000000000, "end")
           if output2 == "錯誤":
                tx.delete(0.0, "end")
                tx.insert(0.0,output2)
                btn1.configure(state = "disable")
                btn2.configure(state = "disable")
                btn3.configure(state = "disable")
                btn4.configure(state = "disable")
                btn5.configure(state = "disable")
                btn6.configure(state = "disable")
                btn7.configure(state = "disable")
                btn8.configure(state = "disable")
                btn9.configure(state = "disable")

    operator = "multiply"
    multiply_open = 1

    tx.configure(state = "disable")


def division():
    
    tx.configure(state = "normal")

    btn11.configure(state = "disable")
    btn10.configure(state = "disable")
    btn12.configure(state = "disable")
    
    firstnum = tx.get(0.0 , "end")

    global fnum
    global operator
    global division_open
    global calulate_open
    global equal_open

    global counter
    global tempory_division
    global tempory_plus
    global tempory_subtract
    global tempory_multiply

    global zero_open

    global point_open

    global flash_zero

    global output2

    counter += 1

    zero_open = 0

    point_open = False

    flash_zero = 0 

    if operator == "plus":

        calulate_open = 1
        fnum = 1/(float(firstnum) + tempory_plus)  
        tempory_division = 1     
    elif operator == "multiply":

        calulate_open = 1
        fnum = 1/(tempory_multiply * float(firstnum))
        tempory_division = 1
    elif operator == "subtract":

        calulate_open = 1
        fnum = 1/(-(float(firstnum) - tempory_subtract))
        tempory_division = 1

    else:
        if calulate_open ==1:

            fnum = float(firstnum)



    btn16.configure(state = "normal")

    if counter == 1:

        tempory_division = fnum / tempory_division
  
    if calulate_open ==1:

       equal_open = 1
       calulate_open = 0
                
       if counter >= 2:

           try:
               tempory_division = tempory_division / fnum
           except:
               
               output2 = "錯誤"


           if math.trunc(tempory_division) == tempory_division:

                tx.delete(0.0, "end")

                tx.insert(0.0, int(tempory_division), "end")
           else:

                tx.delete(0.0, "end")

                tx.insert(0.0, math.floor(tempory_division*1000000000000000000)/1000000000000000000, "end") 
            
           if output2 == '錯誤' and fnum == 0:

                tx.delete(0.0, 'end') 
                tx.insert(0.0,output2,'end')
                btn1.configure(state = "disable")
                btn2.configure(state = "disable")
                btn3.configure(state = "disable")
                btn4.configure(state = "disable")
                btn5.configure(state = "disable")
                btn6.configure(state = "disable")
                btn7.configure(state = "disable")
                btn8.configure(state = "disable")
                btn9.configure(state = "disable")
                   
                
    operator = "division"
    division_open = 1

    tx.configure(state = "disable")


# display calculator

def display():

    tx.configure(state = "normal")
    

    global operator
    global equal_open
    global counter
    global fnum
    global tempory_plus
    global tempory_multiply
    global tempory_division
    global tempory_subtract

    global point_open

    global zero_open

    global flash_zero

    global output2

      
    secondnum = tx.get(0.0 , "end")

    btn16.configure(state = "normal")

    point_open = False


    if equal_open == 1:

        

        if operator == "plus":

            tx.delete(0.0 , "end")

            total2 = tempory_plus + float(secondnum)

            if math.trunc(total2) == total2 :

               tx.insert( 0.0, int(total2 ) ,"end")

            else:

               tx.insert( 0.0, math.floor(total2*1000000000000000000)/1000000000000000000,"end")


        if operator == "subtract":

            tx.delete(0.0 , "end")

            total3 = tempory_subtract - float(secondnum)

            if math.trunc(total3) == total3:

               tx.insert( 0.0, int(total3 ) ,"end")

            else:

               tx.insert( 0.0, math.floor(total3*10000000000000000)/10000000000000000 ,"end")



        if operator == "multiply":

            tx.delete(0.0 , "end")

            total4 = tempory_multiply * float(secondnum)

            if math.trunc(total4) == total4:

               tx.insert( 0.0, int(total4 ) ,"end")

            else:

               tx.insert( 0.0,  math.floor(total4*100000000000000000)/100000000000000000 ,"end")

        
        if operator == "division":

            tx.delete(0.0 , "end")

            try:

                global total

                total = 0

                total = tempory_division / float(secondnum)

            except:
                output2 = "錯誤"
                tx.insert(0.0 , output2 , "end")
                tx.configure(state = "disable")

                btn11.configure(state = "disable")
                btn13.configure(state = "disable")
                btn10.configure(state = "disable")
                btn12.configure(state = "disable")





    
            if math.trunc(total) == total:

                tx.insert(0.0 , int(total), "end")

            else:

                tx.insert(0.0 , math.floor(total*100000000000000000)/100000000000000000 , "end")

        fnum = 0        

        equal_open = 0
        counter = 0
        tempory_multiply = 1
        tempory_plus = 0
        tempory_subtract = 0
        tempory_division = 1
        operator = " "

        zero_open = 0

        flash_zero = 0
        

    tx.configure(state = "disable")


# clear num

def clear_all_num():

    global fnum 
    global tempory_plus
    global tempory_multiply
    global tempory_subtract

    global tempory_division
    global counter

    global operator

    global zero_open

    global point_open

    global flash_zero

    global output2

    zero_open = 0

    point_open = False

    flash_zero = 0

    output2 = ""

    btn16.configure(state = "normal")

    btn14.configure(state = "normal")

    tx.configure(state = "normal")

    btn10.configure(state = "disable")
    btn12.configure(state = "disable")
    btn11.configure(state = "disable")
    btn13.configure(state = "disable")

    btn1.configure(state = "normal")
    btn2.configure(state = "normal")
    btn3.configure(state = "normal")
    btn4.configure(state = "normal")
    btn5.configure(state = "normal")
    btn6.configure(state = "normal")
    btn7.configure(state = "normal")
    btn8.configure(state = "normal")
    btn9.configure(state = "normal")

    tx.delete(0.0 , "end")
    



    fnum = 0
    tempory_multiply = 1
    tempory_plus = 0
    tempory_subtract = 0

    tempory_division = 1

    counter = 0


    operator = " "

    tx.configure(state = "disable")


def reflash():

    #global output2
    global equal_open

    if equal_open == 0 :

        equal_open = 1

        tx.delete(0.0, "end")

  

# calcular button

btn1 = tkinter.Button( text="1")

btn1.config(width = 11 , height = 6 , command = insert1 )

btn1.grid( row = 3, column = 0 )


btn2 =tkinter.Button( text="2")

btn2.config(width = 11, height = 6, command = insert2)

btn2.grid( row = 3, column = 1 )


btn3 =tkinter.Button( text="3")

btn3.config(width = 11, height = 6 , command = insert3)

btn3.grid( row = 3, column = 2)


btn4 =tkinter.Button( text="4")

btn4.config(width = 11, height = 6, command = insert4)

btn4.grid( row =2, column = 0) 


btn5 =tkinter.Button( text="5")

btn5.config(width = 11, height = 6, command = insert5)

btn5.grid( row =2, column = 1) 


btn6 =tkinter.Button( text="6")

btn6.config(width = 11, height = 6 , command = insert6)

btn6.grid( row =2, column = 2) 


btn7 =tkinter.Button( text="7")

btn7.config(width = 11, height = 6, command = insert7)

btn7.grid( row =1, column = 0) 


btn8 =tkinter.Button( text="8")

btn8.config(width = 11, height = 6 , command = insert8)

btn8.grid( row =1, column = 1) 


btn9 =tkinter.Button( text="9")

btn9.config(width = 11, height = 6 , command = insert9)

btn9.grid( row =1, column = 2) 

btn14 =tkinter.Button( text="0" , command = insert0 )

btn14.config(width = 11, height = 6)

btn14.grid( row =4, column = 0 ) 

btn16 =tkinter.Button( text="." , command = point )

btn16.config(width = 11, height = 6)

btn16.grid( row =4, column = 1 )

btn13 =tkinter.Button( text="AC")

btn13.config(width = 10, height = 6 , command = clear_all_num)

btn13.grid( row =4, column = 3 ) 

btn15 =tkinter.Button( text="=")

btn15.config(width = 11, height = 6 , command = display)

btn15.grid( row =4, column = 2) 

btn11 =tkinter.Button( text="-")

btn11.config(width = 10, height = 6 , command = subtract)

btn11.grid( row =1, column = 3 )

btn11.configure(state = "disable")


btn10 =tkinter.Button( text="+")

btn10.config(width = 10, height = 6 , command = plus)

btn10.grid( row =0, column = 3 ) 

btn10.configure(state = "disable")


btn12 =tkinter.Button( text="x")

btn12.config(width = 10, height = 6 , command = mutiply)

btn12.grid( row =2, column = 3 ) 

btn12.configure(state = "disable")


btn13 =tkinter.Button( text="/")

btn13.config(width = 10, height = 6 , command = division)

btn13.grid( row =3, column = 3 ) 

btn13.configure(state = "disable")


# calcular Text


tx = tkinter.Text(width = 30 ,height = 1 )

tx.grid( row = 0 , column = 0 , columnspan = 3 , rowspan = 1 , ipadx = 4)





tx.configure(state = "disable")




cframe.mainloop()
