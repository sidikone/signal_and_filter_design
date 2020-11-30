import sys
from os.path import abspath
sys.path.append(abspath('../include'))

# from os.path import dirname, abspath
# d = dirname(dirname(abspath(__file__)))

import matplotlib.pyplot as plt
from signal_generation import SignalGenerator

def test_signal_generator_use_case_1():
    sign = SignalGenerator(sampling_freq=250, signal_length=2,
                           multiple_sine=[(2.5, 5), (5, 3), (2, 7)])
    sign.add_noise(3.5)
    data = sign.get_data_into_pandas_format()

    nb_lin, nb_col = data.shape
    assert nb_lin == 501
    assert nb_col == 2
    return None


def test_signal_generator_use_case_2():
    sign = SignalGenerator(sampling_freq=250, signal_freq=10, signal_ampl=25, signal_length=1)
    sign.add_noise(3.5)
    data = sign.get_data_into_pandas_format()

    nb_lin, nb_col = data.shape
    assert nb_lin == 251
    assert nb_col == 2
    return None