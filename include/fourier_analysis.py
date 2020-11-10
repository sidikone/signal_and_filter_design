import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import scipy.signal as ss
from scipy.fft import fft

class SpectralAnalysis:

    def __init__(self, other):

        self._amplitude = 0
        self._frequencies = 0
        self.frequency_data = pd.DataFrame()

        if type(other) == type(pd.DataFrame()):
            print("yeah")
            self.data = other.copy()
            self.sampling_freq, self.sampling_period = self._get_sampling_info(self.data)

        else:
            print("yolo")
            self.data = other.get_data_into_pandas_format()
            self.sampling_freq, self.sampling_period = self._get_sampling_info(self.data)

    def _compute_timedelta(self, data):
        diff = data.index.to_series().diff()
        #        time_delta = [time.total_seconds() for time in diff]
        #        return time_delta[1:]
        return diff[1:]

    def _get_sampling_info(self, data):
        time_delta = self._compute_timedelta(data)
        dt = np.round(np.median(time_delta), 2)
        fs = np.round(1 / dt, 2)

        return fs, dt

    def compute_fourier_spectrum(self):
        for col in self.data.columns.values:

            new=fft(self.data[col].values)
            _lines, _cols = self.data.shape
            xf = np.linspace(0.0, 1.0 / (2.0 * self.sampling_period), _lines // 2)
            new = 2/_lines * np.abs(new[0:_lines//2])
            fig, ax = plt.subplots()
            ax.plot(xf, new)
