import time
import random
import re
from fractions import Fraction
from math import gcd
# 📚 1. 元素字典（118个元素）
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

SUB_MAP = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")   #  2. 下标美化
def to_subscript(eq_str):
    if eq_str.startswith("喵呜") or eq_str.startswith("解析出错"):
        return eq_str
    return re.sub(r'([A-Z][a-z]?|\))(\d+)', lambda m: m.group(1) + m.group(2).translate(SUB_MAP), eq_str)

TOKEN_REGEX = re.compile(r'[A-Z][a-z]?|\d+|\(|\)')  # 🧠 3. 词法分析器与递归下降解析器

def parse_formula(formula):
    tokens = TOKEN_REGEX.findall(formula)
    if "".join(tokens) != formula:
        raise ValueError(f"无法识别的字符或大小写规范错误: {formula}")
        
    pos = 0
    def parse_group():
        nonlocal pos
        counts = {}
        while pos < len(tokens):
            t = tokens[pos]
            if t == ')':
                break
            if t == '(':
                pos += 1
                inner = parse_group()
                if pos >= len(tokens) or tokens[pos] != ')':
                    raise ValueError(f"括号不匹配: {formula}")
                pos += 1
                n = 1
                if pos < len(tokens) and tokens[pos].isdigit():
                    n = int(tokens[pos])
                    pos += 1
                for e, c in inner.items():
                    counts[e] = counts.get(e, 0) + c * n
            elif t.isdigit():
                raise ValueError(f"数字位置错误: {formula}")
            else:
                pos += 1
                n = 1
                if pos < len(tokens) and tokens[pos].isdigit():
                    n = int(tokens[pos])
                    pos += 1
                counts[t] = counts.get(t, 0) + n
        return counts

    result = parse_group()
    if pos != len(tokens):
        raise ValueError(f"括号不匹配: {formula}")
    return result
