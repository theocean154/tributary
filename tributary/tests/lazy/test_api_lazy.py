import tributary.lazy as tl

class TestAPI:
    def test_api(self):
        assert hasattr(tl.LazyNode, '__add__')
        assert hasattr(tl.LazyNode, '__add__')
        assert hasattr(tl.LazyNode, '__radd__')
        assert hasattr(tl.LazyNode, '__sub__')
        assert hasattr(tl.LazyNode, '__rsub__')
        assert hasattr(tl.LazyNode, '__mul__')
        assert hasattr(tl.LazyNode, '__rmul__')
        assert hasattr(tl.LazyNode, '__div__')
        assert hasattr(tl.LazyNode, '__rdiv__')
        assert hasattr(tl.LazyNode, '__truediv__')
        assert hasattr(tl.LazyNode, '__rtruediv__')
        assert hasattr(tl.LazyNode, '__pow__')
        assert hasattr(tl.LazyNode, '__rpow__')
        assert hasattr(tl.LazyNode, '__mod__')
        assert hasattr(tl.LazyNode, '__rmod__')
        assert hasattr(tl.LazyNode, '__and__')
        assert hasattr(tl.LazyNode, '__or__')
        assert hasattr(tl.LazyNode, '__invert__')
        assert hasattr(tl.LazyNode, '__bool__')
        assert hasattr(tl.LazyNode, 'int')
        assert hasattr(tl.LazyNode, 'float')
        assert hasattr(tl.LazyNode, '__str__')
        assert hasattr(tl.LazyNode, '__lt__')
        assert hasattr(tl.LazyNode, '__le__')
        assert hasattr(tl.LazyNode, '__gt__')
        assert hasattr(tl.LazyNode, '__ge__')
        assert hasattr(tl.LazyNode, '__eq__')
        assert hasattr(tl.LazyNode, '__ne__')
        assert hasattr(tl.LazyNode, '__neg__')
        assert hasattr(tl.LazyNode, '__len__')
        assert hasattr(tl.LazyNode, 'log')
        assert hasattr(tl.LazyNode, 'sin')
        assert hasattr(tl.LazyNode, 'cos')
        assert hasattr(tl.LazyNode, 'tan')
        assert hasattr(tl.LazyNode, 'asin')
        assert hasattr(tl.LazyNode, 'acos')
        assert hasattr(tl.LazyNode, 'atan')
        assert hasattr(tl.LazyNode, 'abs')
        assert hasattr(tl.LazyNode, 'sqrt')
        assert hasattr(tl.LazyNode, 'exp')
        assert hasattr(tl.LazyNode, 'erf')

