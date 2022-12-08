# Crystal Plasticity Model for Modeling Deformation Caused By Phase Transformation

## Material Point Integrator

This repository contains a Jupyter Notebook implementation of the crystal plasticity model developed to model deformation caused by phase transformation. The Jupyter Notebook describes a material point integrator which can be plugged into a finite element framework to compute stresses at an integration point. The finite element framework can then be used to solve for the deformation at element level and for the mesh.


### Things to note before using the code:
- Change the transformation deformation gradient ( $\bar{\mathbf{F}}^t$ ) based on the transformation, use the appropriate lattice parameters to compute this.
- update the ```creatSchmid.py``` file with the right slip systems.
- Use the appropriate material properties in the "Material Properties" cell.
- Supply the right hardness rule. A sample file with voce-kocks hardness rule is provided. 

Please address any questions/commments to sagar.bhatt0904@gmail.com

### Acknowledgement

This material is based upon work supported by the National Science Foundation under Grant No. CMMI-1729336.

### Citing
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7412821.svg)](https://doi.org/10.5281/zenodo.7412821)

Sagar Bhatt and Antoinette Maniatty, “Crystal Plasticity Model for Modeling Deformation Caused by Phase Transformation”. Zenodo, Dec. 08, 2022. doi: 10.5281/zenodo.7412821.
