import numpy as np

def createSchimid(slipSystemType):

    num_slip_sys = 0 
    
    # Parameters for FCC system
    fcc = 0
    # Parameters for hexagonal system
    hex_basal = 0
    hex_prismatic = 0
    hex_pyramidal_1 = 0
    hex_pyramidal_2 = 0
    ac = 1  # a/c ratio
    
    if slipSystemType == "fcc":
        fcc=1
        
    if slipSystemType == "hcp":
        hex_basal = 1
        hex_prismatic = 1
        hex_pyramidal_1 = 1
        hex_pyramidal_2 = 1

    # Define number of slip systems and planes
    if fcc:
        num_slip_sys += 12

    if hex_basal:
            num_slip_sys += 3 

        
    if hex_prismatic:
        num_slip_sys += 3 

    if hex_pyramidal_1:
        num_slip_sys += 6 

    if hex_pyramidal_2:
        num_slip_sys += 6 

    schmid = np.zeros((num_slip_sys, 3, 3))

    cur_sys = 0

    if fcc:
        c1 = 1 / np.sqrt(3.0)
        c2 = 1 / np.sqrt(2.0)
        factor = 1.0 
        schmid[cur_sys+0] = factor*np.outer(c2*np.array([ 1.0,-1.0, 0.0]), c1*np.array([ 1.0, 1.0, 1.0]))  #  { 1  1  1} < 1 -1  0>
        schmid[cur_sys+1] = factor*np.outer(c2*np.array([-1.0, 0.0, 1.0]), c1*np.array([ 1.0, 1.0, 1.0]))  #  { 1  1  1} <-1  0  1>
        schmid[cur_sys+2] = factor*np.outer(c2*np.array([ 0.0, 1.0,-1.0]), c1*np.array([ 1.0, 1.0, 1.0]))  #  { 1  1  1} < 0  1 -1>
        schmid[cur_sys+3] = factor*np.outer(c2*np.array([ 1.0, 0.0, 1.0]), c1*np.array([-1.0, 1.0, 1.0]))  #  {-1  1  1} < 1  0  1>
        schmid[cur_sys+4] = factor*np.outer(c2*np.array([-1.0,-1.0, 0.0]), c1*np.array([-1.0, 1.0, 1.0]))  #  {-1  1  1} <-1 -1  0>
        schmid[cur_sys+5] = factor*np.outer(c2*np.array([ 0.0, 1.0,-1.0]), c1*np.array([-1.0, 1.0, 1.0]))  #  {-1  1  1} < 0  1 -1>
        schmid[cur_sys+6] = factor*np.outer(c2*np.array([-1.0, 0.0, 1.0]), c1*np.array([ 1.0,-1.0, 1.0]))  #  { 1 -1  1} <-1  0  1>
        schmid[cur_sys+7] = factor*np.outer(c2*np.array([ 0.0,-1.0,-1.0]), c1*np.array([ 1.0,-1.0, 1.0]))  #  { 1 -1  1} < 0 -1 -1>
        schmid[cur_sys+8] = factor*np.outer(c2*np.array([ 1.0, 1.0, 0.0]), c1*np.array([ 1.0,-1.0, 1.0]))  #  { 1 -1  1} < 1  1  0>
        schmid[cur_sys+9] = factor*np.outer(c2*np.array([-1.0, 1.0, 0.0]), c1*np.array([-1.0,-1.0, 1.0]))  #  {-1 -1  1} <-1  1  0>
        schmid[cur_sys+10] = factor*np.outer(c2*np.array([ 1.0, 0.0, 1.0]), c1*np.array([-1.0,-1.0, 1.0]))  #  {-1 -1  1} < 1  0  1>
        schmid[cur_sys+11] = factor*np.outer(c2*np.array([ 0.0,-1.0,-1.0]), c1*np.array([-1.0,-1.0, 1.0]))  #  {-1 -1  1} < 0 -1 -1>        
        cur_sys += 12

    if hex_basal:
        c1 = 1.0 
        c2 = 1.0 
        factor = 1.0 
        sqrt3over2 = np.sqrt(3)/2 
        schmid[cur_sys+0] = factor*np.outer(c2*np.array([ 0.5,-sqrt3over2, 0.0]), c1*np.array([ 0.0, 0.0, 1.0]))   # { 0 0 1} < 1/2 -sqrt(3)/2 0>
        schmid[cur_sys+1] = factor*np.outer(c2*np.array([ 1.0, 0.0, 0.0]), c1*np.array([ 0.0, 0.0, 1.0])) # { 0 0 1} < 1 0 0>
        schmid[cur_sys + 2] = factor * np.outer(c2 * np.array([0.5, sqrt3over2, 0.0]), c1 * np.array([0.0, 0.0, 1.0]))  # { 0 0 1} < 1/2  sqrt(3)/2 0>
        cur_sys+=3
        
    if hex_prismatic:
        c1 = 1.0 
        c2 = 1.0 
        factor = 1.0 
        schmid[cur_sys+0] = factor*np.outer(c2*np.array([ 1.0, 0.0, 0.0]), c1*np.array([ 0.0, -1.0, 0.0]))       # { 0 -1 0} < 1 0 0>
        schmid[cur_sys+1] = factor*np.outer(c2*np.array([ 0.5, sqrt3over2, 0.0]), c1*np.array([ sqrt3over2, -0.5, 0.0]))  # { sqrt(3)/2 -1/2 0} <  1/2 sqrt(3)/2 0>
        schmid[cur_sys+2] = factor * np.outer(c2 * np.array([-0.5, sqrt3over2, 0.0]), c1 * np.array([sqrt3over2, 0.5, 0.0]))  # { sqrt(3)/2  1/2 0} <  1/2 sqrt(3)/2 0>
        cur_sys +=3

    if hex_pyramidal_1:
        c1 = 1.0/np.sqrt(1.0+0.75*ac*ac) 
        c2 = 1.0 
        factor = 1.0 
        schmid[cur_sys+0] = factor*np.outer(c2*np.array([ 1.0,0.0, 0.0]), c1*np.array([ 0.0, -1.0,  ac*sqrt3over2]))  # { 0   -1  sqrt(3)a/2c}b   <   1  0  0>
        schmid[cur_sys+1] = factor*np.outer(c2*np.array([ 1.0,0.0, 0.0]), c1*np.array([ 0.0, -1.0, -ac*sqrt3over2]))  # {0   -1 -sqrt(3)a/2c}b   <   1 0  0>
        schmid[cur_sys+2] = factor*np.outer(c2*np.array([ 0.5, sqrt3over2, 0.0]), c1*np.array([ -sqrt3over2,  0.5,  ac*sqrt3over2]))  # {-sqrt(3)/2  0.5  sqrt(3)a/2c}b   < 0.5  sqrt(3)/2  0>
        schmid[cur_sys+3] = factor*np.outer(c2*np.array([ 0.5, sqrt3over2, 0.0]), c1*np.array([ -sqrt3over2,  0.5, -ac*sqrt3over2]))  # {-sqrt(3)/2  0.5 -sqrt(3)a/2c}b   < 0.5  sqrt(3)/2  0>
        schmid[cur_sys+4] = factor*np.outer(c2*np.array([-0.5, sqrt3over2, 0.0]), c1*np.array([  sqrt3over2,  0.5,  ac*sqrt3over2]))  # { sqrt(3)/2  0.5  sqrt(3)a/2c}b   <-0.5  sqrt(3)/2  0>
        schmid[cur_sys + 5] = factor * np.outer(c2 * np.array([-0.5, sqrt3over2, 0.0]), c1 * np.array([sqrt3over2, 0.5, -ac * sqrt3over2]))  # { sqrt(3)/2  0.5 -sqrt(3)a/2c}b   <-0.5  sqrt(3)/2  0>
        cur_sys +=6

    if hex_pyramidal_2:
        c1 = 1.0/np.sqrt(1.0+ac*ac) 
        c2 = 1.0/np.sqrt(1.0+(1.0/ac)*(1.0/ac)) 
        factor = 1.0 
        schmid[cur_sys+0] = factor*np.outer(c2*np.array([-0.5,  sqrt3over2,  1.0/ac]), c1*np.array([ 0.5, -sqrt3over2,  ac]))  # { 0.5   -sqrt(3)/2    a/c}b   <-0.5   sqrt(3)/2   c/a>d
        schmid[cur_sys+1] = factor*np.outer(c2*np.array([ 0.5, -sqrt3over2,  1.0/ac]), c1*np.array([ 0.5, -sqrt3over2, -ac]))  # { 0.5   -sqrt(3)/2   -a/c}b   < 0.5  -sqrt(3)/2   c/a>d
        schmid[cur_sys+2] = factor*np.outer(c2*np.array([-1.0,0.0,  1.0/ac]), c1*np.array([ 1.0,0.0,  ac]))  # {   1   0    a/c}b   <  -1  0   c/a>d
        schmid[cur_sys+3] = factor*np.outer(c2*np.array([ 1.0,0.0,  1.0/ac]), c1*np.array([ 1.0,0.0, -ac]))  # {   1   0   -a/c}b   <   1  0   c/a>d
        schmid[cur_sys+4] = factor*np.outer(c2*np.array([ 0.5,  sqrt3over2,  1.0/ac]), c1*np.array([ 0.5,  sqrt3over2,  ac]))  # { 0.5    sqrt(3)/2    a/c}b   < 0.5   sqrt(3)/2   c/a>d
        schmid[cur_sys + 5] = factor * np.outer(c2 * np.array([0.5, sqrt3over2, -1.0 / ac]), c1 * np.array([0.5, sqrt3over2, -ac]))  # { 0.5    sqrt(3)/2   -a/c}b   < 0.5   sqrt(3)/2  -c/a>d
        cur_sys += 6

    return (num_slip_sys, schmid)