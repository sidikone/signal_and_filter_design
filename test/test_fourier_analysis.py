import sys
from os.path import abspath
sys.path.append(abspath('../include'))

from signal_generation import SignalGenerator
from fourier_analysis import SpectralAnalysis


def test_compute_fourier_spectrum():
    sign = SignalGenerator(sampling_freq=250, signal_length=10,
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
    sign = SignalGenerator(sampling_freq=250, signal_length=10,
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
    sign = SignalGenerator(sampling_freq=250, signal_length=10,
                           multiple_sine=[(2.5, 5), (5, 3), (2, 7)])
    sign.add_noise(3.5)
    data = sign.get_data_into_pandas_format()
    spec = SpectralAnalysis(sign)
    data_spec = spec.compute_spectral_density_using_welch(sampling_res=.1)
    data_spec_dB = spec.compute_spectral_density_using_welch(sampling_res=.1, typ='dB')

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
