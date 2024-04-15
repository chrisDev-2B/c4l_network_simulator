# -*- coding: utf-8 -*-

import numpy as np
from os.path import dirname, abspath, join
from os import getcwd
import sys


from metabolicpd.life import network

if __name__ == "__main__":

    file_path = abspath(__file__)
    data_directory = join(dirname(dirname(dirname(file_path))), 'data')
    network_name = 'simple_pd_network.csv'

    s = network.Metabolic_Graph(
        file=join(data_directory, network_name),
        mass=None,  # Makes the masses random via constructor
        flux=None,
        source_weights=None,
        t_0=0,
        t=15,
        num_samples=100,
    )

    # The three ways of directly controlling metabolites
    # 1. fix trajectory using pos or derivative
    # 2. fix initial value and force it to be constant
    # 3. set initial value (can also be done in Metabolic_Graph.mass)
    #    doesn't control trajectory
    s.fixMetabolite("gba_0", 2.5, -np.sin(s.t_eval), isDerivative=True)
    s.fixMetabolite("a_syn_0", 1.5)
    s.setInitialValue("clearance_0", 0.0)

    result = s.simulate()
    network.basic_plot(result, s, [0, 1, 3, 6, 17, 22, 23, 25])
