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
    NFFT = 4*fs
    psd_window = np.blackman(NFFT)
    NOVL = NFFT/2
    template = (template_p + template_c*1.j) 
    etime = time+template_offset
    datafreq = np.fft.fftfreq(template.size)*fs
    df = np.abs(datafreq[1] - datafreq[0])
    try:   
        dwindow = signal.tukey(template.size, alpha=1./8)  # Tukey window preferred, but requires recent scipy 
    except:
        dwindow = signal.blackman(template.size)          # Blackman window OK if Tukey is not available
    template_fft = np.fft.fft(template*dwindow) / fs
    data = strain_L1.copy()
    data_psd, freqs = mlab.psd(data, Fs = fs, NFFT = NFFT, window=psd_window, noverlap=NOVL)
    data_fft = np.fft.fft(data*dwindow) / fs
    power_vec = np.interp(np.abs(datafreq), freqs, data_psd)
    optimal = data_fft * template_fft.conjugate() / power_vec
    optimal_time = 2*np.fft.ifft(optimal)*fs
    sigmasq = 1*(template_fft * template_fft.conjugate() / power_vec).sum() * df
    sigma = np.sqrt(np.abs(sigmasq))
    SNR_complex = optimal_time/sigma
    peaksample = int(data.size / 2)  # location of peak in the template
    SNR_complex = np.roll(SNR_complex,peaksample)
    SNR = abs(SNR_complex)
    indmax = np.argmax(SNR)
    timemax = time[indmax]
    SNRmax = SNR[indmax]
    d_eff = sigma / SNRmax
    phase = np.angle(SNR_complex[indmax])
    offset = (indmax-peaksample)
    template_phaseshifted = np.real(template*np.exp(1j*phase))    
    template_rolled = np.roll(template_phaseshifted,offset) / d_eff  
    template_whitened = util.whiten(template_rolled,interp1d(freqs, data_psd),dt)  
    template_match = filtfilt(bb, ab, template_whitened) / normalization 
    pcolor='g'
    strain_whitenbp = strain_L1_whitenbp
    template_L1 = template_match.copy()
    assert exists('figures/'+'GW150914'+"_"+"H1"+"_matchtime."+"png")
    remove('figures/'+'GW150914'+"_"+"H1"+"_matchtime."+"png")
            
    
    



