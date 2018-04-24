class point:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def __repr__(self):
        return "point is %s, %s" % (self.i,self.j)

    def __eq__(self, other):
        if isinstance(other, point):
          return ((self.i == other.i) and (self.j == other.j))
        else:
          return False
    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.__repr__())

def main():
    pt1 = point(1,0)
    pt2 = point(1,0)

    print pt1
    print pt2

    pset = set()
    pset.add(pt1)
    pset.add(pt2)
    print pset

main()
