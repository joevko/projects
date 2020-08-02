from complex import Complex

def test_add_two_complex():
    x = Complex(1, 1)
    y = Complex(4, 9)
    z = x + y
    assert z == Complex(5, 10)
    #z.re == 5 and z.im == 9


def test_sub_two_complex():
    x = Complex(1, 1)
    y = Complex(2, 4)
    z = x - y
    assert z == Complex(-1, -3)
     #z.re == -6 and z.im == 4

def test_mul_two_complex():
    x = Complex(2,3)
    y = Complex(4,2)
    z = x * y
    assert z == Complex(2, 16)
    #z.re == 2 and z.im == 16

def test_conj_complex():
    c = Complex(1,3).conjugate()
    print("test ", c.re, " ", c.im)
    assert c == Complex(1, -3)
    #c.re == 1 and c.im == -3

def test_mod_complex():
    m = Complex(6,-8).modulus()
    assert m == 10


def test_eq_two_complex():
    x = Complex(2,3)
    y = Complex(2,3)
    assert x == y

def test_radd():
    x = 1
    y = Complex(3, 5)
    z = x + y
    assert z == Complex(4, 5)

def test_rmul():
    x = 2
    y = Complex(4, 6)
    z = x * y
    assert z == Complex(8, 12)

def test_rsub():
    x = 1
    y = Complex(2, 3)
    z = x - y
    assert z == Complex(-1, -3)


'''Unlock the test functions below to test the complex.py program.'''

#test_add_two_complex()
#test_sub_two_complex()
#test_mul_two_complex()
#test_conj_complex()
#test_mod_complex()
#test_eq_two_complex()
#test_radd()
#test_rmul()
#test_rsub()
