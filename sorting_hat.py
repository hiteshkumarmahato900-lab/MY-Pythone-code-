############################ Hitesh n################################
ravenclaw = 0
gryffindor = 0
hufflepuff = 0
slytherin = 0
############################question 1################################
print('Q1) Do you like Dawn or Dusk? \n')
print('1) Dawn ')
print('2) Dusk\n')

answer=int(input('Enter your answer (1-2):\n'))
if answer ==1 :
 gryffindor = gryffindor +1
 ravenclaw = ravenclaw +1
elif answer ==2 :
 hufflepuff = hufflepuff +1
 slytherin = slytherin +1 
else :
  print( "Wrong input.")

print('\n')
############################question  2################################
print('Q2) When I’m dead, I want people to remember me as:\n')
print('1) The Good ')
print('2) The Great ')
print('3) The Wise ') 
print('4) The Bold\n') 

answer=int(input('Enter your answer (1-4):\n'))

if answer ==2 :
  slytherin = slytherin +2
elif answer ==1 :
 hufflepuff = hufflepuff +2
elif answer ==3 :
   ravenclaw = ravenclaw +2
elif answer ==4:
   gryffindor = gryffindor +2
else :
  print( "Wrong input.")

print('\n')
############################question 3################################
print('Q3) Which kind of instrument most pleases your ear? \n ')
print('1) The violin ') 
print('2) The trumpet')
print('3) The piano ')
print('4) The drum\n')

answer=int(input('Enter your answer (1-4):\n'))

if answer ==2 :
  slytherin = slytherin +2
elif answer ==1 :
 hufflepuff = hufflepuff +2
elif answer ==3 :
   ravenclaw = ravenclaw +2
elif answer ==4:
   gryffindor = gryffindor +2
else :
  print( "Wrong input.")
print('\n')
############################ total ################################
print('The Total Score For Each House.\n')

print("Slytherin  :",slytherin)
print("Hufflepuff :",hufflepuff)
print("Ravenclaw  :",ravenclaw)
print("Gryffindor :",gryffindor)

############################ Thank YOU ################################