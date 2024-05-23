
#This function will return the maximum of given numbers.
def max_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:   #The signs >= are called compare operators that compare values including strings.
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(3,41,5))