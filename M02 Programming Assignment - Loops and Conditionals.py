#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 4.1 Choose a number between 1 and 10 and assign it to the variable secret. Then, select another number between 1 and 10
# and assign it to the variable guess. Next, write the conditional tests (if, else, and elif) to print the string 'too low'
# if guess is less than secret, 'too high' if greater than secret, and 'just right' if equal to secret.


# In[ ]:


secret = 8 #Assign a number to secret as directed in 4.1
guess = 6 #Assign a number to guess as directed in 4.1

if guess < secret: #evaluate whether guess is less than secret
    print(str(guess) + " too low") #print result
elif guess == secret: #evaluate whether guess is equal to secret
    print(str(guess) + " just right!") #print result
elif guess > secret: #evaluate whether guess is greater than secret
    print(str(guess) + " too high") #print result


# In[ ]:


# 4.2 Assign True or False to the variables small and green. Write some if/else statements to print which of these matches
# those choices: cherry, pea, watermelon, pumpkin.


# In[ ]:


small = True #Assign true or false to small as directed in 4.2
green = True #Assign ture or false to green as directed in 4.2

if small:
    if green:
        print("It is a pea.")
    else:
        print("It may be a cherry.")
elif green:
    print("It is a watermelon.")
else:
    print("It might be a pumpkin.")


# In[ ]:


# 6.1 Use a for loop to print the values of the list [3, 2, 1, 0].


# In[ ]:


valuesList = [3,2,1,0] #creates a list with values as assigned in 6.1
for x in valuesList: #cycles through each position in the list
    print(x) #prints the value stored in the current position


# In[ ]:


# 6.2 Assign the value 7 to the variable guess_me, and the value 1 to the variable number. Write a while loop that compares
# number with guess_me. Print 'too low' if number is less than guess me. If number equals guess_me, print 'found it!' and
# then exit the loop. If number is greater than guess_me, print 'oops' and then exit the loop. Increment number at the end
# of the loop.


# In[ ]:


guess_me = 7 #Assigns the value 7 to the variable guess_me as directed in 6.2
number = 1 #Assigns the value 1 to the variable number as directed in 6.2

while number <= guess_me: #set up a while loop
    if number < guess_me: #evaluate whether number is less than guess_me
        print(str(number) + " too low") #print result
    if number == guess_me: #evaluate whether number is equal to guess_me
        print(str(number) + " found it!") #print result
        break #exit loop
    elif number > guess_me: #evaluate whether number is greater than guess_me
        print(str(number) + " is greater than " + str(guess_me) + ". oops") #print result
        break #exit loop
    number += 1 #increment number


# In[ ]:


# 6.3 Assign the value 5 to the variable guess_me. Use a for loop to iterate a variable called number over range(10). If
# number is less than guess_me, print 'too low'. If it equals guess_me, print found it! and then break out of the for loop.
# If number is greater than guess_me, print 'oops' and then exit the loop.


# In[ ]:


guess_me = 5 #Assigns the value 5 to the variable guess_me as directed in 6.3

for number in range(0,10): #initiates a for loop, defines the range to be checked and sets number as the variable to store the number being checked
    if number < guess_me: #evaluate whether number is less than guess_me
        print(str(number) + " too low") #print result
    if number == guess_me: #evaluate whether number is equal to guess_me
        print(str(number) + " found it!") #print result
        break #exit loop
    elif number > guess_me: #evaluate whether number is greater than guess_me
        print(str(number) + " is greater than " + str(guess_me) + ". oops") #print result
        break #exit loop

