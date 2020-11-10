import matplotlib.pyplot as plt
from signal_generation import SignalGenerator
from fourier_analysis import SpectralAnalysis


def main():

    sign1 = SignalGenerator(sampling_freq=50, signal_start=4, signal_end=50,
                            multiple_sine=[(1, 25), (3, 5), (5, 15)])
    sign1.add_noise(10)
    data1 = sign1.get_data_into_pandas_format()

    spec1 = SpectralAnalysis(data1)
    data2 = spec1.compute_fourier_spectrum()
    data2.plot()
#    data1.plot()
    plt.show()




if __name__ == "__main__":
    main()
