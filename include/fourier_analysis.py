import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.fft import fft


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
        diff = data.index.to_series().diff()
        return diff.dropna()

    def _get_sampling_info(self, data):
        time_delta = self._compute_timedelta(data)
        dt = np.round(np.median(time_delta), 4)
        fs = np.round(1 / dt, 4)

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

    def compute_fourier_spectrum(self, typ=None):

        self._frequencies = self._compute_frequencies()
        for col in self.data.columns.values:
            self._amplitudes.append(self._compute_fft(col))

        if typ is not None:
            for col in self.data.columns.values:
                self._amplitudes_dB.append(20 * np.log10(self._compute_fft(col)))

        self.get_data_into_pandas_format(typ=typ)
        return self.dataFrame

    def get_data_into_pandas_format(self, typ):

        self.dataFrame = pd.DataFrame({'Frequencies': self._frequencies})
        for ind, col in enumerate(self.data.columns.values):
            self.dataFrame[col] = self._amplitudes[ind]
        if typ is not None:
            for ind, col in enumerate(self.data.columns.values):
                self.dataFrame[col+"(dB)"] = self._amplitudes_dB[ind]

        self.dataFrame = self.dataFrame.set_index('Frequencies')