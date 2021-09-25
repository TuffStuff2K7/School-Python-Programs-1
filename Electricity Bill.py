from datetime import date

name = input('Enter name: ')
consumerid = input('Enter consumer ID: ')
units = int(input('Enter units: '))

if units < 0:
    print ('Invalid argument, please enter a number above 0')
    exit()

elif units <= 100:
    con = units*1.5
    add = 25.0

elif units <= 200:
    con = (100*1.5)+(units-100)*2.5
    add = 50.0

elif units <= 300:
    con = (100*1.5)+(200-100)*2.5+(units-200)*4
    add = 75.0

elif units <= 350:
    con = (100*1.5)+(200-100)*2.5+(300-200)*4+(units-350)*5
    add = 100.0

elif units > 350:
    con = 1500.0
    add = 0.0
    
print("")   

print('~~~~~~~~~ TamilNadu Electricity Board ~~~~~~~~~')
print('              Coimbatore District               ')
print("")

print('Date: ', date.today())
print('Consumer no:', consumerid)
print('Name:', name)
print('Units consumed:', units)
print("")

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print("")

print("Unit charges:", con)
print("Additional charges:", add)
print("")

print("Total amount:", con + add)
print("")

print('~~~~~~~~~~~~~~ Save Electricity! ~~~~~~~~~~~~~~')
print("")

exitSaver= input('Input anything to continue: ')