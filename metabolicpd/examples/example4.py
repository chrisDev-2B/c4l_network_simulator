# -*- coding: utf-8 -*-

import numpy as np
from os.path import dirname, abspath, join
from os import getcwd
import sys
sys.path.append(getcwd())
from metabolicpd.life import network

if __name__ == "__main__":

    file_path = abspath(__file__)
    data_directory = join(dirname(dirname(dirname(file_path))), 'data')
    network_name = 'simple_pd_network_no_virtual_virtual.csv'

    s = network.Metabolic_Graph(
        file=join(data_directory, network_name),
        mass=None,  # Makes the masses random via constructor
        flux=None,
        source_weights=None,
        t_0=0,
        t=500,
        num_samples=1000,
    )

    # The three ways of directly controlling metabolites
    # 1. fix trajectory using pos or derivative
    # 2. fix initial value and force it to be constant
    # 3. set initial value (can also be done in Metabolic_Graph.mass)
    #    doesn't control trajectory
    s.fixMetabolite("gba_0", 2.5, -np.sin(s.t_eval), isDerivative=True)
    s.fixMetabolite("a_syn_0", 1.5)
    s.setInitialValue("clearance_0", 0.0)
    print(s.mtb)

    result = s.simulate()
    # NOTE: it looks like mis_a_syn_0 diverges but it actually converges to ~8
    network.basic_plot(result, s, [0, 1, 3, 6, 19, 24, 25, 27], ylim=[0, 10])
    network.basic_plot(
        result,
        s,
        [0, 1, 2, 3, 4, 5, 6, 7, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 37, 38],
        ylim=[0, 3],
    )
