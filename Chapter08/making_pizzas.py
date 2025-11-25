# import make_pizza 导入一整个模块
# import make_pizza as mp 也可以使用mp给模块指定别名
# from pizza import * 导入模块中的所有函数
from make_pizza import make_pizza # 导入一个模块的特定函数
# from make_pizza import make_pizza as mp # 使用as给函数指定别名
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
