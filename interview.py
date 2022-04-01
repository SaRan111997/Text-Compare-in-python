import collections

str = 'HC:Unsafe condition: Access not provided in the excavation for ingress/egress'

#split string
splits = str.split()
file1 = open('input2.txt', 'r')
Lines = file1.readlines()
count = 0
length=[]
#l=[5,6,8,7,8]
def checking(text):
	input1=str.split()
	input2=text.split()
	#print(input1)
	#print(input2)
	#print(list(set(input1) & set(input2)))
	#print(len(list(set(input1) & set(input2))))
	length.append(len(list(set(input1) & set(input2))))
	if len(list(set(input1) & set(input2)))==8:
		def listToString(input2):
			# initialize an empty string
			str1 = " "
			return (str1.join(input2))
		print(listToString(input2))
		#print(input2)
#print(length)
#print(max(l))

for line in Lines:
	count += 1
	checking(line)
print(length)
#print(max(length))

