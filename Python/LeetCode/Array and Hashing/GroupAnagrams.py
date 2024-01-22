class Solution:
    def groupAnagrams(strs):
        strs.sort()
        thedict = {}
        for item in strs:
            
            if (''.join(sorted(item)) in thedict):
                thedict[''.join(sorted(item))].append(item)
            else:
                thedict[''.join(sorted(item))] = [item]

        return(list(thedict.values()))








# strs = ["yak","rum","yak","tip","pep","feb","paw",'den','ned']
# strs.sort()
# print(strs)
# thedict = {}
# theAccess = False
# for item in strs:
#     x = 0
#     # print(item)
#     for i in item:
#         # print(ord(i),end=' ')
#         x +=ord(i)
        
#     if item in thedict:
#         thedict[item].append(item)
#     elif x in thedict:
#         print(x)
#         if sorted(thedict[x][0])!= sorted(item):
#             print(thedict)
#             print(item)
#             thedict[item] = [item]
#         else:
#             thedict[x].append(item)
#     else:
#         thedict[x] = [item]

# print(list(thedict.values()))


# print(''.join(sorted('ahmed')))