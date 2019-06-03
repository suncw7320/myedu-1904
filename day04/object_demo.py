
# 声明一个类  语法 : class  类名(父类名)
class Human(object):
    # _init_: 类的初始化方法
    # self: 代表类的本身, name,age,sex 初始化的时候,要用到的参数
    def __init__(self,name,age,sex):
        # self.name = name : 把方法中的参数  绑定给  类的属性
        self.name = name
        self.age = age
        self.sex = sex
    # 类中的方法  必须包含self 参数
    def eat(self):
        print(self.name+'在吃饭')
    def sleep(self):
        print(self.name+'在睡觉')

    # 类中的方法,可以调用其它方法,可以调用属性,除了 init 方法
    def info(self):
        print('这个人叫%s,今年%s岁,性别: %s'%(self.name,self.age,self.sex))
        self.eat()
if __name__ == '__main__':
    # 新建一个对象, 根据Human 类 新建对象
    # 对象是 类的  实例比
    girl = Human('田雨',18,'女')
    girl.eat()
    girl.sleep()
    girl.info()
