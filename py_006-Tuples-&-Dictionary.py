#Tuples-%-Dictionary

Days_of_the_week = ('Mon','Tue','Wed','Thurs','Fri','Sat','Sun')

Days_of_the_week[:-2]


Position = ('First','Second','Third')

print(type(Position))


New_dict = {'Username':'John','Class no':223,'College':'Computer science'}

New_dict['College']

print(type(New_dict))

for key,value in New_dict.items():
    print(key,':',value)