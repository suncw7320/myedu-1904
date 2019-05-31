import json
# #字典以{  }包起来 , : 前面是key ,后面是value ; 多个键值对用 逗号分隔开
# adict = {'username':'admin',"password":"123456"}
# #字典是无序的,他没有索引,只能通过key  去访问value,并且key  不能重复
# # def dict_sel():
# #     print(adict['username'])
# #修改
# # def dict_updat():
# #     adict['username'] = 'scw'
# #     print(adict)
#
# #删除字典里面的键值对
# def dict_del():
#     adict.pop('username')
#     print(adict)
# #增加字典里面的键值对
# # def dict_add():
# #     adict['age'] = 25
# #     print(adict)
# #     bdict = {'list':[1,2,3],'tuple':(1,2,4)}
# #合并方式一: 将bdict 添加进 adict
#     # adict.update(bdict)
#     # print(adict)
# #合并方式二 : 将adict 和 bdict 合并,新生成一个dict
#     cdict = {'password':'7777777','class':'1904'}
# #注意第二个字典参数前  要加  **
#     ddict = dict(adict,**cdict)
#     print(adict)
#
# #字典和字符串的转换
# def dict_zhuanhuan():
#     print(type(adict))
#     # json.dumps(adict) 字典 转换成 字符串 , ensure_ascii=False : 防止中文乱码
#     str_dict = json.dumps(adict,ensure_ascii=False)
#     print(str_dict)
#     print(type(str_dict))
#
#     dict_str='{"username": "卡见风使舵", "password": "123456"}'
#     # json.loads(dict_str)  字符串 转换 成字典
#     json_loads = json.loads(dict_str)
#     print(type(json_loads))
# 题: 新建一个字典变量,里面有两个键值对,通过key访问一个值,删除一个键值对,添加一个键值对,更改任意一个值,再新建一个字典,将两个合并
mdict = {'username':'admin',"password":"123456"}
def dict_sel():
    print(mdict['username'])
    print(mdict)
def dict_del():
    mdict.pop('username')
    print(mdict)
def dict_noo():
    mdict['username']='suncw'
    print(mdict)
def dict_add():
    vdict = {'lk':'1,2,3','nc':'2,3,4'}
    mdict.update(vdict)
    print(mdict)


#
# if __name__ == '__main__':
#     # dict_sel()
#     # dict_updat()
#     # dict_del()
#     # dict_add()
#     dict_zhuanghuan()



# bdict = {'username':'admin',"password":"23456"}
# def j_dict():
#     print(bdict['username'])
# def k_dict():
#     bdict.pop('username')
#     print(bdict)
# def l_dict():
#     bdict['age']=30
#     print(bdict)
# def c_dict():
#     bdict['username']='suncw'
#     print(bdict)
#
# def n_dict():
#     ndict = {"class":"1904"}
#     bdict.update(ndict)
#     print(bdict)
if __name__ == '__main__':
    dict_sel()
    dict_del()
    dict_noo()
    dict_add()
    # j_dict()
    # k_dict()
    # l_dict()
    # c_dict()
    # n_dict()