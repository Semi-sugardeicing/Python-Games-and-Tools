import time
import random
元素字典 = {
    "H": {"name": "氢", "mass": 1.008},   "He": {"name": "氦", "mass": 4.003},
    "Li": {"name": "锂", "mass": 6.94},    "Be": {"name": "铍", "mass": 9.012},
    "B": {"name": "硼", "mass": 10.81},    "C": {"name": "碳", "mass": 12.01},
    "N": {"name": "氮", "mass": 14.01},    "O": {"name": "氧", "mass": 16.00},
    "F": {"name": "氟", "mass": 19.00},    "Ne": {"name": "氖", "mass": 20.18},
    "Na": {"name": "钠", "mass": 22.99},   "Mg": {"name": "镁", "mass": 24.31},
    "Al": {"name": "铝", "mass": 26.98},   "Si": {"name": "硅", "mass": 28.09},
    "P": {"name": "磷", "mass": 30.97},    "S": {"name": "硫", "mass": 32.06},
    "Cl": {"name": "氯", "mass": 35.45},   "Ar": {"name": "氩", "mass": 39.95},
    "K": {"name": "钾", "mass": 39.10},    "Ca": {"name": "钙", "mass": 40.08},
    "Sc": {"name": "钪", "mass": 44.96},   "Ti": {"name": "钛", "mass": 47.87},
    "V": {"name": "钒", "mass": 50.94},    "Cr": {"name": "铬", "mass": 52.00},
    "Mn": {"name": "锰", "mass": 54.94},   "Fe": {"name": "铁", "mass": 55.85},
    "Co": {"name": "钴", "mass": 58.93},   "Ni": {"name": "镍", "mass": 58.69},
    "Cu": {"name": "铜", "mass": 63.55},   "Zn": {"name": "锌", "mass": 65.38},
    "Ga": {"name": "镓", "mass": 69.72},   "Ge": {"name": "锗", "mass": 72.63},
    "As": {"name": "砷", "mass": 74.92},   "Se": {"name": "硒", "mass": 78.97},
    "Br": {"name": "溴", "mass": 79.90},   "Kr": {"name": "氪", "mass": 83.80},
    "Rb": {"name": "铷", "mass": 85.47},   "Sr": {"name": "锶", "mass": 87.62},
    "Y": {"name": "钇", "mass": 88.91},    "Zr": {"name": "锆", "mass": 91.22},
    "Nb": {"name": "铌", "mass": 92.91},   "Mo": {"name": "钼", "mass": 95.95},
    "Tc": {"name": "锝", "mass": 98.00},   "Ru": {"name": "钌", "mass": 101.07},
    "Rh": {"name": "铑", "mass": 102.91},  "Pd": {"name": "钯", "mass": 106.42},
    "Ag": {"name": "银", "mass": 107.87},  "Cd": {"name": "镉", "mass": 112.41},
    "In": {"name": "铟", "mass": 114.82},  "Sn": {"name": "锡", "mass": 118.71},
    "Sb": {"name": "锑", "mass": 121.76},  "Te": {"name": "碲", "mass": 127.60},
    "I": {"name": "碘", "mass": 126.90},   "Xe": {"name": "氙", "mass": 131.29},
    "Cs": {"name": "铯", "mass": 132.91},  "Ba": {"name": "钡", "mass": 137.33},
    "La": {"name": "镧", "mass": 138.91},  "Ce": {"name": "铈", "mass": 140.12},
    "Pr": {"name": "镨", "mass": 140.91},  "Nd": {"name": "钕", "mass": 144.24},
    "Pm": {"name": "钷", "mass": 145.00},  "Sm": {"name": "钐", "mass": 150.36},
    "Eu": {"name": "铕", "mass": 151.96},  "Gd": {"name": "钆", "mass": 157.25},
    "Tb": {"name": "铽", "mass": 158.93},  "Dy": {"name": "镝", "mass": 162.50},
    "Ho": {"name": "钬", "mass": 164.93},  "Er": {"name": "铒", "mass": 167.26},
    "Tm": {"name": "铥", "mass": 168.93},  "Yb": {"name": "镱", "mass": 173.05},
    "Lu": {"name": "镥", "mass": 174.97},  "Hf": {"name": "铪", "mass": 178.49},
    "Ta": {"name": "钽", "mass": 180.95},  "W": {"name": "钨", "mass": 183.84},
    "Re": {"name": "铼", "mass": 186.21},  "Os": {"name": "锇", "mass": 190.23},
    "Ir": {"name": "铱", "mass": 192.22},  "Pt": {"name": "铂", "mass": 195.08},
    "Au": {"name": "金", "mass": 196.97},  "Hg": {"name": "汞", "mass": 200.59},
    "Tl": {"name": "铊", "mass": 204.38},  "Pb": {"name": "铅", "mass": 207.20},
    "Bi": {"name": "铋", "mass": 208.98},  "Po": {"name": "钋", "mass": 209.00},
    "At": {"name": "砹", "mass": 210.00},  "Rn": {"name": "氡", "mass": 222.00},
    "Fr": {"name": "钫", "mass": 223.00},  "Ra": {"name": "镭", "mass": 226.00},
    "Ac": {"name": "锕", "mass": 227.00},  "Th": {"name": "钍", "mass": 232.04},
    "Pa": {"name": "镤", "mass": 231.04},  "U": {"name": "铀", "mass": 238.03},
    "Np": {"name": "镎", "mass": 237.00},  "Pu": {"name": "钚", "mass": 244.00},
    "Am": {"name": "镅", "mass": 243.00},  "Cm": {"name": "锔", "mass": 247.00},
    "Bk": {"name": "锫", "mass": 247.00},  "Cf": {"name": "锎", "mass": 251.00},
    "Es": {"name": "锿", "mass": 252.00},  "Fm": {"name": "镄", "mass": 257.00},
    "Md": {"name": "钔", "mass": 258.00},  "No": {"name": "锘", "mass": 259.00},
    "Lr": {"name": "铹", "mass": 262.00},  "Rf": {"name": "𬬻", "mass": 267.00},
    "Db": {"name": "𬭊", "mass": 270.00},  "Sg": {"name": "𬭳", "mass": 269.00},
    "Bh": {"name": "𬭛", "mass": 270.00},  "Hs": {"name": "𬭶", "mass": 277.00},
    "Mt": {"name": "鿏", "mass": 276.00},  "Ds": {"name": "𫟼", "mass": 281.00},
    "Rg": {"name": "𬬭", "mass": 280.00},  "Cn": {"name": "鎶", "mass": 285.00},
    "Nh": {"name": "鉨", "mass": 284.00},  "Fl": {"name": "𫓧", "mass": 289.00},
    "Mc": {"name": "镆", "mass": 288.00},  "Lv": {"name": "鉝", "mass": 293.00},
    "Ts": {"name": "石田", "mass": 294.00}, "Og": {"name": "气奥", "mass": 294.00}
}
a = 0
式子 = 0

