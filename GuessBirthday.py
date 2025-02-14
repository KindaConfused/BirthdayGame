from random import randint as rint

print("Day|Month|Year, H = Higher, L = Lower and C = Correct\nCD for Correct Day, CM for Correct Month, CY for Correct Year\n")

smallD = 1
smallM = 1
smallY = 1924

largeD = 31
largeM = 12
largeY = 2024

D = rint(smallD, largeD)
M = rint(smallM, largeM)
Y = rint(smallY, largeY)

Day = False
Month = False
Year = False

tries = 0

while True:
    if Day and Month and Year:
        break
    print(f"Is your Birthday {D} | {M} | {Y}?")
    user = input("Higher, Lower or Correct: ").lower()
    if user == 'h':
        tries += 1
        D = rint(D, largeD)
        M = rint(M, largeM)
        Y = rint(Y, largeY)
    elif user == 'l':
        tries += 1
        D = rint(smallD, D)
        M = rint(smallM, M)
        Y = rint(smallY, Y)
    elif user == 'cd':
        print("Day Locked")
        smallD = D
        largeD = D
        Day = True
    elif user == 'cm':
        print("Month Locked")
        smallM = M
        largeM = M
        Month = True
    elif user == 'cy':
        print("Year Locked")
        smallY = Y
        largeY = Y
        Year = True
    elif user == 'c':
        break
    else:
        print("Please type H, L, or C, CD, CM, CY")

print(f"\nYour Birthday is {D}|{M}|{Y}!\nIt took {tries} Tries")