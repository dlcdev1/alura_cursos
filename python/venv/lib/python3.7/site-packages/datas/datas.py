class point(tuple):

    def __new__(cls, x, y):
        return super(point, cls).__new__(cls, (x, y))

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __str__(self):
        return '({}, {})'.format(*self)


class attrdict(dict):

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        self.__dict__.pop(key)

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __unicode__(self):
        return unicode(repr(self.__dict__))


class trydict(dict):

    def __getitem__(self, k):
        try:
            return dict.__getitem__(self, k)
        except KeyError:
            v = self[k] = type(self)()
            return v


class nesteddict(dict):

    def __missing__(self, k):
        v = self[k] = type(self)()
        return v


class autodict(nesteddict):

    def __init__(self, prev=None, root=None, **kwargs):
        self.prev = prev
        self.root = root
        self.__super = super(autodict, self)
        self.__super.__init__(**kwargs)

    def __setitem__(self, k, v):
        if v is None:
            self.prev[self.root] = [k]
        else:
            self.__super.__setitem__(k, v)

    def __missing__(self, k):
        v = self[k] = type(self)(self, k)
        return v


if __name__ == '__main__':

    print('TRYDICT ###################')
    td = trydict()
    td[0][1][2][3][4] = None
    td[0][1][2][3][10] = float('inf')
    print(td)

    print('AUTODICT ###################')
    ad = autodict()
    ad['a']['b']['c']['d'] = None
    ad['a'][1][2] = 3
    print(ad)

    print('ATTRDICT ###################')
    at = attrdict()
    at.halo = 'aloha'
    at.aloha = 'halo'
    print(at)

    print('NESTEDDICT ###################')
    ad = nesteddict()
    ad['a']['b']['c']['d'] = None
    ad['a'][1][2] = 3
    print(ad)
