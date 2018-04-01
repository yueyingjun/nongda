#    流程控制   顺序执行  分支  循环执行

#    分支结构  条件结构    循环结构   迭代结构
#    单路分支  双路分支   多路分支  嵌套分支
'''
num=101

if num>=60 and num<70:
    print("及格");
elif num>=70  and num<80:
    print("还行")
elif num>=80  and num<90:
    print("良好")
elif num>=90 and num<100:
    print("优秀")
elif num==100:
    print("满分")
elif num>=0 and num<60:
    if num>=50 and num<60:
        print("继续努力")
    else:
        print("需要重修");
else:
    print("不符合规范")
  4


def 函数名 (形参)
    函数体
    函数体
    函数体
    函数体

函数名(实参)

实参 形参 -- 对应


杨辉三角   参数   改变输出的行数

9*9     参数    改变  8*8    20*20
'''

def stars(rows=5): # 形参 参数默认值
    row = 0
    #  循环每一行
    while row < rows:
        row += 1
        #  循环每一行的空格
        space = 0
        while space < rows - row:
            space += 1
            print(" ", end="")
        #  循环每一行的星星
        star = 0
        while star < 2 * row - 1:
            print("*", end="")
            star += 1

        print("")
stars()
stars(3)  # 调用函数的时候的参数 实参
stars(6)
stars(10)










