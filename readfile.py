def read(file_name):
    txt = open(file_name,'r', encoding='ANSI')
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
                        if out[k]=='\"' and k<=j+5:
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

    for i in range(length):
        if out[i]+out[i+1]+out[i+2]=="eye":
            for j in range(i+4, length):
                if out[j]=='\"':
                    close=out[j+1]
                    break
            break
            
    string_list.append(close)
    print(close)

    for i in range(length):
        if out[i]+out[i+1]+out[i+2]=="awn" :
            for j in range(i+4, length):
                if out[j]=='\"':
                    yawn=out[j+1]
                    break
            break
    string_list.append(yawn)
    print(yawn)

    for i in range(length):
        if out[i]+out[i+1]+out[i+2]=="ure" :
            for j in range(i+4, length):
                if out[j]=='\"':
                    posture=out[j+1]
                    break
            break
            
    string_list.append(posture)
    print(posture)

    for i in range(length):
        if out[i]+out[i+1]+out[i+2]=="own" :
            for j in range(i+4, length):
                if out[j]=='\"':
                    unknown=out[j+1]
                    break
            break
    string_list.append(unknown)
    print(unknown)
    txt.close()
    return string_list