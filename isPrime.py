import math 
def isPrime(n):
	k=0
	for i in range (1,n+1):
		if n % i==0:
			k=k+1
	if k==2:
		return True	
	else:
		return False
def primeTh4kPlus1(n):
	currentNumberOf=0
	currentNumber=1
	while currentNumberOf<n:
		currentNumber+=1

		if isPrime(currentNumber) and currentNumber%4==1:
			currentNumberOf+=1
		
	return currentNumber
def primeDecomposition(n):
	a=0
	while a<math.sqrt(primeTh4kPlus1(n)):
		a=a+1
		if math.sqrt(primeTh4kPlus1(n)-a**2):
			return (a,math.sqrt(primeTh4kPlus1(n)-a**2))
			break
print(primeDecomposition(4))