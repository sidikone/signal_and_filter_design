import matplotlib.pyplot as plt
from signal_generation import SignalGenerator
from fourier_analysis import SpectralAnalysis


def main():

    sign1 = SignalGenerator(sampling_freq=50, signal_start=5, signal_end=100,
                            multiple_sine=[(.1, 5), (.5, 2.5), (.75, 10)])
    sign1.add_noise(2.5)
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
    plt.show()


if __name__ == "__main__":
    main()
