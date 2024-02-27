
## Package Dependencies and Python Version
This project has been run with Python 3.11; however, earlier versions may work - up to Python 3.5 which is required for the typing library.

A list of the required packages for the project with versions that are known to work is provided.
- biopython 1.8.3
- matplotlib 3.8.3
- numpy 1.26.4
- scipy 1.12.0
- seaborn 0.13.2
- pandas 2.2.1

As noted, earlier version of Python and the packages may work; however, the most recent version of this repo is known to work with the above versions.

## Installing the Dependencies

Python can be installed from [python.org](https://www.python.org/).
The packages can be installed using a package manager such as [**pip**](https://pypi.org/project/pip/) or [**conda**](https://conda.io/projects/conda/en/latest/index.html).

## Project Layout

The main code for this project is contained within the ```metabolicpd``` folder.
Within the ```metabolicpd``` folder, you will find three additional folders: ```examples```, ```io```, and ```life```.
```
├───data
│   └───kegg
├───metabolicpd
│   ├───examples
│   ├───io
│   ├───life
```

### examples Folder

The ```examples``` folder holds python script files that demonstrate various use cases of the code base.

### io Folder

The ```io``` folder contains helper functions for reading in KEGG data files from ```data > kegg```.

### life Folder

The ```life``` folder contains the main object, ```network```, which is responsible for processing the data files, creating simulations, and plotting results.


## Running the Examples

In order to run the examples, open an ```example#.py```  file (found in ```metabolicpd > examples```) in an IDE such as Pycharm, Spyder, VSCode, etc. 
Next, just run the example file.

The script file should grab the path to the ```data``` folder, then create a ```network``` object and display the result of the simulation.

# KEGG Notes
- [KGML Docs](https://www.kegg.jp/kegg/xml/docs/)
- [Pathway with gene information](https://www.genome.jp/kegg-bin/show_pathway?mtu01200))
- [Pathway without gene info](https://www.genome.jp/kegg-bin/show_pathway?rn01200))
