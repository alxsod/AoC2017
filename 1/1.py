file_contents = open('input.txt','r')
int_contents = file_contents.read()


def calc_sum1():
    int_sum = 0
    prev_int = int_contents[len(int_contents)-1]
    for int1 in int_contents:
        if(int1 == prev_int):
            int_sum += int(int1);
        prev_int = int1
    return int_sum

def calc_sum2():
    int_sum = 0
    repeat = len(int_contents)
    repeat = int(repeat / 2)
    for indx in range(0,len(int_contents)):
        add_int = int_contents[(indx + repeat) % (len(int_contents))]
        if(int_contents[indx] == add_int):
            int_sum += int(add_int)
    return int_sum

## Answer 1
print(calc_sum1())
## Answer 2
print(calc_sum2())