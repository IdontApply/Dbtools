from dbman import Mydatabase as db
import csv


###############################################################################################################################################################################################
def csv_list():
    with open('/home/mytham9/workspace/working/thescraper/oplist/csvfilesfordb.txt','r+',encoding='utf8') as f:

        csvfile = f.readline()
        f.truncate(0)
    if csvfile:
        with open(csvfile.rstrip(), 'r',encoding='utf8') as f:
            list1 = list(csv.reader(f, delimiter=" "))
        return [x for x in list1 if x != []]


def INSERT_product_side(db = db(), csvlist = csv_list()):
    db.__init__()
    print(csvlist[0][6])
    ins = db.commans()[0]
    print('ins works')
    db.query(ins,[csvlist[0][6]])
    print('q works')
    s = db.ru()
    print('fetch works')
    ind = db.commans()[1]
    db.query(ind,[s])
    s1 = db.ru()
    inp = db.commans()[2]
    db.commit()


    for c in csvlist:
        c1 = [c[0], s1, c[5], c[4], c[3], c[2].replace(',', ''), c[1]]


        db.query(inp,c1)
#        c1 = [c[6],c[0],c[5],c[4],c[3],c[2].replace(',', ''),c[1]]
#        print(c1)
#        db.query(command, c1)

#        command = db.commans()[0]
#        c1 = [c[6],c[0],c[5],c[4],c[3],c[2].replace(',', ''),c[1]]
#        print(c1)
#        db.query(command, c1)
#        db.commit()

    db.commit()
    db.close()
###############################################################################################################################################################################################
#OperationalError: FATAL:  Peer authentication failed for user "hmayt"
