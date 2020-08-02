import math
class Complex:


    def __init__(self, re, im):
        '''Constructor of the Complex class. '''
        self.re = re
        self.im = im


    # Assignment 3.3

    def conjugate(self):
        '''The conjugate function changes reverts signs of a complex number expression.
        If-statement to evaluate the sign of individual parts of the complex expression'''
        a = self.re
        b = self.im

        if b < 0:
            b = b * (-1)
            print("b1 ", b)
        elif b > 0:
            b = b * (-1)
            print("b2 ", b)
        print (a,b)
        return Complex(a,b)


    def modulus(self):
        '''This function calculates the modulus of a complex number.'''
        x = self.re * self.re + self.im * self.im
        absx = abs(x)
        mod = math.sqrt(absx)
        return mod


    def __add__(self, other):
        '''This function adds to numbers. Using if-statement to check what kind of
        values we are about to add. 3 possibilities: i.e int, complex, or Complex'''
        #if isinstance(other, int) or isinstance(other, float) :
        if isinstance(other, (int, float)):
            x = self.re + other
            y = self.im
            return Complex(x,y)
        elif isinstance(other, complex):
            x = self.re + other.real
            y = self.im + other.imag
            return Complex(x,y)
        elif isinstance(other, Complex):
            x = self.re + other.re
            y = self.im + other.im
            return Complex(x,y)



    def __sub__(self, other):
        '''This function behaves similarly to __add__ function.
        This is subtraction.'''
        #if isinstance(other, int) or isinstance(other, float):
        if isinstance(other, (int, float)):
            x = self.re - other
            y = self.im
            return Complex(x,y)
        elif isinstance(other, complex):
            x = self.re - other.real
            y = self.im - other.imag
            return Complex(x,y)
        elif isinstance(other, Complex):
            x = self.re - other.re
            y = self.im - other.im
            return Complex(x,y)



    def __mul__(self, other):
        '''This function multiplies 2 numbers. If statement to check what type of number
        we want to multiply. Also, 3 possibilities as in the functions above.'''
        #if isinstance(other, int) or isinstance(other, int):
        if isinstance(other, (int, float)):
            x = self.re * other
            y = self.im * other
            return Complex(x,y)
        elif isinstance(other, complex):
            x = (self.re * other.real) + ((self.im * other.imag) * (-1))
            y = (self.re * other.imag) + (self.im * other.real)
            return Complex(x,y)
        elif isinstance(other, Complex):
            x = (self.re * other.re) + ((self.im * other.im) * (-1))
            y = (self.re * other.im) + (self.im * other.re)
            return Complex(x,y)

        #return Complex(x,y)


    def __eq__(self, other):
        '''Checks if 2 numbers are equal'''
        #if isinstance(other, int) or isinstance(other, int):
        if isinstance(other, (int, float)):
            return self.re == other and self.im == 0
        elif isinstance(other, complex):
            return self.re == other.real and self.im == other.imag
        elif isinstance(other, Complex):
            return self.re == other.re and self.im == other.im



    # Assignment 3.4 REVERSED FUNCTIONS FOR __add__, __sub__, __mul__.

    def __radd__(self, other):
        '''Addition is commutative, so we have to allow reversed addition
        f.ex: Complex(5,7) + 3j and 3j + Complex(5,7)'''
        return self + other

    def __rsub__(self, other):
        '''Same idea as in __radd__. This function is called when the first
        arg in __sub__ is not a Complex number'''
        #print("in rsub, self= " + str(self) +  ",  other=" + str(other))
        #z = other.__sub__(self)
        #x = other - self.re
        #y = -self.im
        #return Complex(x,y)
        return (-self) + other
    ''''''
    def __rmul__(self, other):
        return self * other


    # Optional, possibly useful methods

    # Allows you to write `-a`
    def __neg__(self):
        return Complex(-self.re, -self.im)

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        pass
