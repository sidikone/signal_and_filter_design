import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.signal as ss


class SpectralAnalysis:

    def __init__(self, other):
        self.sampling_freq, self.sampling_period = self._compute_timedelta(other)

    def _compute_timedelta(self, data):
        diff = data.index.to_series().diff()
        time_delta = [time.total_seconds() for time in diff]

        return time_delta[1:]

    def _get_sampling_info(self, data):
        time_delta = self._compute_timedelta(data)
        dt = np.median(time_delta)
        fs = 1 / dt

        return fs, dt