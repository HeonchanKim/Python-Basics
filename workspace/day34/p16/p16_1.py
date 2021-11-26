#%% Person 클래스 메소드
class Person:
    population = 0
    
    def __init__(self, name):
        self.name = name
        Person.population += 1
        print("{} is born".format(self.name))
    
    def __del__(self):
        Person.population -= 1
        print("{} is dead".format(self.name))
        
    @classmethod
    def get_poppulation(cls):
        return cls.population
    
man = Person("james")
woman = Person("emily")
print("전체 인구수 : {}명".format(Person.get_poppulation()))
del man
print("전체 인구수 : {}명".format(Person.get_poppulation()))

    
    
    