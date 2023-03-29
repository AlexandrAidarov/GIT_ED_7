# [1, 4, 5, 2, 3, 8, 9, 0, 11 ]  -> 0-5, 8-9, 11


def a(input_list):
    resultTemp = []
    result = []
    for i in range(len(input_list)):
        if i == len(input_list) - 1 and input_list(i) not in resultTemp:
            
            

