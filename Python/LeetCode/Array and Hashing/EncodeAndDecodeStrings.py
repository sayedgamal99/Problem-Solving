class solution:
    def encode(self,strs):
        result = ''
        for i in strs:
            result+=str(len(i))+'@'+i
        return result

    def decode(self,strr):
        result=[]
        num = ''
        i = 0
        while(i<len(strr)):
            num = int(strr[i:strr.find('@',i)])
            result.append(strr[i+2:i+2+num])
            i=i+2+num
        return result



Input= ["lint","co@@de","l:;ove","you"]
todecode = solution().encode(Input)
print(todecode)
print(solution().decode(todecode))

# print('ahmed'.find())