import logging
logging.basicConfig(filename="t1.log" , level=logging.DEBUG,format= '%(asctime)s %(message)s')
l=[1,2,3,4,[1,2,3,4],"ashu","singh"]
l1=[]
l2=[]
for i in l:
    logging.info("hello")
    if type(i)==list:
        logging.info("hi")
        for j in i:
            logging.info("yeeee")
            if type(j)==int:
                logging.info("inside")
                l1.append(j)
    elif type(i)==int:
        l1.append(i)
    else :
        if type(i)==str:
            l2.append(i)
print(l1)
print(l2)
