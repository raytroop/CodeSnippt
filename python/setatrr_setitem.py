# caffe/net_spec.py
from collections import OrderedDict


class NetSpec(object):
    """A NetSpec contains a set of Tops (assigned directly as attributes).
    Calling NetSpec.to_proto generates a NetParameter containing all of the
    layers needed to produce all of the assigned Tops, using the assigned
    names."""

    def __init__(self):
        super(NetSpec, self).__setattr__('tops', OrderedDict())
        # object.__setattr__(self, 'tops', OrderedDict())       # OK, dont forget `self`
        # self.tops = OrderedDict()      # Error 
          # Traceback (most recent call last):
          # File "setatrr_setitem.py", line 28, in <module>
          #   obj = NetSpec()     # __init__  --> super(NetSpec, self).__setattr__
          # File "setatrr_setitem.py", line 14, in __init__
          #   self.tops = OrderedDict()       # RuntimeError: maximum recursion depth exceeded
          # File "setatrr_setitem.py", line 16, in __setattr__
          #   self.tops[name] = value
          # File "setatrr_setitem.py", line 19, in __getattr__
          # ...
    def __setattr__(self, name, value):
        self.tops[name] = value

    def __getattr__(self, name):
        return self.tops[name]

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __getitem__(self, item):
        return self.__getattr__(item)

if __name__ == '__main__':
    obj = NetSpec()     # __init__  --> super(NetSpec, self).__setattr__
    print(obj.tops)     # class member
    obj['a'] = 1        # __setitem__
    obj.b = 2           # __setattr__
    print(obj.tops)     # class memer
    print(obj['a'])     # __getitem__
    print(obj.b)        # __getattr__
    print(obj.__dict__)
    print(vars(obj))

