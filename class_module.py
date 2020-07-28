# This file contains all of the classes for the project

# concentrated loads
class ConcentratedLoad:
  def __init__(self, mag, x):
    self.pos = x
    self.magnitude = mag
  
  def get_pos(self):
    return self.pos
  
  def get_magnitude(self):
    return self.magnitude
  
# concentrated moments
class ConcentratedMoment:
  def __init__(self, x, mag):
    self.pos = x
    self.magnitude = mag
  
  def get_pos(self):
    return self.pos
  
  def get_magnitude(self):
    return self.magnitude
  
# distributed loads
class DistributedLoad:
  def __init__(self, mag, s, e):
    self.start = s
    self.end = e
    self.magnitude = mag
  
  def get_start(self):
    return self.start
  
  def get_end(self):
    return self.end
  
  def get_magnitude(self):
    return self.magnitude
  
  def get_centroid_load(self):
    self.centroid_load = []
    self.centroid_load.append( ( self.start + self.end ) / 2 )
    self.centroid_load.append( self.magnitude * ( self.end - self.start ) )
    return self.centroid_load
  
  def get_dw(self):
    return self.magnitude / ( ( self.end - self.start) * 1000 )
  
# support
class Support:
  def __init__(self, t, x):
    self.type = t
    self.pos = x
    self.reaction = None
  
  def get_pos(self):
    return self.pos
  
  def get_reaction(self):
    return self.reaction
  
  def set_reaction(self, r):
    self.reaction = r
   
  