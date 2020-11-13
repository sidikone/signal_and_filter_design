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


def test_signal_generator_use_case_1():
    sign = SignalGenerator(sampling_freq=250, signal_start=0, signal_end=2,
                           multiple_sine=[(2.5, 5), (5, 3), (2, 7)])
    sign.add_noise(3.5)
    data = sign.get_data_into_pandas_format()

    nb_lin, nb_col = data.shape
    assert nb_lin == 501
    assert nb_col == 2
    return None


def test_signal_generator_use_case_2():
    sign = SignalGenerator(sampling_freq=250, signal_freq=10, signal_ampl=25, signal_start=0, signal_end=1)
    sign.add_noise(3.5)
    data = sign.get_data_into_pandas_format()

    nb_lin, nb_col = data.shape
    assert nb_lin == 251
    assert nb_col == 2
    return None


def main():
    sign1 = SignalGenerator(sampling_freq=250, signal_freq=10, signal_ampl=25, signal_start=0, signal_end=1)
    sign1.add_noise(3.5)
    data1 = sign1.get_data_into_pandas_format()
    print(data1.shape)

    data1.plot()
    spec1 = SpectralAnalysis(sign1)
    #    data2 = spec1.compute_fourier_spectrum()
    #    data2.plot()
    #    data1.plot()

    #    data3 = spec1.compute_spectral_density_using_periodogram(typ='dB')
    #    print(list(data3))
    #    data4 = data3[['raw_data(spectral)', 'noise_data(spectral)']]
    #    data4.plot()
    #    data3.plot()

    data5 = spec1.compute_spectral_density_using_welch(typ='dB')
    data5.plot()
    #    plt.show()

    dat = iirFilter(sampling_freq=50,
                    low_freq=5,
                    high_freq=10,
                    attenuation_pass=1,
                    attenuation_stop=80,
                    typ='cheby2')

    dat.compute_frequency_response(sampling_res=.05, display=False)
    data6 = dat.apply_filter(data1)
    data6.plot()

    dat2 = firFilter(num_taps=50,
                     cut_off=1.5,
                     width=5.0,
                     window=('gaussian', 11),
                     fs=50)
    did = dat2.compute_frequency_response(sampling_res=.05, display=False)
    dodo = dat2.apply_filter(data1)
    dodo.plot()
    print(did.head(5))
    plt.show()


if __name__ == "__main__":
    main()
