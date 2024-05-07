# if __name__ == '__main__':
#     N = int(input())
#     thelist=[]
#     for command in range(N):
#         ask = input().split()
#         if ask[0] == 'insert':
#             thelist.insert(int(ask[1]),int(ask[2]))
#         elif ask[0] == 'print':
#             print(thelist)
#         elif ask[0] == 'remove':
#             if int(ask[1]) in thelist:
#                 thelist.remove(int(ask[1]))
#         elif ask[0] == 'append':
#             thelist.append(int(ask[1]))
#         elif ask[0] == 'sort':
#             thelist.sort()
#         elif ask[0] == 'pop':
#             thelist.pop()
#         elif ask[0] == 'reverse':
#             thelist.reverse()


steps = int(input())
print((steps/5).__ceil__())