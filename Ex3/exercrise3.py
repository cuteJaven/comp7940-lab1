from Ex2.exercrise2 import print_factor


def loop_fac(x):
    new_list=[str(a) for a in x]
    for i in range(len(new_list)):
        print_factor(new_list[i])


my_list = [52633, 8137, 1024, 999]
loop_fac(my_list)
