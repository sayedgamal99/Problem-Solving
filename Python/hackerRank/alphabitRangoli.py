

# ----c----
# --c-b
# c-b-a


def print_rangoli(size):

    liss = []
    for i in range(size):
        liss.append(chr(ord('a')+i))
    revliss = list(reversed(liss))
    revliss = revliss+liss[1:]
    print(revliss)
    columns = size*2 - 1
    rows = size*2 - 1
    col_list = [columns-1]

    for i in range(rows):
        indexx = 0
        if (i >= size):
            col_list.pop(-1)
        else:
            if (i != 0):
                col_list.append((col_list[-1]-2))

        for ii in range(columns):
            if (ii in col_list and i < size):
                print(revliss[indexx], end='')
                indexx += 1
            elif (ii in col_list and i >= size):
                print(revliss[indexx], end='')
                indexx += 1
            else:
                print('-', end='')
        indexx = 0
        revv = ''
        for ii in range(columns-1):
            if (ii in col_list and i < size):
                # print(revliss[indexx],end='')
                revv += revliss[indexx]
                indexx += 1
            elif (ii in col_list and i >= size):
                # print(revliss[indexx],end='')
                revv += revliss[indexx]
                indexx += 1
            else:
                # print('-',end='')
                revv += '-'
        revv = (reversed(revv))

        print(''.join(list(revv)))
        # print(col_list)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
