import datetime
history=[]
shall_I_continue=1

while shall_I_continue:
    user_input=int(input("""
        Enter 1 to convert Celcius to Kelvin
        Enter 2 to convert Kelvin to Celcius
        Enter 3 to convert Celcius to Farenheit
        Enter 4 to convert Farenheit to Celcius
        Enter 5 to convert Kelvin to Farenheit
        Enter 6 to convert Farenheit to Kelvin
        Enter 7 to sort by from value
        Enter 8 to sort by to value
        Enter 9 to sort by date/time
        Enter 10 to Exit
        """).strip())

    if user_input==1:
        C=int(input('Input the Celius value ').strip())
        K=C+273.15
        print(C,"C in Kelvin is ",K)
        history.append(("C",C,"K",K,datetime.datetime.now()))

    elif user_input==2:
        K=int(input('Input the Kelvin value ').strip())
        C=K-273.15
        print(K,"K in Celcius is ",C)
        history.append(("K",K,"C",C,datetime.datetime.now()))

    elif user_input==3:
        C=int(input('Input the Celcius value ').strip())
        F=C*1.8+32
        print(C,"C in Farenheit is ",F)
        history.append(("C", C, "F", F, datetime.datetime.now()))

    elif user_input==4:
        F=int(input('Input the Farenheit value ').strip())
        C=(F - 32)*0.5556
        print(F,"F in Celcius is ",C)
        history.append(("F",F,"C",C,datetime.datetime.now()))

    elif user_input==5:
        K=int(input('Input the Kelvin value ').strip())
        F=(K-273.15) * 1.8 +32
        print(K,"K in Farenheit is ",F)
        history.append(("K", K, "F", F, datetime.datetime.now()))

    elif user_input==6:
        F=int(input('Input the Farenheit value ').strip())
        K=(F -32)* 0.556 + 273.15
        print(F,"F in Kelvin is ",K)
        history.append(("F", F, "K", K, datetime.datetime.now()))

    elif user_input==7:
        print(sorted(history,key=lambda x:x[1]))
    elif user_input==8:
        print(sorted(history,key=lambda x:x[3]))
    elif user_input==9:
        print(history)
    elif user_input==10:
        shall_I_continue=0












