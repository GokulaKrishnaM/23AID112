#Create an empty list.
#Use a loop to ask user 5 times to enter their favourite movies.
#Add each movie to the list.
#After all inputs, print the whole list.
Favourite_movies=[]
for i in range(5):
    mov=str(input("Favourite movie :"))
    Favourite_movies.append(mov)
print("Favourite movies:",Favourite_movies)