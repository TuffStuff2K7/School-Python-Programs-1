print('Enter marks to know total:')
print("")

eng = input('English: ')
math = input('Maths  : ')
soc = input('Social : ')
sci = input('Maths  : ')
l2 = input('L2     : ')
print("")

total = float(eng) + float(math) + float(soc) + float(sci) + float(l2)
average = total / 5
print("Total = ", total)
print("Average = ", average)
print("")

input()