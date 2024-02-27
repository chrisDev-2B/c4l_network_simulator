
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
├───docs
│   ├───build
│   │   ├───coverage
│   │   ├───doctrees
│   │   └───html
│   │       ├───_sources
│   │       └───_static
│   │           ├───css
│   │           │   └───fonts
│   │           └───js
│   └───source
├───metabolicpd
│   ├───examples
│   ├───io
│   ├───life
└───tests
```

### examples

The ```examples``` folder holds python script files that demonstrate various use cases of the code base.

### io

The ```io``` folder contains helper functions for reading in KEGG data files from ```data > kegg```.

### life

The ```life``` folder contains the main object, ```network``` which is responsible for processing the data files and creating simulations.


## Running the Examples

In order to run the examples, open an ```example#.py``` file in an IDE such as Pycharm, Spyder, VSCode, etc. 
Next, just run the example file.

The script file should be structured in a way that automatically grabs the path to the ```data``` folder and then creates a ```network``` object and displays the results of the simulation.

## Profiling Code
To profile the code, i.e. to find how long each part of the code takes to run so as to optimize runtime, you can run 
```
poetry run python -m cProfile metabolicpd/simulation.py
```
to print the data to stdout. In order to print this information to a file (which is usually the best idea), use this
```
poetry run python -m cProfile -o simulation_stats metabolicpd/simulation.py
```
With a profile file, we can use the pstats module, e.g. using the repl, to analyse the data.
See [this](https://docs.python.org/3/library/profile.html) link for documentation and examples

# KEGG Notes
- [KGML Docs](https://www.kegg.jp/kegg/xml/docs/)
- [Pathway with gene information](https://www.genome.jp/kegg-bin/show_pathway?mtu01200))
- [Pathway without gene info](https://www.genome.jp/kegg-bin/show_pathway?rn01200))
