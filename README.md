# Crystal Plasticity Model for Modeling Deformation Caused By Phase Transformation

## Material Point Integrator

This repository contains a Jupyter Notebook implementation of the crystal plasticity model developed to model deformation caused by phase transformation. The Jupyter Notebook describes a material point integrator which can be plugged into a finite element framework to compute streses at each integration point. The finite element formulation can then be used to solve for the deformation at element level and for the mesh.


### Things to note before using the code:
- Change the transformation deformation gradient ( $\bar{\mathbf{F}}^t$ ) based on the transformation, use the appropriate lattice parameters to compute this.
- update the ```creatSchmid.py``` file with the right slip systems.
- Use the appropriate material properties in the "Material Properties" cell.
- Supply the right hardness rule. A sample file with voce-kocks hardness rule is provided. 

### Acknowledgement

This material is based upon work supported by the National Science Foundation under Grant No. CMMI-1729336.