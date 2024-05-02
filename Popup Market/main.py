mainMenu = '''
*----------------------------------------*
|               Main menu                |
*----------------------------------------*
| Option |          Description          |
*----------------------------------------*
|   1    | Register Purchase             |
|   2    | Register Repurchase           |
|   3    | Earnings (Amount per day)     |
|   4    | Earnings (Percentage per day) |
|   E    | Exit                          |
*----------------------------------------*
'''

weekMenuPurchase = '''
*----------------------*
|       Purchase       |
*----------------------*
| Option | Description |
*----------------------*
|   1    |  Monday     |
|   2    |  Tuesday    |
|   3    |  Wednesday  |
|   4    |  Thursday   |
|   5    |  Friday     |
|   B    |  Go back    |
*----------------------*
'''

weekMenuRepurchase = '''
*----------------------*
|      Repurchase      |
*----------------------*
| Option | Description |
*----------------------*
|   1    |  Monday     |
|   2    |  Tuesday    |
|   3    |  Wednesday  |
|   4    |  Thursday   |
|   5    |  Friday     |
|   B    |  Go back    |
*----------------------*
'''

main_Menu_Option = ''
week_Menu_Option = ''
mondayEarning = 0
tuesdayEarning = 0
wednesdayEarning = 0
thursdayEarning = 0
fridayEarning = 0
score = '*'
noScore = ' '
invalidMsg = 'Error: Not a valid option!'
enterMsg = 'Enter your option '

while main_Menu_Option != 'E':
    # update the total earning every time we go back to the main menu
    totalEarning = 0
    for earning in [mondayEarning, tuesdayEarning, wednesdayEarning, thursdayEarning, fridayEarning]:
        if earning >= 0:
            totalEarning = totalEarning + earning

    print(mainMenu)
    main_Menu_Option = input(enterMsg)

    # handle option 1 in main menu

    if main_Menu_Option not in ['1', '2', '3', '4', 'E']:
        print()
        print(invalidMsg)
        continue

    if main_Menu_Option == '1':
        print(weekMenuPurchase)
        week_Menu_Option = input(enterMsg)
        if week_Menu_Option not in ['1', '2', '3', '4', '5', 'B']:
            print()
            print(invalidMsg)
            continue
        if week_Menu_Option == 'B':
            continue

        purchaseSum = int(input('Enter purchase sum '))
        if week_Menu_Option == '1':
            mondayEarning = mondayEarning + purchaseSum
        elif week_Menu_Option == '2':
            tuesdayEarning = tuesdayEarning + purchaseSum
        elif week_Menu_Option == '3':
            wednesdayEarning = wednesdayEarning + purchaseSum
        elif week_Menu_Option == '4':
            thursdayEarning = thursdayEarning + purchaseSum
        elif week_Menu_Option == '5':
            fridayEarning = fridayEarning + purchaseSum

    # handle option 2 in main menu
    if main_Menu_Option == '2':
        print(weekMenuRepurchase)
        week_Menu_Option = input(enterMsg)
        if week_Menu_Option not in ['1', '2', '3', '4', '5', 'B']:
            print()
            print(invalidMsg)
            continue
        if week_Menu_Option == 'B':
            continue

        repurchaseSum = int(input('Enter repurchase sum '))
        if week_Menu_Option == '1':
            mondayEarning = mondayEarning - repurchaseSum
        elif week_Menu_Option == '2':
            tuesdayEarning = tuesdayEarning - repurchaseSum
        elif week_Menu_Option == '3':
            wednesdayEarning = wednesdayEarning - repurchaseSum
        elif week_Menu_Option == '4':
            thursdayEarning = thursdayEarning - repurchaseSum
        elif week_Menu_Option == '5':
            fridayEarning = fridayEarning - repurchaseSum

    # handle option 3 in main menu
    if main_Menu_Option == '3':
        weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        weekday_earnings = [mondayEarning, tuesdayEarning, wednesdayEarning, thursdayEarning, fridayEarning]
        for weekday_name, weekday_earning in zip(weekday_names, weekday_earnings):
            if weekday_earning < 0:
                earning_output = "{:>11}kr (LOSS)".format(weekday_earning)
            else:
                earning_output = "{:>11}kr".format(weekday_earning)
            print("{:<10}:{}".format(weekday_name, earning_output))

    # handle option 4 in main menu
    if main_Menu_Option == '4':
        mondayPercentage = ("{:.1f}".format((mondayEarning / totalEarning) * 100))
        tuesdayPercentage = ("{:.1f}".format((tuesdayEarning / totalEarning) * 100))
        wednesdayPercentage = ("{:.1f}".format((wednesdayEarning / totalEarning) * 100))
        thursdayPercentage = ("{:.1f}".format((thursdayEarning / totalEarning) * 100))
        fridayPercentage = ("{:.1f}".format((fridayEarning / totalEarning) * 100))

        for i in range(10, 0, -1):
            print()
            value = (i - 1) * 10
            if i == 10 or i == 5:
                space = '' if i == 10 else ' '
                print(f"{space}{i * 10}% |", end=' ')
            else:
                print('     |', end=' ')

            for earningPercentage in [mondayPercentage, tuesdayPercentage, wednesdayPercentage, thursdayPercentage,
                                      fridayPercentage]:

                if float(earningPercentage) > value:
                    print(' ' + score, end='  ')
                else:
                    print(' ' + noScore, end='  ')

        print()
        print('      --------------------')
        print('       Mo  Tu  We  Th  Fr')
        print()
        weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        weekday_percentages = [mondayPercentage, tuesdayPercentage, wednesdayPercentage, thursdayPercentage,
                               fridayPercentage]
        for weekday_name, weekday_percentage in zip(weekday_names, weekday_percentages):
            if float(weekday_percentage) < 0:
                print("{:<10}:{:>11}%".format(weekday_name, 0.0))
            else:
                print("{:<10}:{:>11}%".format(weekday_name, weekday_percentage))
