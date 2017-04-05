+ 字典中键值对的值为列表时，没有就添加，有就append有没有更优雅的办法？有！通过collections类，可以为每个键值对的值取默认值！marvelous！
+ 可以适当关注Submissions中的Run Time，目前数字不太理想，基本都是50%以下
+ 对于python中继承和__init__方法的理解
    + 方法__init__在实例创建后调用，并不是构造方法，真正的构造方法是__new__
    + 定义了__init__方法后会覆盖掉父类的__init__，并不会再次调用父类__init__
    + 新建对象时，参数会被传至__init__方法如下
        
        ```
            class test():
                def __init__(self,name):
                    self.name = name
            obj = test("name")
        
        ```
+ 很差劲！一方面只比3.18%的人高，另一方面通过率20%表示很多人提交5次救过了！！！
+ collections为字典的每个值取默认值，set的add方法为值集合中添加元素替代append方法，dsicard方法代替remove等方法
+ set真的很好用，一方面没有list的缺元素的问题，另一方面没有字典的，在**不需要索引**的情况下尤为使用
+ 判断是否已存在可以用len==1的方法
+ set、list、dict都可以用len函数、random.choice方法和pushpop方法，这三种数据结构有相似之处
+ set写法：set([])

+ 删除的时候把最后一位放在缺的位置上！！这点是我完全没想到的
