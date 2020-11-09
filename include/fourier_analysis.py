import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.signal as ss


def get_sampling_info(data):
    time_delta = compute_timedelta(data)
    dt = np.median(time_delta)
    fs = 1 / dt

    return fs, dt


def compute_timedelta(data):
    """

    :param data:
    :return:
    """

    diff = data.index.to_series().diff()
    time_delta = [time.total_seconds() for time in diff]

    return time_delta[1:]


class SpectralAnalysis:

    def __init__(self, other):
        self.sampling_frequency = get_sampling_info(other)
