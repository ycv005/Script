import json, codecs, ast

def in_double_quote(content):
    # print("checking string in double quotes")
    return len(content)!=len(content.strip('\"'))
    
with open("to_be_parse.txt","r") as f:
    dic = {}
    data = f.read().splitlines()
    i,metaline=0,0
    for line in data:
        if ": " in line:
            metaline+=1  #counting the no. of lines present in metadata
            key,content = line.split(": ")
            if "," in content and (not in_double_quote(content)):
                content = list(content.split(", "))
                dic[key]=content 
            elif "true" ==content.lower() or "false"==content.lower(): #accept any form of True, true, False, false
                content = ast.literal_eval(content.capitalize())
                dic[key] = content
            else:
                dic[key]=content.strip('\"')  #if extra "double quote" present then remove it, as present in Title and desc
        elif "READMORE" in line:
            dic["short-content"] = data[metaline+2:i] #adding everything before README & after MetaData as said, even new lines
            # metaline +2, here +2 means escaping those two 3 dash (---) lines
            dic["content"] = data[i+1:] #adding everything after READMORE as said, even new lines

            ## OR ##
            # dic["short-content"]= "Content before READMORE and after meta data"
            # dic["content"] = "Content after `READMORE`"
            break
        i+=1

with codecs.open("data.json", 'w',encoding='utf-8') as fp:
    js = json.dumps(dic,ensure_ascii=False)
    fp.write(js)
