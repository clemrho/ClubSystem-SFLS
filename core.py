#powered by Lucas Lu@SFLS
import csv


def printMenu():
    print("""
        **********************************************
        **   欢迎来到社团积分管理系统(powered by c10h8)!!  
        **   版本：v0.1.1（alpha）                        
        **   请输入数字选择功能：                                
        **   1.查询                                     
        **   2.更改个人信息（暂不支持）
        **   3.添加人名(admin)
        **   4.更改积分（admin）
        **   5.除名社员（危）
        **   6.退出                                 
        ***********************************************
    """)

def inputdata():    
    with open('datacenter.csv', newline='') as csvfile:
        reader= csv.DictReader(csvfile)
        dataList=[]
        for row in reader:
            dataList.append(row)  #将每一个人的信息存为一个字典
    return dataList   #再将每一个字典存入列表
        


def outputdata(data):
    with open('datacenter.csv', 'w', newline='') as FF:
        fieldnames = ['\ufeffid','classNum','name','score','div']
        writer = csv.DictWriter(FF, fieldnames=fieldnames)
        #write changes to the file
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    



PASSWORD='1111'
def adminTest():
    psw=input("请输入密码：")
    if psw==PASSWORD:
        return True
    else:
        return False

def consult():
    dataList=inputdata()
    findNameVal=input("请输入姓名： ")
    for x in dataList:
        if x['name']==findNameVal:
            print("个人信息:\n姓名："+x['name']+"\n班级："+x['classNum']+"\n部门："+x['div']+"\n当前积分："+x['score'])
            #output
            break


def adminAdd():
    res=adminTest()
    if res:
        dataList=inputdata()
        inname=input('name:')
        inclass=input("class:")
        inscore=0
        indiv=input('division:')
        newrow={'\ufeffid':'00NAN','classNum':inclass,'name':inname,'score':inscore,'div':indiv}
        #start to loadin the data@!#
        # dataList=inputdata()
        dataList.append(newrow)
        outputdata(dataList)

        # findNameVal=input("请输入姓名： ")
        # for x in dataList:
        #     print(x)
        #     if x['name']==findNameVal:
        #         print("个人信息:\n姓名："+x['name']+"\n班级："+x['classNum']+"\n部门："+x['div']+"\n当前积分："+str(x['score']))
        #         #output
        #         break

    else:
        print("login error")

def adminAlterif():
    res=adminTest()
    if res:
        dataList=inputdata()
        inname=input('name:')
        altscore=int(input("加分/减分分数（减分直接用负数表示）："))
        for x in dataList:
            if x['name']==inname:
                #m=input("删除以下社员？输入y确认\n姓名："+x['name']+"\n班级："+x['classNum']+"\n部门："+x['div']+"\n当前积分："+str(x['score']))
                #if m=='y':
                x['score']=str(int(x['score'])+altscore)
                break
        outputdata(dataList)
    else:
        print("login error")



def adminKillStalin():
    res=adminTest()
    if res:
        dataList=inputdata()
        inname=input('name:')
        for x in dataList:
            if x['name']==inname:
                #m=input("删除以下社员？输入y确认\n姓名："+x['name']+"\n班级："+x['classNum']+"\n部门："+x['div']+"\n当前积分："+str(x['score']))
                #if m=='y':
                dataList.remove({'\ufeffid':x['\ufeffid'],'classNum':x['classNum'],'name':x['name'],'score':x['score'],'div':x['div']})
                break
        outputdata(dataList)
    else:
        print("login error")

