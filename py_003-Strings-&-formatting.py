''' Working with strings and...
 different formating methods
 '''
File_name = 'olami'
print(File_name.upper())
brand = 'Apple'
exchange_rate = 1.235235245

message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' %(brand,1299,exchange_rate)
print(message)

message_0 = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple', 1299, 1.235235245)
print(message_0)
print(type(message))

message_3 = 'The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR'.format('Apple',
 1299, 1.235235245)
print(message_3)

print(type(message))

X ='committee'
print(X.count('m',3))
print(X.startswith('co',2,6),X.endswith(('it','tee')))  # start or end with object specified

D = 'Focusing on myself'
print(D.find('n'))
print(D.index('n'),D.find('a'))

A = '_'
print(A.join(X))