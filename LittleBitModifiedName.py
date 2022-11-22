inputs = input("Write your name: ")
upperlet = inputs.upper()

print_a = [[" "for row in range(7)]for col in range(7)]
print_b = [[" "for row in range(7)]for col in range(7)]
print_c = [[" "for row in range(7)]for col in range(7)]
print_d = [[" "for row in range(7)]for col in range(7)]
print_e = [[" "for row in range(7)]for col in range(7)]
print_f = [[" "for row in range(7)]for col in range(7)]
print_g = [[" "for row in range(7)]for col in range(7)]
print_h = [[" "for row in range(7)]for col in range(7)]
print_i = [[" "for row in range(7)]for col in range(7)]
print_j = [[" "for row in range(7)]for col in range(7)]
print_k = [[" "for row in range(7)]for col in range(7)]
print_l = [[" "for row in range(7)]for col in range(7)]
print_m = [[" "for row in range(7)]for col in range(7)]
print_n = [[" "for row in range(7)]for col in range(7)]
print_o = [[" "for row in range(7)]for col in range(7)]
print_p = [[" "for row in range(7)]for col in range(7)]
print_q = [[" "for row in range(7)]for col in range(7)]
print_r = [[" "for row in range(7)]for col in range(7)]
print_s = [[" "for row in range(7)]for col in range(7)]
print_t = [[" "for row in range(7)]for col in range(7)]
print_u = [[" "for row in range(7)]for col in range(7)]
print_v = [[" "for row in range(7)]for col in range(7)]
print_w = [[" "for row in range(7)]for col in range(7)]
print_x = [[" "for row in range(7)]for col in range(7)]
print_y = [[" "for row in range(7)]for col in range(7)]
print_z = [[" "for row in range(7)]for col in range(7)]
print_space = [[" "for row in range(7)]for col in range(7)]
#For A
for row in range(7):
    for col in range(7):
      if ((row == 3) or ((col == 0 or col == 6) and (row != 0))or ((row == 0 or row == 3) and (col >0 and col <6))) :
        print_a[row][col] = "*"


#For Printing B

for row in range(7):
    for col in range(7):
        if col == 0 or (col == 6 and (row != 0 and row !=3 and row !=6)) or ((row == 0 or row == 3 or row ==6) and col <6):
            print_b[row][col] = "*"
#for C
for row in range(7):
  for col in range(7):
    if (col == 0 and (row != 0 and row != 6)) or (row == 0 and (col != 0) and (col != 6)) or (row == 6 and(col != 0) and (col != 6)):
        print_c[row][col] = "*"

#For D
for row in range(7):
  for col in range(7):
    if (col == 0) or (row == 0 and (col != 6 )) or (row == 6 and(col != 6 )) or (col == 6  and (row!= 0 and row != 6)):
        print_d[row][col] = "*"

#Print Space
for row in range(7):
  for col in range(7):
    if (col == 0) or (row == 0 and (col != 6 and col != 5)) or (row == 6 and(col != 6 and col != 5)) or (col == 6  and (row!= 0 and row != 6)):
        print_space[row][col] = " "





#for E
for row in range(7):
  for col in range(7):
    if (col == 0) or (row == 0) or row == 6 or row == 3:
        print_e[row][col] = "*"

#for F
for row in range(7):
  for col in range(7):
    if (col == 0) or (row == 0 and (col < 6)) or (row == 3 and (col < 6)):
        print_f[row][col] = "*"
#for G
for row in range(7):
  for col in range(7):
    if (col == 0 and row != 0 and row != 6 ) or (row ==6 and col <6) or (row == 0 and (col != 0 and col < 6)) or (row ==5 and (col>3)) or (row ==1 and col >5):
        print_g[row][col] = "*"

#printing H
for row in range(7):
    for col in range(7):
        if (col == 0 or col == 6) or (row == 3):
            print_h[row][col] = "*"

#Print I
for row in range(7):
    for col in range(7):
        if (row == 0 and (col>0 and col<6)) or (row == 6 and (col>0 and col<6)) or col == 3:
            print_i[row][col] = "*"

