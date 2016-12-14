#coding=utf-8
# class Person :
#     __name = 'happy'
#     def getName(self):
#         return self.__name
#     def  __init__(self,tall,weight):
#         self.tall = tall
#         self.weight = weight
#
#
# p = Person("170","170")
# print p.getName()
# print p.tall


class cafeteria:
    def __init__(self, cafe_name, food_type , start_time = 8):
        """餐厅名称，菜的种类，每天的开始开放时间"""
        self.cafe_name = cafe_name
        self.food_type = food_type
        self.start_time =start_time
        self.now_time = start_time
        self.p_num = 0
        self.cafe_info()
    def cafe_info(self):
        """打印餐厅实时信息"""
        print "欢迎光临%s,您是第%s客人，我们有%s的菜系，请尽情享用"% (self.cafe_name,self.p_num,self.food_type)

    def incease_p(self,now_time=0,p_num_new=0):
        """根据时间段来增加人数"""

        if(now_time>=self.now_time and p_num_new>=0):
            self.now_time = now_time
            self.p_num +=p_num_new
            # self.cafe_info()
        else:
            print "error time or people number"
    def rename_cafe(self,new_name):
        self.cafe_name = new_name
        self.cafe_info()
    def refresh_food_type(self,new_food_type):
            self.food_type = new_food_type
            self.cafe_info()


my_cafe = cafeteria("friday_eater","-浙菜,粤菜,湘菜-",12)
my_cafe.cafe_info()
my_cafe.incease_p(9,3)
my_cafe.incease_p(12,2)
my_cafe.incease_p(12,-3)
my_cafe.incease_p(13,3)
my_cafe.incease_p(12,3)
my_cafe.refresh_food_type("-随便-")
my_cafe.rename_cafe(" &*& ")
# my_cafe.__init__()