import urllib.request as req
import socket
import http.client


file = open(r"C:\Users\asus\Downloads\Football\imagenet.synset.geturls","r")

i=245
for link in file:
    # print(link)
    file_name = "ball_" + str(i)+ ".jpg"
    try:
        site = req.urlopen(link)
        x=site.getheader('Content-Length')
        if isinstance(x, str):
            file_size = int(x)
            if file_size > 3500: #4kb nearly
                print(str(i)+"- file-size->",file_size," name-",link) #file_size in bytes
                req.urlretrieve(link, "C:\\Users\\asus\\Downloads\\Football\\Football Images\\" + file_name)
                i+=1
            else:
                continue
        else:
            continue           
    except req.HTTPError as e:
        print (e.code)
    except req.URLError as e:
        print ('URL_Error')
    except socket.timeout as e:
        print ("timeout")
    except http.client.HTTPException as e:
        print("HTTPException")
    except ConnectionError:
        print("Connection Error")

file.close()