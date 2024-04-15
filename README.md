
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


## Example Explanation
Sample output from the examples within the ```examples``` folder is held with ```example_plots``` within the main directory.
Each example serves to demonstrate a specific use case of the network simulator, below is a brief outline of each example and the network simulator capability it is demonstrating:

### Example 1
Example 1 is simulating a subsection of the  [Parkinson's Disease Map](https://pdmap.uni.lu/minerva/) from the University of Luxembourg and the Systems Biology Institute, Tokyo.
```example1.py``` demonstrates the ability to fix a specific node within a network to either a given value (as is done for "a_syn_0") or a provided trajectory (as is done for "gba_0").
Additionally, you are able to set initial conditions for the nodes within the network - within this example, we set the starting value of "clearance_0" to 0.

### Example 2
Example 2 is simulating a subsection of the central carbon metabolism within Mycobacterium Tuberculosis. The network information is taken from [KEGG](https://www.genome.jp/kegg/).
Within this example, we show that:
1. The starting masses of the nodes can be set (bulk setting of initial conditions)
2. The value of the fluxes between the edges can be set

### Example 3
Example 3 provides a simulation of a basic network with 3 nodes. Example 3 demonstrates that the dynamics assigned to edges within the network can be non-trivially assigned.
A ```min_min``` function is defined, and used for hyperedges within the network, by being passed to the ```min_func``` arg in the network object call.


### Example 4
Example 4 demonstrates the ability of the simulator to "complete" networks which do not have an equilibria due to network topology.
A .csv file containing edges for a network without an equilibria can be "completed" to include "virtual nodes" which facilitate the existence of an equilbria.
Within this example, we are simulating the subsection of the [Parkinson's Disease Map](https://pdmap.uni.lu/minerva/); however, we show that you can make multiple calls to the ```basic_plot``` function of a network object after you can run a single simulation.


### Example 5
Example 5 provides an example of dynamically fetching a network from the [KEGG Database](https://www.genome.jp/kegg/) using a wrapper of their API.
This network is then simulated.

### KEGG Notes
- [KGML Docs](https://www.kegg.jp/kegg/xml/docs/)
- [Pathway with gene information](https://www.genome.jp/kegg-bin/show_pathway?mtu01200))
- [Pathway without gene info](https://www.genome.jp/kegg-bin/show_pathway?rn01200))
