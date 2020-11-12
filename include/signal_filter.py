from scipy.signal import iirdesign
from scipy.signal import freqz
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scipy.signal import freqs
from scipy.signal import fir_filter_design


class iirFilter:

    def __init__(self, sampling_freq, low_freq, high_freq, attenuation_pass, attenuation_stop, typ='butter'):
        self._freq = sampling_freq
        self._low = low_freq
        self._high = high_freq
        self._g_pass = attenuation_pass
        self._g_stop = attenuation_stop
        self.typ = typ

        self.b_coeff = 0
        self.a_coeff = 0

        self.frequencies = 0
        self.ampl = 0

        self._design_filter()

    def _design_filter(self):
        filter_coeff = iirdesign(wp=2 * self._low / self._freq,
                                 ws=2 * self._high / self._freq,
                                 gpass=self._g_pass,
                                 gstop=self._g_stop,
                                 ftype=self.typ)

        self.b_coeff, self.a_coeff = filter_coeff
        return self.b_coeff, self.a_coeff

    def compute_frequency_response(self, sampling_res=1, display=False):

        nb_sampling = self._freq / (2 * sampling_res)
        w, h = freqz(b=self.b_coeff,
                     a=self.a_coeff,
                     fs=self._freq,
                     worN=int(nb_sampling))
        amp = 20 * np.log10(abs(h))
        self.frequencies = w
        self.ampl = amp

        if display:
            fig, ax1 = plt.subplots()
            ax1.set_title('Digital filter frequency response')
            ax1.plot(w, amp, 'b')
            ax1.set_ylabel('Amplitude [dB]', color='b')
            ax1.set_xlabel('Frequency [Hz]')
            plt.show()

        data_out = pd.DataFrame({'frequencies': self.frequencies, 'amplitude (dB)': self.ampl})
        data_out = data_out.set_index('frequencies')
        return data_out
