txt = open("03-30 19-58-25.txt",'r', encoding='ANSI')
out=txt.read()
length=len(out)
string_list=[]
binary=[]
for i in range(length):
    if out[i]+out[i+1]+out[i+2]=="ncy" :
        for j in range(i+4, length):
            if out[j]=='\"':
                freqency=out[j+1]
                for k in range(j+3,length):
                    if out[k]=='\"' and k<=j+4:
                        freqency+=out[k-1]
                        break
                break
        break
string2number=""
for i in range(len(freqency)):
    binary.append(bin(ord(freqency[i])))
    k=int(binary[i], 2)
    string2number += k.to_bytes((k.bit_length() + 7) // 8, 'big').decode()
string_list.append(string2number)
print(string2number)