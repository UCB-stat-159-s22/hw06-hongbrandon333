import ligotools as ligo
from ligotools import readligo as rl
from ligotools import utils as utils 
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.mlab as mlab
from ligotools import readligo as rl
from scipy.interpolate import interp1d
from os.path import exists
from os import remove
from scipy.signal import butter, filtfilt

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
    fband = [43.0, 300.0]
    time = time_H1
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
    psd_H1 = interp1d(freqs, Pxx_H1)
    dt = time[1] - time[0]
    strain_H1_whiten = u.whiten(strain_H1,psd_H1,dt)
    bb, ab = butter(4, [fband[0]*2./fs, fband[1]*2./fs], btype='band')
    normalization = np.sqrt((fband[s1]-fband[0])/(fs/2))
    strain_H1_whitenbp = filtfilt(bb, ab, strain_H1_whiten) / normalization
    timemax = 1126259462.432373
    utils.plot_functions(time, timemax, 0, 'g','GW150914', 'H1', 'png',1126259462.44, strain_whitenbp,  0, 0, 0 , 999.743130306333, 0, psd_H1, fs)
    assert exists('figures/'+'GW150914'+"_"+"H1"+"_matchtime."+"png")
    remove('figures/'+'GW150914'+"_"+"H1"+"_matchtime."+"png")
            
    
    



