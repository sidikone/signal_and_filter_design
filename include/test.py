import matplotlib.pyplot as plt
from signal_generation import SignalGenerator
from fourier_analysis import SpectralAnalysis
from signal_filter import iirFilter


def main():

    sign1 = SignalGenerator(sampling_freq=50, signal_start=0, signal_end=10,
                            multiple_sine=[(.1, 5), (.5, 2.5), (.75, 10)])
    sign1.add_noise(5)
    data1 = sign1.get_data_into_pandas_format()
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
    plt.show()


if __name__ == "__main__":
    main()
