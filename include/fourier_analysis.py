import matplotlib.pyplot as plt
import pandas as pd
import scipy.signal as ss


class SpectralAnalysis:

    def __init__(self, sampling_freq):
        self._sampling_freq = sampling_freq
