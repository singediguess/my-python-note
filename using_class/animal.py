class Animal():
    noise = 'grunt'
    color = 'brown'
    def get_color(self):
        return self.color
    def get_noise(self):
        return self.noise

class Dog(Animal): ###inherit from Animal!!
    hair = 'long'
    name = 'Jon'

