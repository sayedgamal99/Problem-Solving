# x= 10
# occ = str(oct(x))[2:]
# hexx = (str(hex(x))[2:]).upper()
# binn = (str(bin(x))[2:])
# name = 'ahmed'
# print(f'the name is {name}')

# def print_formatted(number):
#     for i in range(1,number+1):
#         spaces = len(str((number)))
#         spaces2 = len(str(oct(number)))-2
#         spaces3 = len(str(hex(number)))-2
#         spaces4 = len(str(bin(number)))-2
#         x= i
#         occ = (str(oct(x))[2:]).rjust(spaces2)
#         hexx = (str(hex(x))[2:]).upper().rjust(spaces3)
#         binn = ((str(bin(x))[2:])).rjust(spaces4)
#         print(str(x).rjust(spaces),occ,hexx,binn)

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


print(" ahmed ".zfill())