#print J
for row in range(7):
  for col in range(7):
    if (row == 6 and (col >0)) or (row == 0) or col ==6 or (col == 1 and row>3):
        print_j[row][col] = "*"

#Print K
for row in range(7):
  for col in range(7):
    if col ==0 or (col+row ==4) or (row - col == 2):
        print_k[row][col] = "*"

#Print L
for row in range(7):
  for col in range(7):
    if col == 0 or (row == 6 and (col < 6)):
      print_l[row][col] = "*"

#Print M
for row in range(7):
    for col in range(7):
       if (col == 0 or col == 6) or ((col == row) and (col >0 and col<4)) or ((col + row == 6) and (col>3 and col <6)):
         print_m[row][col] = "*"

#Printing N
for row in range(7):
  for col in range(7):
    if (col == 0 or col == 6) or (row == col):
        print_n[row][col] = "*"

#For Printing O

for row in range(7):
    for col in range(7):
        if (col == 0 and (row != 0 and row!= 6)) or (col == 6 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0 and col < 6)):
            print_o[row][col] = "*"

#For P
for row in range(7):
  for col in range(7):
    if (col == 0) or (row == 0 and (col >1 and col <5)) or (row == 3 and (col >1 and col <5)) or (col == 6 and (row >0 and row <3)):
        print_p[row][col] = "*"
#for q
for row in range(7):
    for col in range(7):
        if (col == 0 and (row >0 and row <5)) or (col == 6 and (row >0 and row <5)) or ((row == 0 and (col>1 and col<5) or row == 5) and (col > 0 and col < 6)) or (row==col and row >2):
            print_q[row][col] = "*"


#For R
for row in range(7):
    for col in range(7):
        if (col == 0) or (row == 0 and (col >1 and col <5)) or (row == 3 and (col >1 and col <5)) or (col == 6 and (row >0 and row <3)) or (row == col and row>3):
            print_r[row][col] = "*"

#for S
for row in range(7):
  for col in range(6):
    if ((row == 0 and col <5) or row == 3 or (row == 6 and col >0)) or (col == 0 and (row < 4)) or (col == 5 and (row >2)):
      print_s[row][col] = "*"

# Printing T
for row in range(7):
    for col in range(7):
        if (row == 0 and (col>0 and col <6)) or col == 3:
            print_t[row][col] = "*"

#For U
for row in range(7):
    for col in range(7):
        if (col == 0 and row != 6) or (col == 6 and row != 6) or ((row == 6) and (col != 0 and col != 6)):
            print_u[row][col] = "*"

#Print V
for row in range(7):
  for col in range(7):
    if ((row == col) and row < 4) or ((row + col == 6) and col > row):
        print_v[row][col] = "*"


#for W
for row in range(7):
    for col in range(7):
        if (col == 0 or col == 6) or ((row + col ==6) and (row > col)) or (row == col and row >2):
            print_w[row][col] = "*"

#PRINTING X
for row in range(7):
  for col in range(7):
    if (row == col) or (row + col == 6):
        print_x[row][col] = "*"
#For Y
for row in range(7):
    for col in range(7):
        if (col == 0 and (row < 3)) or col == 6 or row == 3 or row == 6:
            print_y[row][col] = "*"

#For Z
#Printing Z
for row in range(7):
  for col in range(7):
    if (row == 0 or row == 6) or (row + col == 6):
      print_z[row][col] = "*"





