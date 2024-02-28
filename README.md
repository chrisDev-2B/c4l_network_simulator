
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

Running the examples has been tested on both [VS Code](https://code.visualstudio.com/) and [PyCharm](https://www.jetbrains.com/pycharm/). The code will be easier to run if you are able to open entire folders within the application. 

The example script file should grab the path to the ```data``` folder, then create a ```network``` object and display the result of the simulation.

To run the examples:
1. Clone the repo to your local machine.
2. From VS Code or your IDE, open the repo as a project/folder.
3. From the navigation pane (typically on the left-hand-side of the application), open ```example#.py``` (found in ```metabolicpd > examples```)
4. Run the ```example#.py``` file.
5. If the example runs successfully, a plot of the node trajectories will display along with some text outputted in the console.


### KEGG Notes
- [KGML Docs](https://www.kegg.jp/kegg/xml/docs/)
- [Pathway with gene information](https://www.genome.jp/kegg-bin/show_pathway?mtu01200))
- [Pathway without gene info](https://www.genome.jp/kegg-bin/show_pathway?rn01200))