print("《第一版代码堆》Ϟ(๑⚈ ․̫ ⚈๑)⋆")
print("你好 喵~(ฅ⁍̴̀◊⁍̴́)و ̑̑")
print("加载中 喵~")
print("一般不超2s(秒)")
time.sleep(0.6)
print("这里是 Python 欢迎")

while True:
    回到 = 0
    print("您目前为止想做些什么呢？ ദ്ദി◝ ⩊ ◜.ᐟ")
    print("现在的简单功能请您选择 喵~")
    print("")
    print("①计算器功能说明:本喵可以帮你算式子，算对了就赢了喵~")
    print("②猜数字[新]功能说明:本喵会想一个数字，你来猜，猜对了就赢了喵~")
    print("③部分学习查询工具")
    print()
    print("ps别忘了按回车哦")
    a = input("")
    
    if a == "①" or a == "一" or a == "1":
        while True:
            if a == "十" or a == "退出" or a == "⑩" or a == "+":
                break
            print("好的呢₍ᐢ⸝⸝› ̫‹⸝⸝ᐢ₎喵~")
            time.sleep(0.2)
            print("开始执行程序中请耐心等待 喵~")
            print("初始化中")
            print("正在加载中:")
            for i in range(11):
                print(f"      {i*10}%", end="")
                time.sleep(0.01)
            print("")
            print("好了喵~")
            print("耶，现在主人可以输入式子了呢，喵~")
            
            while True:
                print("说吧喵~")
                print("提示喵~ฅ՞Ⱉ՞ฅ ྀི按⑩可回主菜单")
                式子 = input("")
                a = 式子
                if a == "退出" or a == "⑩" or a == "十" or a == "+":
                    break
                else:
                    try:
                        答案 = eval(式子)
                        print("≽^⚈⩊⚈^≼答案是", 答案, "喵~")
                    except:
                        print("？？？暂时跳过喵~(˵¯͒⌢͗¯͒˵)我才不是不会呢，真的！没有骗你喵~")
                        print("")
                        print("")
                        
    elif a == "2" or a == "②" or a == "二":
        print("咱们要玩哪种版本的？")
        print("无限版本？有次数限制版本？")
        print("你选吧，别说本喵玩不起^⎚˕⎚^")
        print("无限次数请按A 有限次数请按B")
        
        while True:
            if 回到 == "回主页":
                break
            if 回到 == "回到上一级":
                break
                
            while True:
                if 回到 == "回到上一级":
                    break
                if 回到 == "回主页":
                    break
                    
                print("哼哼，你说吧。(ฅ⁍̴̀◊⁍̴́)و ̑̑", end="")
                a = input("")
                
                if a == "A" or a == "a":
                    print("无限次数???")
                    print("好的呢，喵~٩(•̤̀ᵕ•̤́๑)ᵒᵏᵎᵎᵎᵎ")
                    
                    while True:
                        if 回到 == "回主页":
                            break
                        if 回到 == "回到上一级":
                            break
                            
                        print("行，本喵，我先想个数字")
                        print("你要多少范围？只能正整数哦 喵~")
                        
                        # 修复：防止输入字母崩溃
                        while True:
                            try:
                                x = input("起始数字:")
                                x = int(float(x))
                                y = input("末尾数字:")
                                y = int(float(y))
                                break
                            except:
                                print("请输入有效的数字 喵~")
                                
                        if x > y:
                            x, y = y, x
                            
                        随机数 = random.randint(x, y)
                        print("好，本喵想好了，相信我你绝对猜不到^⎚˕⎚^")
                        print("哼哼，你猜吧。(ฅ⁍̴̀◊⁍̴́)و ̑̑")
                        猜的次数 = 0
                        
                        while True:
                            s = input("猜的数字:")
                            
                            # 修复：先判断退出，再计算
                            if s == "退出" or s == "⑩" or s == "十" or s == "+":
                                回到 = "回主页"
                                break
                                
                            if s == "qq":
                                print("ok!!!")
                                while True:
                                    print("你要选择哪种作弊方法？≽^⚈⩊⚈^≼")
                                    print("A. 查看答案")
                                    print("B. 查看猜的次数")
                                    print("C. 控制猜的次数")
                                    print("D. 回到猜数字")
                                    print("")
                                    print("PS:本喵现在支持大小写了 喵~")
                                    print("输入其他退出作弊")
                                    print("")
                                    作弊 = input("请输入选项:")
                                    
                                    if 作弊 == "A" or 作弊 == "a":
                                        print("本局答案为", 随机数, "没有想到吧 喵~՞˶•⩊•˶՞ಣ")
                                        print()
                                    elif 作弊 == "B" or 作弊 == "b":
                                        print("你猜了", 猜的次数, "次 喵~")
                                        print()
                                    elif 作弊 == "C" or 作弊 == "c":
                                        while True:
                                            print("你猜了", 猜的次数, "次 喵~")
                                            print("你想把你猜的记录改为多少呢？ 喵~")
                                            print()
                                            try:
                                                改猜的次数 = input("改猜的次数:")
                                                猜的次数 = int(float(改猜的次数))
                                                print()
                                                print("猜的次数已改为", 猜的次数, "喵~")
                                                break
                                            except:
                                                print("数字!!! ⁽⁽(੭ꐦ •̀Д•́ )੭*⁾⁾喵~")
                                                print()
                                    elif 作弊 == "D" or 作弊 == "d":
                                        print("好的呢，马上回到猜数字环节 喵~")
                                        s = 1
                                        s = input("请输入:")
                                        break
                                    else:
                                        print("???")
                                        time.sleep(1)
                                        print("你要干啥？ ")
                                        print("咱只有这几个选项 喵~")
                                        print()
                                    print("")
                                    
                            try:
                                玩家猜的 = eval(s)
                                if 玩家猜的 < 随机数:
                                    print("猜小了 喵~")
                                    print("输入非数字即可退出")
                                    print("请重新输入")
                                    print("")
                                    猜的次数 += 1
                                if 玩家猜的 > 随机数:
                                    print("猜大了 喵~")
                                    print("输入非数字即可退出")
                                    print("请重新输入")
                                    猜的次数 += 1
                                    print("")
                                if 玩家猜的 == 随机数:
                                    猜的次数 += 1
                                    print("对了，和本喵一样聪明绝顶")
                                    print("你猜了", 猜的次数, "次")
                                    if 猜的次数 == 1:
                                        print("Oh, my god.<(ºOº)> 居然一次就过了!!!")
                                        print("你的实力本喵认可了 ")
                                    if 猜的次数 < 1:
                                        print("你开挂了？ (⇀‸↼‶)")
                                    print("")
                                    print("1.6s后回到上一级 喵~")
                                    time.sleep(1.6)
                                    回到 = "回到上一级"
                                    break
                            except:
                                回到 = "回到上一级"
                                break
                                
                elif a == "B" or a == "b":
                    猜的次数 = 1
                    while True:
                        if 猜的次数 <= 0:
                            回到 = "回主页"
                            break
                        if 回到 == "回主页":
                            break
                        elif 猜的次数 != 0:
                            有限次数猜数字尝试次 = 1
                            print("你要尝试多少次呢？")
                            print("自己输入吧，别说我玩不起")
                            try:
                                有限次数猜数字尝试次 = input("尝试次数:")
                                有限次数猜数字尝试次 = int(float(有限次数猜数字尝试次))
                                
                                while True:
                                    if 猜的次数 <= 0:
                                        print()
                                        print("你输了 喵~(｡í ˰ ì｡)")
                                        print("")
                                        break
                                    if 回到 == "回主页":
                                        break
                                        
                                    print("行，本喵，我先想个数字")
                                    print("你要多少范围？只能正整数哦 喵~")
                                    
                                    # 修复：防止输入字母崩溃
                                    while True:
                                        try:
                                            x = input("起始数字:")
                                            x = int(float(x))
                                            y = input("末尾数字:")
                                            y = int(float(y))
                                            break
                                        except:
                                            print("请输入有效的数字 喵~")
                                            
                                    if x > y:
                                        x, y = y, x
                                        
                                    随机数 = random.randint(x, y)
                                    print("本喵，我已想好一个数字，请猜")
                                    随机数 = random.randint(x, y)
                                    print()
                                    猜的次数 = 有限次数猜数字尝试次
                                    
                                    while 猜的次数 > 0:
                                        s = input("请输入:")
                                        
                                        # 修复：先判断退出
                                        if s == "退出" or s == "⑩" or s == "十" or s == "+":
                                            回到 = "回主页"
                                            break
                                            
                                        if s == "qq" or s == "QQ":
                                            print("")
                                            print("ok!!! ᗜ֊ᗜ")
                                            while True:
                                                print("你要选择哪种作弊方法？≽^⚈⩊⚈^≼")
                                                print("A. 显示答案")
                                                print("B. 显示剩余已猜次数")
                                                print("C. 控制剩余已猜次数")
                                                print("D. 回到猜数字")
                                                print()
                                                print("PS:请大写,本喵懒得弄小写的了(っ꒪ཀ꒪)っ")
                                                作弊 = input("请输入:")
                                                
                                                if 作弊 == "A" or 作弊 == "a":
                                                    print()
                                                    print("答案是:", 随机数, "没有想到吧 喵~՞˶•⩊•˶՞ಣ")
                                                    print()
                                                elif 作弊 == "B" or 作弊 == "b":
                                                    print()
                                                    print("剩余已猜次数:", 猜的次数)
                                                    print()
                                                elif 作弊 == "C" or 作弊 == "c":
                                                    print()
                                                    print(f"目前剩余次数: {猜的次数}")
                                                    try:
                                                        新次数 = int(float(input("请输入新的剩余次数 喵~:")))
                                                        猜的次数 = 新次数
                                                        print(f"次数已修改为 {猜的次数} 喵~")
                                                        print()
                                                    except:
                                                        print("请输入数字 喵~")
                                                elif 作弊 == "D" or 作弊 == "d":
                                                    print("好的呢，马上回到猜数字环节 喵~")
                                                    s = 1
                                                    s = input("请输入猜的数字:")
                                                    break
                                                    
                                        try:
                                            玩家猜的 = eval(s)
                                            if 玩家猜的 < 随机数:
                                                print("小了 喵~")
                                                print("请重新输入")
                                                猜的次数 -= 1
                                                print(f"你还剩 {猜的次数} 次机会 喵~")
                                                print()
                                            elif 玩家猜的 > 随机数:
                                                print("大了 喵~")
                                                print("请重新输入")
                                                猜的次数 -= 1
                                                print(f"你还剩 {猜的次数} 次机会 喵~")
                                                print()
                                            elif 玩家猜的 == 随机数:
                                                猜的次数 -= 1
                                                print("猜对了 喵~")
                                                print("你剩余次数为", 猜的次数, "次")
                                                猜的次数 = 有限次数猜数字尝试次 - 猜的次数
                                                print("你一共尝试猜了", 猜的次数, "次")
                                                print("你之前设置的次数为", 有限次数猜数字尝试次, "次")
                                                print()
                                                回到 = "回主页"
                                                break
                                        except:
                                            print("请输入数字 ⁽⁽(੭ꐦ •̀Д•́ )੭*⁾⁾喵~")
                                            print("数字!!! ⁽⁽(੭ꐦ •̀Д•́ )੭*⁾⁾喵~")
                            except:
                                print("请输入数字 ⁽⁽(੭ꐦ •̀Д•́ )੭*⁾⁾喵~")
                else:
                    print("无限次数请按A 有限次数请按B")
                    
    elif a == "3" or a == "③" or a == "三":
        学科 = 0
        while True:
            print()
            print("目前为止可以帮你的为")
            print("A.化学")
            print("B.生物学")
            print("C.物理")
            print("Q.返回")
            print()
            print("选择吧 Ϟ(๑⚈ ․̫ ⚈๑)⋆")
            学科 = input("请输入: ")
            if 学科 == "A" or 学科 == "a":
                while True:
                    print()
                    print("A.元素查询")
                    print("B.方程式配平")
                    print("Q.返回")
                    print()
                    化学 = input("请输入: ")
                    if 化学 == "A" or 化学 == "a":
                        print()
                        while True:
                            print()
                            print("ok 了，马上开始查询 喵~")
                            查询元素 = input("请输入元素: ").strip().capitalize()
                            if 查询元素 in 元素字典:
                                元素信息 = 元素字典[查询元素]
                                print(f"元素: {查询元素}")
                                print(f"名称: {元素信息['name']}")
                                print(f"原子质量: {元素信息['mass']}")
                            elif 查询元素 == "q" or 查询元素 == "Q":
                                print()
                                print("已退出")
                                print()
                                break
                            else:
                                print("未找到该元素 喵~")
                            print()
                    elif 化学 == "B" or 化学 == "b":
                        print()
                        print("方程式配平功能暂未开放 喵~")
                        print()
                    elif 化学 == "Q" or 化学 == "q":
                        print()
                        print("好的呢，马上回到主页 喵~")
                        print()
                        break
                    else:
                        print()
                        print("请输入正确的选项 喵~")
                        print()
            elif 学科 == "B" or 学科 == "b":
                print("生物学查询功能暂未开放 喵~")
                print("请耐心等待喵~")
                print()
            elif 学科 == "C" or 学科 == "c":
                print("物理查询功能暂未开放 喵~")
                print("请耐心等待喵~")
                print()
            elif 学科 == "Q" or 学科 == "q":
                print("好的呢，马上回到主页 喵~")
                break
            else:
                print("请输入正确的选项 喵~")
                print()
            

        

    #print("") 
       
    elif a == "10" or a == "退出" or a == "⑩" or a == "十":
        print("ok ᗜ֊ᗜ喵~，")
        time.sleep(2)
        print("")
        
    else:
        print("重要的事情说三次 喵~(o｀ε´o)")
        print("才不是本喵文化水平低才不是")
        for i in range(3):
            time.sleep(0.15)
            print("⑩回主页！")
        print("别再忘了 喵~！")
        print("")
        