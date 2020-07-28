# Import all libraries and clases
from class_module import ConcentratedLoad
from class_module import ConcentratedMoment
from class_module import DistributedLoad
from class_module import Support
import matplotlib.pyplot as plt
import csv

# Methods
def parse_data():
  # parses data from setup.dat and returns a 2D list containing parsed data
  temp_cls, temp_cms, temp_dls, temp_spt = [], [], [], [] # temporary lists to hold parsed data
  
  with open( 'setup.csv' ) as data:
    reader = csv.reader( data, delimiter = ',' )
    line_count = 0
    len = None
    for row in reader:
      if row[1] == 'DL': # catches distributed load data and throws into temporary list
        temp_dls.append( DistributedLoad( float( row[2] ), float( row[3] ), float( row[4] ) ) ) 
      
      if row[1] == 'CL': # catches concentrated load data and throws into temporary list
        temp_cls.append( ConcentratedLoad( float( row[2] ), float( row[3] ) ) )
      
      if row[1] == 'CM': # catches concentrated moment data and throws into temporary list
        temp_cms.append( ConcentratedMoment( float( row[2] ), float( row[3] ) ) )
      
      if row[1] == 'Pinned' or row[1] == 'Roller' or row[1] == 'Fixed' or row[1] == 'Free': # catches support data and throws into temporary list
        temp_spt.append( Support( row[1] , float( row[2] ) ) )
      
      if 'Length' in row[0]:
        len = float( row[1] )
  return [temp_cls, temp_cms, temp_dls, temp_spt, len]            

def calc_rxn( temp_cls, temp_cms, temp_dls, temp_spt ):
  # calculates reactions and returns list of reactions
  rhs = 0
  sum_vert = 0
  
  for item in temp_cls: # sums moments about left support due to concentrated loads
    rhs += ( item.get_pos() - temp_spt[0].get_pos() ) * item.get_magnitude()
    sum_vert += item.get_magnitude()
  for item in temp_cms: # sums concentrated moments
    rhs -= item.get_magnitude()
  for item in temp_dls: # sums moments about left support due to distributed loads
    centroid_load = item.get_centroid_load()
    rhs += ( centroid_load[0] - temp_spt[0].get_pos() ) * centroid_load[1]
    sum_vert += centroid_load[1]
  
  right_rxn = rhs / ( temp_spt[1].get_pos()  - temp_spt[0].get_pos() ) # computes right reaction based on sum of moments
  left_rxn = sum_vert - right_rxn # computes left reaction based on sum of vertical forces
  
  return [left_rxn, right_rxn]

def is_between(spot, r1, r2):
  if spot < r2 and spot >= r1:
    return True
  return False
  

def calc_shear( temp_cls, temp_cms, temp_dls, temp_spt, len ):
  inc = len / 1000
  shear_value = 0
  plot_vals = []
  i = 0
  while i < len - inc:
    for item in temp_cls:
      if is_between( item.get_pos(), i - ( inc / 2 ), i + ( inc / 2 ) ):
        shear_value -= item.get_magnitude()
    
    for item in temp_spt:
      if is_between( item.get_pos(), i - ( inc / 2 ), i + ( inc / 2 ) ):
        shear_value += item.get_reaction()
    
    for item in temp_dls:
      if is_between( i, item.get_start(), item.get_end() ):
        shear_value -= item.get_magnitude() * (item.get_end() - item.get_start()) / ( (item.get_end() - item.get_start() ) * 100)
        #shear_value -= item.get_dw(len)
        
    plot_vals.append(shear_value)
    i += inc
  return plot_vals
# Main

# assigns parsed data into global variables
parsed_data = parse_data()
beam_length = parsed_data[4]
cls, cms, dls, spt = parsed_data[0], parsed_data[1], parsed_data[2], parsed_data[3] # puts parsed data into respective global lists
reaction_data = calc_rxn(cls, cms, dls, spt)
x_values = []
i = 0
while i < beam_length - beam_length / 1000:
  x_values.append(i)
  i += beam_length / 1000

 # sets reactions from reaction data
i = 0
for support in spt:
  if not support.get_pos() == len:
    support.set_reaction( reaction_data[i] )
    i += 1
  
# gets plotable shear data
shear = calc_shear( cls, cms, dls, spt, beam_length )
plt.plot( x_values, shear )
plt.savefig( 'test.png' )