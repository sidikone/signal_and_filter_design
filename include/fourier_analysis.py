import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.fft import fft
from scipy.signal import periodogram
from scipy.signal import welch


class SpectralAnalysis:

    def __init__(self, other):

        self._amplitudes = []
        self._amplitudes_dB = []
        self._frequencies = 0

        self.dataFrame = 0

        if type(other) == type(pd.DataFrame()):
            self.data = other.copy()
            self.sampling_freq, self.sampling_period = self._get_sampling_info(self.data)

        else:
            self.data = other.get_data_into_pandas_format()
            self.sampling_freq, self.sampling_period = self._get_sampling_info(self.data)

    def _compute_timedelta(self, data):
        diff = data.index.to_series().diff().dropna()
        time_delta = [time.total_seconds() for time in diff]
        return time_delta

    def _get_sampling_info(self, data):
        time_delta = self._compute_timedelta(data)
        dt = np.round(np.median(time_delta), 8)
        fs = np.round(1 / dt, 8)

        return fs, dt

    def _compute_frequencies(self):
        _lines, _cols = self.data.shape
        freq = np.linspace(0.0, 1.0 / (2.0 * self.sampling_period), _lines // 2)
        return freq

    def _compute_fft(self, col_in):
        _lines, _cols = self.data.shape
        fft_values = fft(self.data[col_in].values)
        fft_values = (2 / _lines) * np.abs(fft_values[0:_lines // 2])
        return fft_values

    def _compute_periodogram(self, col_in, typ=None):
        freq_out, ampl_out = periodogram(self.data[col_in].values, self.sampling_freq)
        if typ is not None:
            freq_out, ampl_out = periodogram(self.data[col_in].values, self.sampling_freq, scaling='spectrum')
        return freq_out, ampl_out

    def _compute_welch(self, col_in, nb_sampl=256, typ=None):
        freq_out, ampl_out = welch(x=self.data[col_in].values, fs=self.sampling_freq, nperseg=nb_sampl)
        if typ is not None:
            freq_out, ampl_out = welch(x=self.data[col_in].values, fs=self.sampling_freq, nperseg=nb_sampl, scaling='spectrum')
        return freq_out, ampl_out

    def compute_fourier_spectrum(self, typ=None):

        self._frequencies = self._compute_frequencies()
        for col in self.data.columns.values:
            self._amplitudes.append(self._compute_fft(col))

        if typ is not None:
            for col in self.data.columns.values:
                self._amplitudes_dB.append(20 * np.log10(abs(self._compute_fft(col))))

        self.get_data_into_pandas_format(add_suffix='(dB)', typ=typ)
        return self.dataFrame

    def compute_spectral_density_using_periodogram(self, typ=None):

        for col in self.data.columns.values:
            freq, ampl = self._compute_periodogram(col_in=col)
            self._amplitudes.append(ampl)

        if typ is not None:
            for col in self.data.columns.values:
                freq, ampl = self._compute_periodogram(col_in=col, typ=typ)
                self._amplitudes_dB.append(ampl)

        self._frequencies = freq
        self.get_data_into_pandas_format(add_suffix='(spectral)', typ=typ)
        return self.dataFrame

    def compute_spectral_density_using_welch(self, sampling_res=1, typ=None):

        nb_sampling = self.sampling_freq / sampling_res
        for col in self.data.columns.values:
            freq, ampl = self._compute_welch(col_in=col, nb_sampl=nb_sampling)
            self._amplitudes.append(ampl)

        if typ is not None:
            for col in self.data.columns.values:
                freq, ampl = self._compute_welch(col_in=col, nb_sampl=nb_sampling, typ=typ)
                self._amplitudes_dB.append(ampl)

        self._frequencies = freq
        self.get_data_into_pandas_format(add_suffix='(spectral)', typ=typ)
        return self.dataFrame

    def get_data_into_pandas_format(self, add_suffix, typ=None):

        self.dataFrame = pd.DataFrame({'Frequencies': self._frequencies})
        for ind, col in enumerate(self.data.columns.values):
            self.dataFrame[col] = self._amplitudes[ind]
        if typ is not None:
            for ind, col in enumerate(self.data.columns.values):
                self.dataFrame[col + add_suffix] = self._amplitudes_dB[ind]

        self.dataFrame = self.dataFrame.set_index('Frequencies')
