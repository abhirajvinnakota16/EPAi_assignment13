import math

class Polygon:
    def __init__(self, e, r):
        self.edges = e
        self.radius = r
        
    @property
    def edges(self):
      return self._edges
      
    @edges.setter
    def edges(self, value):
      if (value <= 2):
        raise ValueError("Minimum edges need to be 3")
      self._edges = value

    @property
    def radius(self):
      return self._radius

    @radius.setter
    def radius(self, value):
      if (value <= 0):
        raise ValueError("Minimum radius is greater than zero")
      self._radius = value

    @property
    def internal_angle(self):
      return (self.edges-2)*180/self.edges

    @property
    def edge_length(self):
      return 2 * self.radius * math.sin(math.pi/self.edges)

    @property
    def apothem(self):
      return self.radius * math.cos(math.pi/self.edges)

    @property
    def area(self):
      return self.edges * self.edge_length * self.apothem / 2

    @property
    def perimeter(self):
      return self.edges * self.edge_length

    def __repr__(self):
      return f"Polygon with {self.edges} vertices and a circumradius of {self.radius}"

    def __eq__(self, obj):
      if (self.radius == obj.radius and self.edges == obj.edges):
        return True
      else:
        return False

    def __gt__(self, obj):
      if (self.edges > obj.edges):
        return True
      else :
        return False 