def getProduct(listOfNumbers):
    for num in listOfNumbers:
        difference = 2020 - num
        if difference in listOfNumbers:
            return num * difference

test = open("day1.txt", 'r')
data = []
for line in test:
    data.append(int(line))

print(getProduct(data))