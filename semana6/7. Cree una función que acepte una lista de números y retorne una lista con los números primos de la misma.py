def is_prime():
  list_numbers=[1,3,6,2,7,8]
  prime_list=[]
  for number in list_numbers:
    counter1=0
    for index in range(1,number):
      if number%index==0:
        counter1=counter1+1
    if counter1==1:
        prime_list.append(number)
    print(prime_list)
      
is_prime()

