import time
import random
回到=0
a=0#用于看你是要干嘛的呢
式子=0#之后计算用的一个变量)
print("《第一版不知道目地的代码堆》Ϟ(๑⚈ ․̫ ⚈๑)⋆")#2026年9月19日 周六 23:06起始
print("你好")
print("加载中")
print("一般不超2s(秒)")
time.sleep(0.6)#等0.6秒，太快就崩了
print("这里是 Python 欢迎")
while True:
     回到=0
     print("您目前为止想做些什么呢？ ദ്ദി◝ ⩊ ◜.ᐟ")
     print("现在的简单功能请您选择")
     print("①计算②猜数字[新] (别忘了按回车哦)")
     a=input("")#input("里面用户端输地")
     if a == "①" or a == "一" or a == "1":
         while True:
                  if a =="十" or a == "退出" or a == "⑩"or a=="+":
                      break #第二次退                
                  print("好的呢₍ᐢ⸝⸝› ̫‹⸝⸝ᐢ₎喵~")
                  time.sleep(0.2)
                  print ("开始执行程序中请耐心等待喵~")
                  print("初始化中")#动画
                  print("正在加载中:")
                  for i in range(11):         #动画否则无聊
                      print(f"      {i*10}%", end="")    
                      time.sleep(0.01)
                  print("")
                  print ("好了喵~")
                  print("耶，现在主人可以输入式子了呢，喵~")
                  while True :                     
                      print("说吧喵~")   
                      print("提示喵~ฅ՞Ⱉ՞ฅ ྀི按⑩可回主菜单")
                      式子=input("")#输式子   
                      a=式子           
                      if a == "退出" or a == "⑩" or a =="十"or a=="+":
                          break #第一次退
                      else:
                          try:
                              答案=eval(式子)
                              print("≽^⚈⩊⚈^≼答案是", 答案, "喵~") 
                          except:                              
                               print("？？？暂时跳过喵~(˵¯͒⌢͗¯͒˵)我才不是不会呢，真的！没有骗你喵~")                                        
                               print("")
                               print("")  
                               
                               
                               
     elif a ==  "2" or a =="②"  or a =="二":            
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
                          print("哼哼，你说吧。(ฅ⁍̴̀◊⁍̴́)و ̑̑",end="") #"end="不换行在同一行
                          a = input("")
                          if a == "A" or a =="a":
                            print("无限次数???")
                            print("好的呢，喵~٩(•̤̀ᵕ•̤́๑)ᵒᵏᵎᵎᵎᵎ")                          
                            while True:
                                 if 回到 == "回主页":
                                      break
                                 if 回到 == "回到上一级":
                                      break
                                 print("行，本喵，我先想个数字")
                                 print("你要多少范围？只能正整数哦 喵~")
                                 x=input("起始数字:")                           
                                 x=int(float(x))#转换为整数                                
                                 y=input("末尾数字:")
                                 y=int(float(y))#转换为整数
                                 if x>y:
                                     x,y=y,x
                                 随机数 = random.randint(x, y)                        
                                 print("好，本喵想好了，相信我你绝对猜不到^⎚˕⎚^")
                                 print("哼哼，你猜吧。(ฅ⁍̴̀◊⁍̴́)و ̑̑")
                                 猜的次数 = 0
                                 while True:
                                      s = input("")
                                      if s == "qq":#作弊代码                                           
                                            print("ok!!!")
                                            while True:
                                                
                                                 print("你要选择哪种作弊方法？≽^⚈⩊⚈^≼")
                                                 print("A查看答案")
                                                 print("B查看猜的次数")
                                                 print("C控制猜的次数")
                                                 print("D回到猜数字")
                                                 print("")
                                                 print("PS:请大写,本喵懒得弄小写的了(っ꒪ཀ꒪)っ")
                                                 print("输入其他退出作弊")
                                                 print("")
                                                 作弊 = input("请输入:") 
                                                 if   作弊 == "A":
                                                      print("本局答案为",随机数,"没有想到吧 喵~՞˶•⩊•˶՞ಣ")
                                                      print()

                                                 elif 作弊 == "B": 
                                                      print("你猜了",猜的次数,"次 喵~") 
                                                      print()                                              

                                                 elif 作弊 == "C":
                                                      while True:
                                                        print("你猜了",猜的次数,"次 喵~") 
                                                        print("你想把你猜的记录改为多少呢？ 喵~")
                                                        print()
                                                        try:
                                                            改猜的次数 = input("改猜的次数:")
                                                            猜的次数 = int(float(改猜的次数))
                                                            print()
                                                            print("猜的次数已改为",猜的次数,"喵~")                                                       

                                                            break
                                                        except:
                                                             print("数字!!! ⁽⁽(੭ꐦ •̀Д•́ )੭*⁾⁾喵~")
                                                             print()

                                                 elif 作弊 == "D":
                                                      print("好的呢，马上回到猜数字环节 喵~")
                                                      s = 1
                                                      s = input("请输入:")
                                                      break

                                                 else:
                                                      print("???")
                                                      time.sleep(1)
                                                      print("你要干啥？")
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
                                            print("你猜了",猜的次数,"次")
                                            if 猜的次数 == 1:
                                                 print("Oh, my god.<(ºOº)> 居然一次就过了!!!")
                                                 print("你的实力本喵认可了")
                                            if 猜的次数 < 1:
                                                 print("你开挂了？ (⇀‸↼‶)")
                                            print("")
                                            print("1. 6s可回主页")                                           
                                            time.sleep(1.6)                                                  
                                            回到 = "回到上一级"
                                            break
                                                                                       
                                            
                                        if s == "退出" or s == "⑩" or s =="十":                                           
                                             回到 = "回主页"
                                             break
                                      except:
                                       回到 = "回到上一级"
                                       break                       
                                                                                                                                                               
                          elif a =="B" or a =="b":
                            print("没写到这")
                            print("2s后回主页")
                            time.sleep(2)
                            回到 = "回到上一级"
                            break   
                          else:
                            print("无限次数请按A 有限次数请按B")                                                                    
       
     elif a == "10" or a == "退出" or a == "⑩" or a =="十":
                   print("ok ᗜ֊ᗜ喵~，")
                   time.sleep(2)#等2秒
                   print("")                  
     else: #输入其他不合规的东西
                print("重要的事情说三次 喵~(o｀ε´o)")
                print("才不是本喵文化水平低才不是")
                for i in range(3):#重复执行3次
                    time.sleep(0.15)
                    print ("⑩回主页！")
                print("别再忘了 喵~！")
                print("") 
                #2026.9.25.18.00第一次
