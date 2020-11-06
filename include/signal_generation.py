import matplotlib.pyplot as plt
import numpy as np
import math as m


class signalGenerator:

    def __init__(self, sampling_freq=100, signal_freq=1, signal_ampl=1):
        self._sampling_freq = sampling_freq
        self._signal_freq = signal_freq
        self._signal_ampl = signal_ampl

        self._signal_start = 0
        self._signal_end = 1

        self._signal_generation()

    def _signal_generation(self) -> object:
        self._sampling_period = 1. / self._sampling_freq
        self._time = np.arange(self._signal_start, self._signal_end + self._sampling_period, self._sampling_period)
        self._signal = self._signal_ampl * np.sin(2 * np.pi * self._signal_freq * self._time)

        return None

    def plot_signal(self, show=False):
        self._signal_generation()
        fig, ax = plt.subplots()
        ax.set_ylabel("Amplitude")
        ax.set_xlabel("Time")
        plt.plot(self._time, self._signal)
        if show:
            plt.show()
        return None

    # getter methods
    def get_sample_freq(self):
        return self._sampling_freq

    def get_signal_freq(self):
        return self._signal_freq

    def get_signal_ampl(self):
        return self._signal_ampl

    def get_signal_length(self):
        return self._signal_start, self._signal_end

    def get_signal_data(self):
        self._signal_generation()
        return self._time, self._signal

    # setter methods
    def set_sample_freq(self, freq):
        self._sampling_freq = freq

    def set_signal_freq(self, freq):
        self._signal_freq = freq

    def set_signal_ampl(self, ampl):
        self._signal_ampl = ampl

    def set_signal_length(self, start=0, end=1):
        self._signal_start = start
        self._signal_end = end



def main():
    sign1 = signalGenerator()
    sign2 = signalGenerator()

    sign1.set_signal_freq(5)
    sign2.set_signal_freq(2.5)
    sign1.set_signal_ampl(10)
    sign2.set_signal_ampl(2.5)

    sign1.plot_signal(False)
    sign2.plot_signal(True)
    # sign1_x, sign1_y = sign1.get_signal_data()
    # sign2_x, sign2_y = sign2.get_signal_data()
    #
    # fig, ax = plt.subplots()
    # ax.plot(sign1_x, sign1_y)
    # ax.plot(sign2_x, sign2_y)
    # plt.show()

if __name__ == "__main__":
    main()


