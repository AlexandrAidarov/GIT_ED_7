# Дана строка (возможно, пустая) состоящая из букв от A-Z
# Нужно написать строку  вида RLE, которая на выходе даст
# A7B12C43XBA3


superString = input("Введите буквы: ")
sumList = ()
sum = 0
L = 0
letter = "ab"
for i in superString:
    L += 1
    if i == letter and L < len(superString):
        sum += 1
        letter = i
    elif i == letter and L == len(superString):
        sum += 1
        sumList.append(letter)
        sumList.append(sum)
    elif i != letter and L == len(superString):
        sumList.append(letter)
        if sum > 1:
            sumList.append(sum)
        sumList.append(i)
    
    else:
        if L == 1:
            sum += 1
            letter = i
        else:
            sumList.append(letter)
            letter = i
            if sum > 1:
                sumList.append(sum)
            sum = 1
        



print(sumList)