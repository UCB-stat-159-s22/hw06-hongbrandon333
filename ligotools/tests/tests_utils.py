from ligotools.utils import *
import numpy as np
from ligotools import readligo as rl

strain_H1, time_H1, chan_dict_H1 = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')
strain_L1, time_L1, chan_dict_L1 = rl.loaddata('data/L-L1_LOSC_4_V2-1126259446-32.hdf5', 'L1')

def testwhiten():
    strain_H1_whiten = util.whiten(strain_H1,psd_H1,dt)
    strain_L1_whiten = util.whiten(strain_L1,psd_L1,dt)
    try:
        assert np.isclose(strain_H1_whiten[0], 648.1674991391047)
    except AssertionError as detail:
        print('The whitened H1 strain data is incorrect')
        quit()
    try:
        assert np.isclose(strain_L1_whiten[0], -258.0340503594763)
    except AssertionError as detail:
        print('The whitened L1 strain data is incorrect')
        quit() 



