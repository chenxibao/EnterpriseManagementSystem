from tkinter import *
from pystrich.ean13 import EAN13Encoder
from string import digits
import os,time,string, random, tkinter, qrcode
import tkinter.filedialog
import tkinter.messagebox
import tkinter

root = tkinter.Tk() #tkinter模块为python标准的图形界面接口。本代码的目的是建立根窗口
#初始化数据
number = "1234567890"
letter = "ABCDEFGHIJKLMNOPQRSTVUWXYZ1234567890"
allis = "1234567890ABCDEFGHIJKLMNOPQRSTVUWXYZabcdefghijklmnopqrstvuwxyz!@#$%^&*()_+"
i = 0
randstr = []
fourth = []
fifth = []
randfir = ""
randsec = ""
randthr = ""
str_one = ""
strone = ""
strtwo = ""
nextcard = ""
userput = ""
nres_letter = ""

def mainmenu():
    print("""\033[1;35m
    ***************************************************************
                         企业编码生成系统
    ***************************************************************
    
            1.生成6位数字防伪编码（213563型）
            2.生成9位系列产品数字防伪编码（879-335439型）
            3.生成25位混合产品序列号（B2R12-N7TE8-9IET2-FE350-DW2K4型）
            4.生成含数据分析功能的防伪编码（5A61M0583D2）
            5.智能批量生成带数据分析功能的防伪码
            6.后续补加生成防伪码（5A61M0583D2）
            7.EAN-13条形码批量生成
            8.二维码批量输出
            9.企业粉丝防伪码抽奖
            0.退出系统      
    =================================================================
    说明：通过数字键选择菜单
    =================================================================
    \033[0m""")
#通过循环控制用户对程序功能的选择
    while i < 9:
        #调用程序进入主页面
        mainmenu()
        #键盘输入需要操作的选项
        choice = input("\033[1;32m   请输入您需要操作的菜单选项：\33[0m")
        if len(choice) != 0:
            choice = input_validation(choice) #验证输入的是否是数字
            if choice ==  1:
                #如果输入大于0的整数，调用scode1()函数生产防伪码
                scode1(str(choice))
            #选择菜单2，调用scode2()函数生成9位系列产品数字防伪编码
            if choice == 2:
                scode2(choice)
            #选择菜单3，调用scode3()函数生成25位混合产品序列号
            if choice == 3:
                scode3(choice)
            #选择菜单4，调用scode4()函数生成含数据分析功能的防伪编码
            if choice == 4:
                scode4("",choice)
            # 选择菜单5，调用scode5()函数智能批量生成带数据分析功能的防伪码
            if choice == 5:
                scode5(choice)
            # 选择菜单6，调用scode6()函数后续补加生成防伪码
            if choice == 6:
                scode6(choice)
            #选择菜单7，调用scode7()函数EAN-13条形码批量生成
            if choice == 7:
                scode7(choice)
            #选择菜单8，调用scode8()函数二维码批量输出
            if choice == 8:
                scode8(choice)
            #选择菜单8，调用scode8()函数二维码批量输出
            if choice == 9:
                scode9(choice)
            # 选择菜单8，调用scode8()函数二维码批量输出
            if choice == 0:
                i = 0
                print("正在退出系统")
        else:
            print("\033[1;31;40m   输入非法，请重新输入！！\003[0m")
            time.sleep(2)

def input_validation(insel):
    if str.isdigit(insel):
        if insel == 0:
            print("\033[1;31;40m   输入非法，请重新输入！！\033[0m")
            return 0
        else:
            return insel
    else:
        print("\033[1;31;40m   输入非法，请重新输入！！\033[0m")
        return 0

#实现生成6位数字防伪码
def scode1(schoice):
    #调用inputbox函数对输入数据进行非空、合法性判断
    incount = inputbox("\033[1;32m   请输入您要生成的防伪码的数量：\33[0m",1,0)
    while int(incount) == 0: #如果输入的字母或者数字0，则要求重新输入
        incount = inputbox("\033[1;32m   请输入您要生成的防伪码的数量：\33[0m",1,0)
    randstr.clear() #清空保存批量防伪码信息的变量randstr
    for j in range(int(incount)):#根据输入防伪码的数量循环批量生成防伪码
        randfir = "" #设置存储单条防伪码的变量为空
        for i in range(6):
            randfir = randfir+random.choice(number)#产生数字随机因子
        randfir = randfir + "\n" #在单条防伪码后面添加转义换行符“\n”，使验证码单条列显示
    randstr.append(randfir) #将单条防伪码加到保存批量生成防伪码的变量randstr
    #调用wfile（）函数，实现生成防伪码屏幕输出和文件输出
    wfile(randstr,"scode"+str(schoice)+".txt","","已生成6位防伪码共计：","codepath")

