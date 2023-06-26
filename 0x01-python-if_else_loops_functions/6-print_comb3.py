#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
#!/usr/bin/python3
for x in range(0, 10):
    for i in range(x, 9):
        if (x != 8):
            print("{}{}, ".format(x, i+1), end='')
        else:
            print("{}{}\n".format(x, i+1), end='')
