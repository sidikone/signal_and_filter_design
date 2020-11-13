from scipy.signal import iirdesign
from scipy.signal import filtfilt

from scipy.signal import firwin
from scipy.ndimage import convolve1d
# from scipy.signal import firwin2

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

        self._amplitudes = []
        self.b_coeff = 0
        self.a_coeff = 0
        self.data = 0
        self.dataFrame = 0
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

    def _compute_iir_filter(self, col_in):

        data_out = filtfilt(self.b_coeff, self.a_coeff, self.data[col_in].values)
        return data_out

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

    def apply_filter(self, other):

        if type(other) == type(pd.DataFrame()):
            self.data = other.copy()

        else:
            self.data = other.get_data_into_pandas_format()

        for col in self.data.columns.values:
            self._amplitudes.append(self._compute_iir_filter(col))

        self.get_data_into_pandas_format()
        return self.dataFrame

    def get_data_into_pandas_format(self):

        self.dataFrame = pd.DataFrame({'Timestamp': self.data.index.values})
        for ind, col in enumerate(self.data.columns.values):
            self.dataFrame[col + '(filtered)'] = self._amplitudes[ind]

        self.dataFrame = self.dataFrame.set_index('Timestamp')
        return None


class firFilter:

    def __init__(self, num_taps, cut_off, width, window, fs):
        self._num_taps = num_taps
        self._cut_off = cut_off
        self._width = width
        self._window = window
        self._fs = fs

        self.coeff = 0
        self.frequencies = 0
        self.ampl = 0
        self.data = 0
        self.dataFrame = 0
        self._amplitudes = []
        self._design_filter()

    def _design_filter(self):
        self.coeff = firwin(numtaps=self._num_taps,
                            cutoff=self._cut_off,
                            width=self._width,
                            window=self._window,
                            fs=self._fs)

        return self.coeff

    def _compute_fir_filter(self, col_in, mod):

        data_out = convolve1d(input=self.data[col_in].values, weights=self.coeff, mode=mod)
        return data_out

    def compute_frequency_response(self, sampling_res=1, display=False):

        nb_sampling = self._fs / (2 * sampling_res)
        w, h = freqz(b=self.coeff,
                     a=1,
                     fs=self._fs,
                     worN=int(nb_sampling))
        amp = 20 * np.log10(abs(h))

        self.frequencies = w
        self.ampl = amp

        if display:
            fig, ax1 = plt.subplots()
            ax1.set_title('Digital filter frequency response')
            ax1.plot(w, amp, 'b')
            ax1.set_ylabel('Amplitude [dB]', color='b')
            ax1.set_xlabel("Frequency [Hz]")
            plt.show()

        data_out = pd.DataFrame({'frequencies': self.frequencies, 'amplitude (dB)': self.ampl})
        data_out = data_out.set_index('frequencies')

        return data_out

    def apply_filter(self, other, mode='reflect'):

        if type(other) == type(pd.DataFrame()):
            self.data = other.copy()

        else:
            self.data = other.get_data_into_pandas_format()

        for col in self.data.columns.values:
            self._amplitudes.append(self._compute_fir_filter(col, mod=mode))

        self.get_data_into_pandas_format()
        return self.dataFrame

    def get_data_into_pandas_format(self):

        self.dataFrame = pd.DataFrame({'Timestamp': self.data.index.values})
        for ind, col in enumerate(self.data.columns.values):
            self.dataFrame[col + '(filtered)'] = self._amplitudes[ind]

        self.dataFrame = self.dataFrame.set_index('Timestamp')
        return None
