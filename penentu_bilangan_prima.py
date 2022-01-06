import timeit

start = timeit.default_timer()

def isPrime(an_array):
    primes = [] #Array kosong untuk diisi bilangan prima
    for element in an_array: #Looping untuk tiap element array
        if element >= 2:
            for i in range(2,element): #Looping untuk mencari pembagi
                if element % i == 0: #Jika bilangan bisa dibagi maka program berhenti
                    break
            else:
                primes.append(element) #Jika bilangan tidak ada pembagi maka akan masuk ke array bilangan prima
    print("Prime numbers: ",primes) #Print array bilangan prima

ara_ara = [0,1,2,3,4,5,6,7,8,9,10,2000,5711,7919]
isPrime(ara_ara)

stop = timeit.default_timer()
print('Time: ', stop - start)  
