
def inttoroman2(number):
	digitvalues = [1000, 900, 500,  100, 90, 50, 40, 10, 9, 5, 4, 1]
	romanianvalues = ['M', 'CM', 'D', 'C', 'XC', 'L', 'XL',  'X', 'IX', 'V', 'IV', 'I']
	n = number
	finnaly = []
	finnaly2 = []
	for x in range(len(digitvalues)):
		newnumber = number // digitvalues[x]
		number = number - newnumber * digitvalues[x]
		finnaly.append(newnumber)
		#print(number ,newnumber , digitvalues[x])
	for x in range(len(finnaly)):
		#print(x, finnaly[x], romanianvalues[x])
		finnaly2.append(finnaly[x] * romanianvalues[x])
	end = ''.join(finnaly2)
	print(end, n)
	return end
	#print(finnaly2)
	#print(number)
	#print(finnaly)

for i in range(100):
	inttoroman2(i)
inttoroman2(90)
