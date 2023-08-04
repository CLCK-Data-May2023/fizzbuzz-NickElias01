#Goal: output numbers from 1 to 100.
   #if number is divisible by 3, replace with FIZZ
   #if number is divisible by 5, replace with BUZZ
   #if both, FIZZBUZZ

for i in range(1,101,1):
    if i % 3 == 0 and not i % 5 == 0:
        i = "Fizz"
    elif i % 5 == 0 and not i % 3 == 0:
        i = "Buzz"
    elif i % 3 == 0 and i % 5 == 0:
        i = "FizzBuzz"
    print(i)