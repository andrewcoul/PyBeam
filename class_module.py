# This file contains all of the classes for the project

# Concentrated loads
class ConcentratedLoad:
  def __init__(self, mag, x):
    self.position = x
    self.magnitude = mag
  
  def get_position(self):
    return self.position
  
  def get_magnitude(self):
    return self.magnitude
  
# Concentrated moments
class ConcentratedMoment:
  def __init__(self, x, mag):
    self.position = x
    self.magnitude = mag
  
  def get_position(self):
    return self.position
  
  def get_magnitude(self):
    return self.magnitude
  
# Distributed loads
class DistributedLoad:
  def __init__(self, s, e, smag, emag):
    self.start = s
    self.end = e
    self.start_magnitude = smag
    self.end_magnitude = emag
  
  def get_start(self):
    return self.start
  
  def get_end(self):
    return self.end
  
  def get_start_magnitude(self):
    return self.start_magnitude
    
  def get_end_magnitude(self):
    return self.end_magnitude
  
# Pinned support
class Pinned:
  def __init__(self, x):
    self.position = x
    self.x_reaction = None
    self.y_reaction = None
   
  def set_x_reaction(self, r):
    self.x_reaction = r
  
  def set_y_reaction(self, r):
    self.y_reaction = r
    
  def get_position(self):
    return self.position
  
  def get_x_reaction(self):
    return self.x_reaction
  
  def get_y_reaction(self):
    return self.y_reaction
  
  def get_type(self):
    return 'Pinned'

# Roller support  
class Roller:
  def __init__(self, x):
    self.position = x
    self.y_reaction = None
  
  def set_y_reaction(self, r):
    self.y_reaction = r
  
  def get_position(self):
    return self.position
  
  def get_y_reaction(self):
    return self.y_reaction
    
  def get_type(self):
    return 'Roller'

# Fixed support    
class Fixed:
  def __init__(self, x):
    self.position = x
    self.x_reaction = None
    self.y_reaction = None
    self.internal_moment = None
    
  def set_x_reaction(self, r):
    self.x_reaction = r
    
  def set_y_reaction(self, r):
    self.y_reaction = r
    
  def set_internal_moment(self, m):
    self.internal_moment = m
    
  def get_position(self):
    return self.position
  
  def get_x_reaction(self):
    return self.x_reaction
  
  def get_y_reaction(self):
    return self.y_reaction
  
  def get_internal_moment(self):
    return self.internal_moment
    
  def get_type(self):
    return 'Fixed'