for row in range(7):
    for names in range(len(upperlet)):
        if upperlet[names] == "A":
            for col in range(7):
                print(" ", end="")
                print(print_a[row][col], end="")
                print("", end="")
        if upperlet[names] == "B":
            for col in range(7):
                print(" ", end="")
                print(print_b[row][col], end="")
                print("", end="")
        if upperlet[names] == "C":
            for col in range(7):
                print(" ", end="")
                print(print_c[row][col], end="")
                print("", end="")
        if upperlet[names] == "D":
            for col in range(7):
                print(" ", end="")
                print(print_d[row][col], end="")
                print("", end="")
        if upperlet[names] == "E":
            for col in range(7):
                print(" ", end="")
                print(print_e[row][col], end="")
                print("", end="")
        if upperlet[names] == "F":
            for col in range(7):
                print(" ", end="")
                print(print_f[row][col], end="")
                print("", end="")
        if upperlet[names] == "G":
            for col in range(7):
                print(" ", end="")
                print(print_g[row][col], end="")
                print("", end="")
        if upperlet[names] == "H":
            for col in range(7):
                print(" ", end="")
                print(print_h[row][col], end="")
                print("", end="")
        if upperlet[names] == "I":
            for col in range(7):
                print("", end="")
                print(print_i[row][col], end="")
                print("", end=" ")
        if upperlet[names] == "J":
            for col in range(7):
                print(" ", end="")
                print(print_j[row][col], end="")
                print("", end="")
        if upperlet[names] == "K":
            for col in range(7):
                print(" ", end="")
                print(print_k[row][col], end="")
                print("", end="")
        if upperlet[names] == "L":
            for col in range(7):
                print("", end="")
                print(print_l[row][col], end="")
                print(" ", end="")
        if upperlet[names] == "M":
            for col in range(7):
                print(" ", end="")
                print(print_m[row][col], end="")
                print("", end="")
        if upperlet[names] == "N":
            for col in range(7):
                print(" ", end="")
                print(print_n[row][col], end="")
                print("", end="")
        if upperlet[names] == "O":
            for col in range(7):
                print(" ", end="")
                print(print_o[row][col], end="")
                print("", end="")
        if upperlet[names] == "P":
            for col in range(7):
                print(" ", end="")
                print(print_o[row][col], end="")
                print("", end="")
        if upperlet[names] == "Q":
            for col in range(7):
                print(" ", end="")
                print(print_q[row][col], end="")
                print("", end="")
        if upperlet[names] == "R":
            for col in range(7):
                print("", end="")
                print(print_r[row][col], end="")
                print("", end="")
        if upperlet[names] == "S":
            for col in range(7):
                print(" ", end="")
                print(print_s[row][col], end="")
                print("", end="")
        if upperlet[names] == "T":
            for col in range(7):
                print(" ", end="")
                print(print_t[row][col], end="")
                print("", end="")
        if upperlet[names] == "U":
            for col in range(7):
                print(" ", end="")
                print(print_u[row][col], end="")
                print("", end="")
        if upperlet[names] == "V":
            for col in range(7):
                print(" ", end="")
                print(print_v[row][col], end="")
                print("", end="")
        if upperlet[names] == "W":
            for col in range(7):
                print(" ", end="")
                print(print_w[row][col], end="")
                print("", end="")
        if upperlet[names] == "X":
            for col in range(7):
                print(" ", end="")
                print(print_x[row][col], end="")
                print("", end="")
        if upperlet[names] == "Y":
            for col in range(7):
                print(" ", end="")
                print(print_y[row][col], end="")
                print("", end="")

        if upperlet[names] == "Z":
            for col in range(7):
                print(" ", end="")
                print(print_z[row][col], end="")
                print("", end="")
        if upperlet[names] == " ":
            for col in range(7):
                print(print_space[row][col], end="")
                print("", end="")

    print()

#Print A
# for row in range(7):
#   for col in range(7):
#     if ((row == 3) or ((col == 0 or col == 6) and (row != 0))or ((row == 0 or row == 3) and (col >0 and col <6))) :
#       print("*",end="")
#     else:
#       print(" ", end="")
#   print()

#PRINTING C
# for row in range(7):
#   for col in range(7):
#     if (col == 0 and (row!= 0 and row != 6)) or (row == 0 and (col != 0)) or (row == 6 and(col != 0)):
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()

#PRINTING D
# for row in range(7):
#   for col in range(7):
#     if (col == 0) or (row == 0 and (col != 6 and col!= 5)) or (row == 6 and(col != 6 and col!= 5)) or (col == 6  and (row!= 0 and row != 6)):
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()

#PRINTING E
# for row in range(7):
#   for col in range(7):
#     if (col == 0) or (row == 0) or row == 6 or row ==3 :
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()

#PRINTING F
# for row in range(7):
#   for col in range(7):
#     if (col == 0) or (row == 0) or row ==3 :
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()

