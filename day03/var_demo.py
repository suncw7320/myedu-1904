
# 声明一个全局变量
avra = '再见'
def d1():
    #可以使用全局变量
    print(avra)

    # 在方法内部声明的变量.只能在方法内部使用
    bvra = '一般般'

def d2():
    # 无法使用其它方法内声明的变量
    print(bvra)

# 在方法内  对全局变量重新赋值, 要先用global 引用全局变量
def d3():
    global avar
    avar = '告辞'

if __name__ == '__main__':
    d1()
    d3()
    d1()