def solve_linear_system(matrix, num_vars): #  4. 矩阵求解 (RREF + 零空间基)
    A = [[Fraction(x) for x in row] for row in matrix]
    rows = len(A)
    cols = num_vars
    pivots = []
    r = 0
    for c in range(cols):
        pivot_row = -1
        for i in range(r, rows):
            if A[i][c] != 0:
                pivot_row = i
                break
        if pivot_row == -1:
            continue
        A[r], A[pivot_row] = A[pivot_row], A[r]
        factor = A[r][c]
        A[r] = [x / factor for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][k] - f * A[r][k] for k in range(cols)]
        pivots.append(c)
        r += 1
        if r == rows:
            break

    for i in range(r, rows):
        if any(A[i][k] != 0 for k in range(cols)):
            return None, "原子不守恒（方程组不相容）"

    free_vars = [c for c in range(cols) if c not in pivots]
    if not free_vars:
        return None, "只有零解（无配平可能）"
    
    j = free_vars[0]
    base = [Fraction(0)] * cols
    base[j] = Fraction(1)
    
    for i, p in enumerate(pivots):
        base[p] = -A[i][j]
        
    denominators = [x.denominator for x in base]
    lcm_val = 1
    for d in denominators:
        lcm_val = lcm_val * d // gcd(lcm_val, d)
    
    int_coeffs = [int(x * lcm_val) for x in base]
    final_gcd = 0
    for c in int_coeffs:
        final_gcd = gcd(final_gcd, abs(c))
    int_coeffs = [c // final_gcd for c in int_coeffs]
    
    return int_coeffs, "配平成功"


def balance_equation(equation_str): # 5. 终极配平引擎（严格模式）
    try:
        eq = equation_str.replace(" ", "").replace("->", "=").replace("→", "=")
        if "=" not in eq:
            return "喵呜，请输入包含等号的化学方程式！"
        
        reactants_str, products_str = eq.split("=")
        reactants = reactants_str.split("+")
        products = products_str.split("+")
        
        parsed_reactants = [parse_formula(f) for f in reactants]
        parsed_products = [parse_formula(f) for f in products]
        
        all_elements = set()
        for d in parsed_reactants + parsed_products:
            all_elements.update(d.keys())
        elements = sorted(list(all_elements))
        
        num_r, num_p = len(reactants), len(products)
        matrix = []
        for el in elements:
            row = [d.get(el, 0) for d in parsed_reactants] + [-d.get(el, 0) for d in parsed_products]
            matrix.append(row)
            
        coeffs, msg = solve_linear_system(matrix, num_r + num_p)
        if coeffs is None:
            return f"喵呜，{msg}，可能不遵守原子守恒哦~"
        
        res_r = [(str(c) if c != 1 else "") + reactants[i] for i, c in enumerate(coeffs[:num_r])]
        res_p = [(str(c) if c != 1 else "") + products[i] for i, c in enumerate(coeffs[num_r:])]
        
        return " + ".join(res_r) + " = " + " + ".join(res_p)
        
    except Exception as e:
        return f"喵呜，解析出错了：{str(e)}"

a = 0  #  6. 主程序入口
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
            if 回到 == "回主页": break
            if 回到 == "回到上一级": break
            while True:
                if 回到 == "回到上一级": break
                if 回到 == "回主页": break
                print("哼哼，你说吧。(ฅ⁍̴̀◊⁍̴́)و ̑̑", end="")
                a = input("")
                
                if a == "A" or a == "a":
                    print("无限次数???")
                    print("好的呢，喵~٩(•̤̀ᵕ•̤́๑)ᵒᵏᵎᵎᵎᵎ")
                    while True:
                        if 回到 == "回主页": break
                        if 回到 == "回到上一级": break
                        print("行，本喵，我先想个数字")
                        print("你要多少范围？只能正整数哦 喵~")
                        while True:
                            try:
                                x = int(float(input("起始数字:")))
                                y = int(float(input("末尾数字:")))
                                break
                            except:
                                print("请输入有效的数字 喵~")
                        if x > y: x, y = y, x
                        随机数 = random.randint(x, y)
                        print("好，本喵想好了，相信我你绝对猜不到^⎚˕⎚^")
                        print("哼哼，你猜吧。(ฅ⁍̴̀◊⁍̴́)و ̑̑")
                        猜的次数 = 0
                        while True:
                            s = input("猜的数字:")
                            if s in ["退出", "⑩", "十", "+"]:
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
                                    print("PS:本喵现在支持大小写了 喵~")
                                    作弊 = input("请输入选项:")
                                    if 作弊 in ["A", "a"]:
                                        print("本局答案为", 随机数, "没有想到吧 喵~՞˶•⩊•˶՞ಣ")
                                    elif 作弊 in ["B", "b"]:
                                        print("你猜了", 猜的次数, "次 喵~")
                                    elif 作弊 in ["C", "c"]:
                                        while True:
                                            try:
                                                改猜的次数 = input("改猜的次数:")
                                                猜的次数 = int(float(改猜的次数))
                                                print("猜的次数已改为", 猜的次数, "喵~")
                                                break
                                            except:
                                                print("数字!!! ⁽⁽(੭ꐦ •̀Д•́ )੭*⁾⁾喵~")
                                    elif 作弊 in ["D", "d"]:
                                        print("好的呢，马上回到猜数字环节 喵~")
                                        s = input("请输入:")
                                        break
                                    else:
                                        print("你要干啥？咱只有这几个选项 喵~")
                            try:
                                玩家猜的 = eval(s)
                                if 玩家猜的 < 随机数:
                                    print("猜小了 喵~请重新输入")
                                    猜的次数 += 1
                                if 玩家猜的 > 随机数:
                                    print("猜大了 喵~请重新输入")
                                    猜的次数 += 1
                                if 玩家猜的 == 随机数:
                                    猜的次数 += 1
                                    print("对了，和本喵一样聪明绝顶")
                                    print("你猜了", 猜的次数, "次")
                                    if 猜的次数 == 1: print("Oh, my god.<(ºOº)> 居然一次就过了!!!")
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
                        if 回到 == "回主页": break
                        elif 猜的次数 != 0:
                            有限次数猜数字尝试次 = 1
                            print("你要尝试多少次呢？")
                            try:
                                有限次数猜数字尝试次 = int(float(input("尝试次数:")))
                                while True:
                                    if 猜的次数 <= 0:
                                        print("你输了 喵~(｡í ˰ ì｡)")
                                        break
                                    if 回到 == "回主页": break
                                    print("你要多少范围？只能正整数哦 喵~")
                                    while True:
                                        try:
                                            x = int(float(input("起始数字:")))
                                            y = int(float(input("末尾数字:")))
                                            break
                                        except:
                                            print("请输入有效的数字 喵~")
                                    if x > y: x, y = y, x
                                    随机数 = random.randint(x, y)
                                    print("本喵，我已想好一个数字，请猜")
                                    猜的次数 = 有限次数猜数字尝试次
                                    while 猜的次数 > 0:
                                        s = input("请输入:")
                                        if s in ["退出", "⑩", "十", "+"]:
                                            回到 = "回主页"
                                            break
                                        if s in ["qq", "QQ"]:
                                            print("ok!!! ᗜ֊ᗜ")
                                            while True:
                                                print("A. 显示答案 B. 显示剩余已猜次数 C. 控制剩余已猜次数 D. 回到猜数字")
                                                作弊 = input("请输入:")
                                                if 作弊 in ["A", "a"]:
                                                    print("答案是:", 随机数)
                                                elif 作弊 in ["B", "b"]:
                                                    print("剩余已猜次数:", 猜的次数)
                                                elif 作弊 in ["C", "c"]:
                                                    try:
                                                        猜的次数 = int(float(input("请输入新的剩余次数 喵~:")))
                                                        print(f"次数已修改为 {猜的次数} 喵~")
                                                    except: print("请输入数字 喵~")
                                                elif 作弊 in ["D", "d"]:
                                                    s = input("请输入猜的数字:")
                                                    break
                                        try:
                                            玩家猜的 = eval(s)
                                            if 玩家猜的 < 随机数:
                                                print("小了 喵~")
                                                猜的次数 -= 1
                                                print(f"你还剩 {猜的次数} 次机会 喵~")
                                            elif 玩家猜的 > 随机数:
                                                print("大了 喵~")
                                                猜的次数 -= 1
                                                print(f"你还剩 {猜的次数} 次机会 喵~")
                                            elif 玩家猜的 == 随机数:
                                                猜的次数 -= 1
                                                print("猜对了 喵~")
                                                print("你剩余次数为", 猜的次数, "次")
                                                猜的次数 = 有限次数猜数字尝试次 - 猜的次数
                                                print("你一共尝试猜了", 猜的次数, "次")
                                                print("你之前设置的次数为", 有限次数猜数字尝试次, "次")
                                                回到 = "回主页"
                                                break
                                        except:
                                            print("请输入数字 ⁽⁽(੭ꐦ •̀Д•́ )੭*⁾⁾喵~")
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
            学科 = input("请输入: ")
            
            if 学科 == "A" or 学科 == "a":
                while True:
                    print()
                    print("A.元素查询")
                    print("B.方程式配平")
                    print("Q.返回")
                    化学 = input("请输入: ")
                    
                    if 化学 == "A" or 化学 == "a":
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
                        print("ok 了，马上开始配平 喵~")
                        print("【重要提示】为了保证计算准确，请严格遵守化学元素符号规范：")
                        print("  • 首字母大写，第二个字母小写（如 Na, Fe, Mn, CO2）")
                        print("  • 正确书写分子（如氧气写 O2，铁写 Fe）")
                        print("  • 输入 q 或 Q 退出配平模式")
                        while True:
                            原始式子 = input("请输入未配平的方程式：")
                            if 原始式子 == "q" or 原始式子 == "Q":
                                print()
                                print("已退出配平模式 喵~")
                                print()
                                break
                            if not 原始式子:
                                continue
                            配平结果 = balance_equation(原始式子)
                            print(f"喵~ 配平结果：{to_subscript(配平结果)}")
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
