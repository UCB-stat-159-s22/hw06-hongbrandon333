from ligotools import readligo as rl
import numpy as np


strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1')
strain_L1, time_L1, chan_dict_L1 = rl.loaddata('data/L-L1_LOSC_4_V2-1126259446-32.hdf5', 'L1')
    
        
def test_loadH1_strain_data():
    try:
        assert np.isclose(strain_H1[0], 2.177040281449375e-19)
        assert strain_H1.shape == (131072, )
    except AssertionError as detail:
        print('The strain data loaded from the H1 dataset is incorrect')
        quit()
        
def test_loadH1_time_data():
    try:
        assert np.isclose(time_H1[0], 1126259446.0)
        assert time_H1.shape == (131072, )
    except AssertionError as detail:
        print('The time data loaded from the H1 dataset is incorrect')
        quit()

def test_loadL1_strain_data():
    try:
        assert np.isclose(strain_L1[0], -1.0428999418774637e-18)
        assert strain_L1.shape == (131072, )
    except:
        print('The strain data loaded from the L1 data is incorrect')
        quit()

def test_loadL1_time_data():
    try:
        assert np.isclose(time_L1[0], 1126259446.0)
        assert time_L1.shape == (131072, )
    except AssertionError as detail:
        print('The time data loaded from the L1 data is incorrect')
        quit()

    