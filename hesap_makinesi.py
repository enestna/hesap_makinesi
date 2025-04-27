def calculator():
    print("things to do")
    print("1=sum")
    print("2=extraction")
    print("3=multiplication")
    print("4=division")
    print("5=exponent")
    process=input("Please enter the actions to be taken (1,2,3,4,5)")
    if process<'1' or process>'5':
        print("invalid login") 
            
    num1=float(input("please enter first number"))
    num2=float(input("please enter second number "))
    
    if process=='1':
        sum=num1+num2
        print("total=",sum)
    elif process=='2':
        extraction=num1-num2
        print("extraction=",extraction)
    elif process=='3':
        multiplication=num1*num2
        print("multiplication=",multiplication)
    elif process=='4':
         if num2==0:
             print("Error! You cannot divide a number by zero.")
         else :
             division=num1/num2
             print("division=",division)    
    elif process=='5':
        exponent=num1**num2
        print("exponent=",exponent)
 

calculator()