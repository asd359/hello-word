#coding:utf-8
class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.reading = 200000
    def get_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_course(self):
        """打印一条指出汽车里程的消息"""
        print 'this car has '+str(self.reading)+' miles on it.'
    def update_course(self,mileage):
        """将里程表读数设置为指定的值"""
        if mileage >= self.reading:
            self.reading = mileage
        else:
            print "you can't roll back an course"
    def increment(self,kilometer):
        """将里程表读数增加指定的量"""
        if kilometer >= 0:
            self.reading += kilometer
        else:
            print "you can't use negative number！"



class Battery:
    """一次模拟电动车电瓶的简单尝试"""
    def __init__(self,battery_size = 60):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print "this car has a "+str(self.battery_size)+"-kwh battery."
    def get_range(self):
        """打印一条描述电瓶续航里程的信息"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size ==85:
            range = 270
        else:
            range = 100
        message = "this car can go approximately "+str(range)
        message += "miles on a full charge"
        print message


class ElectricCar(Car,object):
    """模拟电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性，再初始化电动汽车特有的属性"""
        super(ElectricCar,self).__init__(make,model,year)
        self.battery = Battery()



