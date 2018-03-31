def read(file_name):
    txt = open(file_name,'r', encoding='latin-1')
    out=txt.read()
    length=len(out)
    string_list=[]
    frequency=""
    for i in range(length):
        k=out.find("frequency")
        k+= (len("frequency")+2)
        for j in range(k, length):
            if out[j]=='\"':
                for m in range(j+1,length):
                    frequency += out[m]
                    if out[m+1]=='\"':
                        break
                break
        break
    print(frequency)

    for i in range(length):
        k=out.find("close_eye")
        k+=(len("close_eye")+2)
        for j in range(k, length):
            if out[j]=='\"':
                close=out[j+1]
                break
        break
    string_list.append(close)
    print(close)

    for i in range(length):
        k=out.find("yawn")
        k+=(len("yawn")+2)
        for j in range(k, length):
            if out[j]=='\"':
                yawn=out[j+1]
                break
        break
    string_list.append(yawn)
    print(yawn)

    for i in range(length):
        k=out.find("posture")
        k+=(len("posture")+2)
        for j in range(k, length):
            if out[j]=='\"':
                posture=out[j+1]
                break
        break
            
    string_list.append(posture)
    print(posture)

    for i in range(length):
        k=out.find("unknown")
        k+=(len("unknown")+2)
        for j in range(k, length):
            if out[j]=='\"':
                unknown=out[j+1]
                break
        break
    string_list.append(unknown)
    print(unknown)
    txt.close()
    return string_list

    # Main method.
if __name__ == '__main__':
    read("temp.txt")