if __name__ == '__main__':
    # try 和 except 中间 写可能会出错的代码
    # 如果出错 则执行 except 里面的代码
    # 不出错 不会执行 except里面的代码
    # 不管出不出错 都不会影响其它代码的执行
    # 这个叫异常处理

    try:
        print('错误之前')
        a=5/0
        print('错误之后')
    except:
        print('报错后')
        print('123456')