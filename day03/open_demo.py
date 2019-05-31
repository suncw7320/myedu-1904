
def open_write():
    # open(文件地址文件名,打开方式)
    # w+ : 写入时覆盖原有内容
    text_io = open('test.text','w+')
    for i in range(5):
        text_io.write('哈哈哈呵呵呵\n')

def open_writel():
    # open (文件地址文件名,打开方式)
    # a+ : 写入时追加内容
    text_io = open('../test.text','a+')
    for i in range(5):
        text_io.write('嘻嘻嘻\n')
def open_read():
    text_io = open('test.text','r')
    # 读取所有行,返回一个list
    # print(text_io.readlines)

    # readlines() 读取一行
    print(text_io.readline())
if __name__ == '__main__':
    open_write()
    open_writel()
    open_read()