import matplotlib.pyplot as plt
import numpy as np

error1 = "end value must be greater than start value !"


class SignalGenerator:

    def __init__(self, sampling_freq=100, signal_freq=1, signal_ampl=1):
        self._sampling_freq = sampling_freq
        self._signal_freq = signal_freq
        self._signal_ampl = signal_ampl

        self._signal_start = 0
        self._signal_end = 1
        self._sampling_period = 1
        self._time = 0
        self._signal = 0

        self._multiple_gen_trig = False
        self.single_signal_generation()

    def _time_gen(self):
        self._sampling_period = 1. / self._sampling_freq
        self._time = np.arange(self._signal_start, self._signal_end + self._sampling_period, self._sampling_period)
        return None

    def _amplitude_gen(self):
        self._signal = self._signal_ampl * np.sin(2 * np.pi * self._signal_freq * self._time)
        return None

    def single_signal_generation(self):
        self._time_gen()
        self._amplitude_gen()
        return None

    def multiple_signal_generation(self, parameters_list=0):

        first = True
        self._multiple_gen_trig = True
        for (freq, ampl) in parameters_list:
            if first:
                self._signal = ampl * np.sin(2 * np.pi * freq * self._time)
                print("yeah")
                first = False
            else:
                self._signal += ampl * np.sin(2 * np.pi * freq * self._time)
            print(freq, "\t", ampl)

        return None

    def plot_signal(self, show=False):
        if not self._multiple_gen_trig:
            self.single_signal_generation()
        fig, ax = plt.subplots()
        ax.set_ylabel("Amplitude")
        ax.set_xlabel("Time")
        ax.plot(self._time, self._signal, label=str(self._signal_freq) + " Hz")
        ax.legend()
        if show:
            plt.show()
        return None

    def plot_multiple(self, other, show=False):
        self.single_signal_generation()
        other.single_signal_generation()
        other_time, other_signal = other.get_signal_data()

        fig, ax = plt.subplots()
        ax.set_ylabel("Amplitude")
        ax.set_xlabel("Time")
        ax.plot(self._time, self._signal, label=str(self._signal_freq) + " Hz")
        ax.plot(other_time, other_signal, label=str(other.get_signal_freq()) + " Hz")

        ax.legend()
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
        self.single_signal_generation()
        return self._time, self._signal

    # setter methods
    def set_sample_freq(self, freq):
        self._sampling_freq = freq
        self._time_gen()

    def set_signal_freq(self, freq):
        self._signal_freq = freq
        self._time_gen()

    def set_signal_ampl(self, ampl):
        self._signal_ampl = ampl
        self._amplitude_gen()

    def set_signal_length(self, start=0, end=1):
        self._signal_start = start
        self._signal_end = end
        if self._signal_start > self._signal_end:
            raise ValueError(error1)
        self._time_gen()


def main():
    sign1 = SignalGenerator()
    sign1.set_signal_freq(5)
    sign1.multiple_signal_generation([(2, 5), (12, 6) ,(7, 10)])

    sign2 = SignalGenerator()
    sign2.set_signal_freq(2.5)
    sign2.set_signal_length(start=2, end=5)

    sign1.plot_signal(True)
    # sign1.set_signal_ampl(10)
    # sign2.set_signal_ampl(2.5)
    #
    # # sign1.plot_signal(False)
    # # sign2.plot_signal(False)
    # sign1.plot_multiple(sign2, True)


if __name__ == "__main__":
    main()
