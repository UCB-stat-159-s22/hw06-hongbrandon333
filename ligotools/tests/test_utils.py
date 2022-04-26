import ligotools as ligo
from ligotools import readligo as rl
from ligotools import utils as utils 
import numpy as np
import matplotlib.mlab as mlab
from ligotools import readligo as rl
from scipy.interpolate import interp1d
from os.path import exists
from os import remove

strain_H1, time_H1, chan_dict_H1 = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')
strain_L1, time_L1, chan_dict_L1 = rl.loaddata('data/L-L1_LOSC_4_V2-1126259446-32.hdf5', 'L1')
fs = 4096
NFFT = 4*fs

def test_whiten():
    dt = time_H1[1] - time_H1[0]
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
    psd_H1 = interp1d(freqs, Pxx_H1)
    strain_H1_whiten = utils.whiten(strain_H1,psd_H1,dt)
    assert strain_H1_whiten.shape == (131072, )
        
def test_writewavefile(): 
    data = np.linspace(0,10,16000)
    utils.write_wavfile("audio/temp.wav", fs, data)
    assert exists("audio/temp.wav")
    remove("audio/temp.wav")
    
def test_reqshift():
    fshift = 400.
    speedup = 1.
    dt = time_L1[1] - time_L1[0]
    fss = int(float(fs)*float(speedup))
    Pxx_L1, freqs = mlab.psd(strain_L1, Fs = fs, NFFT = NFFT)
    psd_L1 = interp1d(freqs, Pxx_L1)
    strain_L1_whiten = utils.whiten(strain_L1,psd_L1,dt)
    strain_L1_shifted = utils.reqshift(strain_L1_whiten,fshift=fshift,sample_rate=fs)
    assert strain_L1_shifted.shape == (131072,)

def test_plot_functions():
    pass
    
    



