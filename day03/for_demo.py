def for_demo():
    # for (关键字) i (变量名,代表循环次数) in (关键字) range (迭代器函数)
    for i in range(5):
        print('hello world')
        print(i)
def for_demo1():
    # for (关键字) i (变量名,代表循环次数) in (关键字) range (迭代器函数)
    #两个参数时:  从第一参数开始计数,到第二个参数的前一位  停止
    for i in range(5,10):
        print('hello world')
        print(i)
def for_demo2():
    # 三个参数时:  从第一个参数开始计数,到第二个参数的前一位 停止 . 每次循环 递增 参数三(步长)
    for i in range(5,10,2):
        print(i)
    # 当步长为负数时, 第一个参数  要比第二个参数 大
    for i in range(15,7,-2):
        print(i)
if __name__ == '__main__':
    for_demo2()