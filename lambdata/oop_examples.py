class BareMinimumClass:
    pass
 

class Complex:
    def __init__(self, realpart, imagpart):

         """Constructer for complex numbers.
         complex numbers are part real, part imaginary.
         Imaginary numbers are roots of negative numbers.
         """

         self.r = realpart
         self.i = imagpart



    def add(self, other_complex):
         self.r += other_complex.r
         self.i += other_complex.i         

    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)     


class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def receive_upvotes(self):
        self.upvotes += 1

    def is_popular(self):
        return self.upvotes > 100


if __name__ == '__main__':
    # Demo code if you run 'python oop_example.py'
    # Example 0
    b = BareMinimumClass()
    # Example 1
    num1 = Complex(3, -5)
    num2 = Complex(-1, 6)
    num1.add(num2) # what should num1 be after?
    print(num1.r, num1.i)
    # Example 2
    user1 = SocialMediaUser('erle', 'jax')
    user2 = SocialMediaUser('John', 'New York', upvotes=50)
    user3 = SocialMediaUser('Jhon Doe', 'Anytown, USA')
    print(user2.is_popular()) # False
    for _ in range(75):
        user2.receive_upvotes()
    print(user2.is_popular()) # True


class Animal:
    """General representation of animals."""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type
    def run(self):
        return 'Vroom!'
    def eat(self, food):
        return food + ' are delicious, yum!'
class Tiger(Animal):
    pass




import math, sys;
def example1():
    ####This is a long comment. This should be wrapped----> 
    #### to fit within 72 characters.
    some_tuple=(   1,2, 3,'a'  );
    some_variable={'long':'Long code lines should be wrapped within 79 characters.',
    'other':[math.pi, 100,200,300,9876543210,'This is a long string that goes on'],
    'more':{'inner':'This whole logical line should be wrapped.',some_tuple:[1,
    20,300,40000,500000000,60000000000000000]}}
    return (some_tuple, some_variable)
def example2(): return {'has_key() is deprecated':True}.has_key({'f':2}.has_key(''));
class Example3(   object ):
    def __init__    ( self, bar ):
     #Comments should have a space after the hash.
     if bar : bar+=1;  bar=bar* bar   ; return bar
     else:
                    some_string = """
                       Indentation in multiline strings should not be touched.
Only actual code should be reindented.
"""
                    return (sys.path, some_string)