#PRINTING G
# for row in range(7):
#   for col in range(7):
#     if (col == 0 and row!= 0 and row != 6 ) or (row ==6 and col <6) or (row == 0 and (col != 0 and col < 6)) or (row ==5 and (col>3)) or (row ==1 and col >5):
#       print("*",end="")
#     else:
#       print(" ", end="")
#   print()


# #Printing I
# for row in range(7):
#   for col in range(7):
#     if row == 0 or row == 6 or col ==3:
#       print_i [row] [col] = "*"
#   #   else:
#   #     print(" ", end="")
#   # print()

# #printing H
# for row in range(7):
#   for col in range(7):
#     if ((col == 0 or col == 6 ) and (row != 0)) or (row == 3):
#       print_h [row] [col] = "*"
#   #   else:
#   #     print(" ", end="")
#   # print()

#PRINTING J
# for row in range(7):
#   for col in range(7):
#     if (row == 6 and (col >0)) or (row == 0) or col ==6 or (col == 1 and row>3):
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()

#PRINTING K
# for row in range(7):
#   for col in range(7):
#     if col ==0 or (col+row ==4) or (row - col == 2) :
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()

# #Printing L
# for row in range(7):
#   for col in range(7):
#     if col == 0 or row == 6:
#       print_l [row] [col] = "*"

# #Printing M
# for row in range(7):
#   for col in range(7):
#     if (col == 0 or col == 6) or ((col == row) and (col >0 and col<4)) or ((col + row == 6) and (col>3 and col <6)):
#       print_m [row] [col] = "*"


#print n
# for row in range(7):
#   for col in range(7):
#     if (col == 0 or col == 6 ) or (row == col):
#         print_m[row][col] = "*"
#     else:
#       print(" ", end="")
#   print()

#PRINTING p
# for row in range(7):
#   for col in range(7):
#     if (col == 0) or (row == 0 and (col >1 and col <5)) or (row == 3 and (col >1 and col <5)) or (col == 6 and (row >0 and row <3)):
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()

#PRinting Q
# for row in range(7):
#     for col in range(7):
#         if (col == 0 and (row >0 and row <5)) or (col == 6 and (row >0 and row <5)) or ((row == 0 and (col>1 and col<5) or row == 5) and (col > 0 and col < 6)) or (row==col and row >2):
#           print("*", end="")
#         else:
#           print(" ",end="")
#     print()


#PRINTING R
# for row in range(7):
#   for col in range(7):
#     if (col == 0) or (row == 0 and (col >1 and col <5)) or (row == 3 and (col >1 and col <5)) or (col == 6 and (row >0 and row <3)) or (row == col and row>3):
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()

# # Printing S
# for row in range(7):
#     for col in range(7):
#         if (row == 0 or row == 3 or row == 6) or (col == 0 and (row != 4 and row != 6)) or (col == 6 and ((row != 0 and row != 1 and row != 2))):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# Printing T
#         for row in range(7):
#             for col in range(7):
#                 if row == 0 or col == 3:
#                     print("*", end="")
#                 else:
#                     print(" ", end="")
#             print()

#PRINTING v
# for row in range(7):
#   for col in range(7):
#     if ((row == col) and row <4) or ((row + col == 6) and col>row ):
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()

#Printing W
# for row in range(7):
#   for col in range(7):
#     if (col == 0 or col == 6) or ((row + col ==6) and (row > col)) or (row == col and row >2) :
#       print("*",end="")
#     else:
#       print(" ", end="")
#   print()

#PRINTING X
# for row in range(7):
#   for col in range(7):
#     if (row == col) or (row + col == 6):
#       print("*",end="")
#     else:
#       print(" ",end="")
#   print()

#Printing Y
# for row in range(7):
#   for col in range(7):
#     if (col == 0 and (row<3)) or col == 6 or row ==3 or row == 6:
#       print("*",end="")
#     else:
#       print(" ", end="")
#   print()

#Printing Z
# for row in range(7):
#   for col in range(7):
#     if (row == 0 or row == 6) or (row + col == 6):
#       print("*",end="")
#     else:
#       print(" ", end="")
#   print()