def scode2(schoice):
    ordstart = inputbox("\033[1;32m  请输入系列产品的数字起始号（3位）：\33[0m",3, 3)
    # 如果输入的系列产品起始号不是三位数，则要求重新输入
    while int(ordstart) == 0:
        ordstart = inputbox("\033[1;32m  请输入系列产品的数字起始号（3位）：\33[0m",1, 0)
    ordcount = inputbox("\033[1;32m 请输入产品系列的数量 ",1, 0)
    #如果输入的产品数量小于1或者小于9999，则要求重新输入
    while int(ordstart) < 1 or int(ordstart) >9999:
        ordstart = inputbox("\033[1;32m 请输入产品系列的数量 ",1, 0)
    incount = inputbox("\033[1;32m 请输入要生成的每个系列产品的防伪码数量:\33[0m",1,0)
    while int(incount) == 0:#如果输入为字母或数字0，则要求重新输入
        incount = inputbox("\033[1;32m 请输入要生成防伪码的数量:\33[0m",1,0)
    randstr.clear() #清空保存批量防伪码信息的变量randstr
    for m in range(int(ordcount)): #分类产品编号
        for j in range(int(incount)):#产品防伪码编号
            randfir = ""
            for i in range(6): #生成一个不包含类别的产品编码
                randfir = randfir + random.choice(number) #每次生成一个随机因子
            # 将生成的单条防伪码加到防伪列表里
            randstr.append(str(int(ordstart)+m)+randfir+"\n")
    #调用函数wfile(),实现生成的防伪码在屏幕输出和文件输出
    wfile(randstr,"scode"+str(schoice)+".txt","","已生成9位系列产品防伪码共计：","codepath")

#生成25位混合产品序列号函数，参数schoice设置输出的文件名称
def scode3(schoice):
    #输入要生成的防伪码的数量
    incount = inputbox("\033[1;32m 请输入要生成的25位混合产品序列号的数量：\33[0m",1,0)
    while int(incount) == 0:#如果输入非法（符号、字母或者数字0都认为是非法输入），重新输入
        incount = inputbox("\033[1;32m 请输入要生成的25位混合产品序列号的数量：\33[0m",1,0)
    randstr.clear()
    for j in range(incount):
        strone = ""
        for i in range(25):
            strone = strone+random.choice(letter)
        #将生成的防伪码每隔5位添加横线——
        strtwo = strone[:5]+ "-"+strone[5:10]+"-"+strone[10:15]+"-"+strone[15:20]+"-"+strone[20:25]+"\n"
        randstr.append(strtwo)
    wfile(randstr,"scode"+str(schoice)+".txt","","已生成25混合防伪序列码共计：","codepath")

#生成含数据分析功能的防伪码函数
def scode4(schoice):
    intype = input("\033[1;32m   请输入数据分析编号（3位字母):\33[0m",2,3)
    #验证输入是否是三个字母，判断输入是否是字母以及长度是否为3
    while not str.isalpha(intype) or len(intype) != 3:
        intype = input("\033[1;32m   请输入数据分析编号（3位字母):\33[0m", 2, 3)
    incount = inputbox("\033[1;32m 输入要生成带数据分析功能的序列防伪码的数量:\33[0m",1,0)
    #验证输入的是否大于0
    while incount == 0:
        incount = inputbox("\033[1;32m 输入要生成带数据分析功能的序列防伪码的数量:\33[0m",1,0)
    ffcode(incount,intype,"",schoice) #调用ffcode（）生成防伪码

def ffcode(scount,typestr,ismessage, schoice):
    randstr.clear()
    #按照数量生成含数据分析功能防伪码
    for j in range(int(scount)):
        strpro = typestr[0].upper()#取第一个字母，并转成大写，区域分析码
        strtype = typestr[1].upper()#取第二个字母，并转成大写，颜色分析码
        strclass = typestr[2].upper()#取第三个字母，并转成大写，批次分析码
        randfir = random.sample(number,3) #随机抽取三个防伪码的位置，不分先后
        randsec = sorted(randfir) #进行排序
        letterone = ""
        for i in range(9):
            letterone = letterone + random.choice(number)
        #将单个字母按randsec变量中存储的位置值添加到数字防伪码中，并保存到sim变量中
        sim = str(letterone[0:int(randsec[0])])+strpro+\
                str(letterone[int(randsec[0]):int(randsec[1])])+strtype+\
                    str(letterone[int(randsec[1]):int(randsec[2])])+strclass+\
                        str(letterone[int(randsec[2]):9])+"\n"
        randstr.append(sim)

    wfile(randstr,typestr+"scode"+str(schoice)+".txt",ismessage,"生成含数据分析的防伪码共计：","codepath")


