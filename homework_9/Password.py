def password(str):
    count=0
    if (len(str)>=6):
        try:
            int(str)
            return("False")
        except:
            str=str.lower()
            if "password" in str:
                return("False") 
            else:
                for i in range(len(str)):
                    try:
                        int(str[i])
                        return("True")
                        break
                    except:
                        count+=1
                if count==len(str):
                    return("False")
    else:
        return("False")
