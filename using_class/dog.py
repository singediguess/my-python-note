class Dog():
    color = 'brown'
    name = 'doggy'
    def get_color(self):
        print(self.name)
        return self.color

obj = Dog()
#obj == self
print (obj.get_color())
