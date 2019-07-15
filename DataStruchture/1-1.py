
class Student:

    def __init__(self, name, id):
        # self.name = name
        self.__name = name  #private 변수 >> getter 함수로만 접근 가능
        self.id = id

    # getter함수 >> private 변수 접근 시 사용
    def get_name(self):
        # return self.name
        return self.__name

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.__name = name


s1 = Student("aaa", 100)

# 맴버변수 >> private 접근 불가
#print(s1.__name)

print(s1.get_name())
s1.set_name('aaa')
print(s1.set_name())