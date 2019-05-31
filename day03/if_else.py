def if_demo():
    # True 对
    # Llase 错

    a = 2<3

    if a :
        print('a 是 True')
    else:
        print('a 是 Flase')

def elif_demo():
    a =4
    # = 是赋值  ,  == 是  判断相等
    if a==1:
        print('a是1')   #  判断 a 是否等于1
    elif a==2:
        print('a是2')   #  判断 a 是否等于2
    elif a==3:
        print('a是3')    #  判断 a 是否等于3
    elif a==4:
        print('a是4')    #  判断 a 是否等于4
    else:
        print('a不是1,2,3,4')


if __name__ == '__main__':
    # if_demo()
    elif_demo()