def scode5(schoice):
    #设置默认打开文件
    defualt_dir = r"codeauto.mir"
    #打开文件对话框，指定打开的文件名为codeauto，扩展名为mir的文件
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Text file","*.mir")],
                                                   title=u"请选择只能批处理文件：",initialdir=(os.path.expanduser(defualt_dir)))
    codelist = openfile(file_path)#读取从文件选择对话框选中的文件
    #以换行符为分隔符
    codelist = codelist.split("\n")
    print(codelist)
    for item in codelist:#按读取的信息循环生成防伪码
        codea = item.spilt(",")[0]#分割“，”，防伪码的三位字母
        codeb = item.split(",")[1]#防伪码的数量
        ffcode(codea,codeb,"no",schoice)#批量生成防伪码


















def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:#如果文件夹不存在
        os.mkdir(path)#创建要创建的文件

def openfile(filename): #读取文件内容函数

    f = open(filename) #打开指定文件
    fllist = f.read()  #读取文件内容
    f.close()          #关闭文件
    return fllist       #返回读取的文件内容

def inputbox(showstr, showorder, length):
    instr = input(showstr) #使用input函数要求用户输入信息，showstr为输入提示文字
    if len(instr) != 0: #输入的长度不为0
        # 分成三种验证方式验证，1：数字，不限位数，大于零的整数
        if showstr == 1: #验证方式1，数字格式，不限位数，大于零的整数
            if str.isdigit(instr): #验证是否是数字
                if instr == 0: #验证是否为0，如果是0要求重新输入，返回值为“0”
                    print("\003[1;31;40m 输入为0，请重新输入！！\033[0m") #要求重新输入
                    return "0"  #函数返回值为0，为什么返回值为0呢？
                else:#如果输入正确
                    return instr
            else: #如果输入不是数字，要求用户重新输入，函数返回值为“0”
                print("\003[1;31;40m 输入非法，请重新输入！！\033[0m")
                return "0" #函数返回值为0
        if showstr ==2:#验证方式2，要求字母格式且是指定字母
            if str.isalpha(instr): #判断输入是否为字母
                if len(instr) != length: #判断输入的位数
                    print("\003[1;31;40m 必须输入"+str(length)+"个字母，请重新输入！！\033[0m")
                    return "0" #返回值为0
                else:  #如果输入的是三个字母，返回输入的字母
                    return instr  #将函数返回值设置为输入的字母
            else:
                print("003[1;31;40m 输入非法，请重新输入！！\033[0m")
                return "0"
        if showstr == 3: #验证方式3，要求数字格式且输入数字位有要求
            if str.isdigit(instr): #验证是否为数字
                if len(instr) != length: #验证输入的位数是不是制定的位数
                    print("\003[1;31;40m 必须输入"+str(length)+"个数字，请重新输入！！\033[0m")
                    return "0"
                else:
                    return instr
            else:#如果输入的不是数字
                print("003[1;31;40m 输入非法，请重新输入！！\033[0m")
                return "0"
    else:
        print("003[1;31;40m 输入为空，请重新输入！！\033[0m") #输入为空要求重新输入
        return "0" #函数返回值为0

#while函数实现读取已经生成的防伪编码，通过屏幕输出，文件输出
# def wfile(sstr, sfile, typies, smsg):
def wfile(sstr,sfile,typies,smsg,datapath):
    mkdir(datapath) #调用该函数创建文件夹
    datafile = datapath+"\\"+sfile #设置保存防伪码的文件（包含路径）
    file = open(datafile,'w') #打开保存防伪码的文件，如果文件不存在，则创建该文件
    wrlist = sstr
    pdata = "" #清空变量pdata，pdate存储屏幕输出的防伪码
    wdata = ""  #清空变量wdata,wdata存储保存到文本文件的防伪码信息
    for i in range(len(wrlist)):#按条循环读取防伪码数据
        wdata = str(wrlist[i].replace('[','').replace(']',''))#去掉字符的中括号
        wdata = wdata.replace("'","").replace("'","") #去掉字符串的引号
        file.write(str(wdata)) #写入保存防伪码的文件
        pdata = pdata + wdata #将单条防伪码存储到pdata变量
    file.close()
    print("\033[1;31m"+pdata+"\033[0m")#屏幕输出生成的防伪码信息
    if typies != "no":#是否显示信息提示框。如果typies的值为“no”，不显示
        #显示输出完成的信息提示框，显示信息包含防伪信息码的保存路径
        tkinter.messagebox.showinfo("提示",smsg+str(len(randstr))
                                    +"\n防伪码文件存放位置："+datafile)
        root = tkinter.Tk()
        root.withdraw()#关闭辅助窗口











