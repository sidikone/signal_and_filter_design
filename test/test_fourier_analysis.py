import sys
from os.path import abspath

sys.path.append(abspath('../include'))

# from os.path import dirname, abspath
# d = dirname(dirname(abspath(__file__)))

import matplotlib.pyplot as plt
from signal_generation import SignalGenerator
from fourier_analysis import SpectralAnalysis
from signal_filter import iirFilter
from signal_filter import firFilter


def test_compute_fourier_spectrum():
    sign = SignalGenerator(sampling_freq=250, signal_start=0, signal_end=10,
                           multiple_sine=[(2.5, 5), (5, 3), (2, 7)])
    sign.add_noise(3.5)
    data = sign.get_data_into_pandas_format()
    spec = SpectralAnalysis(sign)
    data_spec = spec.compute_fourier_spectrum()
    data_spec_dB = spec.compute_fourier_spectrum(typ='dB')

    nb_lin, nb_col = data.shape
    assert nb_lin == 2501
    assert nb_col == 2

    nb_l_spec, nb_c_spec = data_spec.shape
    assert nb_l_spec == 1250
    assert nb_c_spec == 2

    nb_l_spec_dB, nb_c_spec_dB = data_spec_dB.shape
    assert nb_l_spec_dB == 1250
    assert nb_c_spec_dB == 4
    return None


def test_compute_periodogram():
    sign = SignalGenerator(sampling_freq=250, signal_start=0, signal_end=10,
                           multiple_sine=[(2.5, 5), (5, 3), (2, 7)])
    sign.add_noise(3.5)
    data = sign.get_data_into_pandas_format()
    spec = SpectralAnalysis(sign)
    data_spec = spec.compute_spectral_density_using_periodogram()
    data_spec_dB = spec.compute_spectral_density_using_periodogram(typ='dB')

    nb_lin, nb_col = data.shape
    assert nb_lin == 2501
    assert nb_col == 2

    nb_l_spec, nb_c_spec = data_spec.shape
    assert nb_l_spec == 1251
    assert nb_c_spec == 2

    nb_l_spec_dB, nb_c_spec_dB = data_spec_dB.shape
    assert nb_l_spec_dB == 1251
    assert nb_c_spec_dB == 4
    return None


def test_compute_welch():
    sign = SignalGenerator(sampling_freq=250, signal_start=0, signal_end=10,
                           multiple_sine=[(2.5, 5), (5, 3), (2, 7)])
    sign.add_noise(3.5)
    data = sign.get_data_into_pandas_format()
    spec = SpectralAnalysis(sign)
    data_spec = spec.compute_spectral_density_using_welch()
    data_spec_dB = spec.compute_spectral_density_using_welch(typ='dB')

    nb_lin, nb_col = data.shape
    assert nb_lin == 2501
    assert nb_col == 2

    nb_l_spec, nb_c_spec = data_spec.shape
    assert nb_l_spec == 129
    assert nb_c_spec == 2

    nb_l_spec_dB, nb_c_spec_dB = data_spec_dB.shape
    assert nb_l_spec_dB == 129
    assert nb_c_spec_dB == 4
    return None

def main():

    sign = SignalGenerator(sampling_freq=250, signal_start=0, signal_end=10,
                           multiple_sine=[(2.5, 5), (5, 3), (2, 7)])
    sign.add_noise(3.5)
    data = sign.get_data_into_pandas_format()
    spec = SpectralAnalysis(sign)
    data_spec = spec.compute_spectral_density_using_welch()
    data_spec_dB = spec.compute_spectral_density_using_welch(typ='dB')

    data.plot()
    data_spec.plot()
    data_spec_dB.plot()
    plt.show()


if __name__ == "__main__":
    main()
