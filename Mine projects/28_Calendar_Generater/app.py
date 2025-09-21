import calendar

while True:


    try:
        user_choice = int(input('1.Check single month\n2.Whole year\n3.EXIT (1/2/3): '))
    except:
        print('Some thing went wrong!')
    
    #Check the option 

    if user_choice not in [1,2,3]:
        print('Invilad choice!')

    #print the speicfic month calender

    elif user_choice == 1:
        year = int(input('Enter the year: '))
        month = int(input('Enter the month: '))

        print(calendar.month(year,month))

    #print the whole year calender

    elif user_choice == 2:
        year_1 = int(input('Enter the year:  '))
        whole_year = calendar.calendar(year_1)
        print(whole_year,)
    else:
        print("see you later")
        break