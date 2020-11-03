from polygon_class import Polygon
from functools import lru_cache

class Polygon_seq:
  def __init__(self, e, r):
    self.radius = r;
    self.edges = e;
  
  def __len__(self):
    return self.edges

  def __getitem__(self, index):
    if isinstance(index, int):
      if (index <0 or index >= self.edges):
        raise IndexError
      elif (index <3):
        return 
      else:
        return Polygon_seq._poly(index, self.radius)
  
  @staticmethod
  @lru_cache(2*10)
  def _poly(edges, radius):
    return Polygon(edges, radius)

  def __repr__(self):
    return f"Polygon sequence with {self.edges} polygons with a circumradius of {self.radius}"

  @property
  def max_efficiency(self):
    return Polygon(self.edges, self.radius)
