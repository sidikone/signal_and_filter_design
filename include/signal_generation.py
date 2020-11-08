import matplotlib.pyplot as plt
import numpy as np

error1 = "end value must be greater than start value !"


class SignalGenerator:

    def __init__(self, sampling_freq=100, signal_freq=1, signal_ampl=1, signal_start=0, signal_end=1, multiple_sine=[]):

        self._multiple_gen_trig = False
        self._sampling_freq = sampling_freq
        self._signal_start = signal_start
        self._signal_end = signal_end
        if self._signal_start > self._signal_end:
            raise ValueError(error1)
        self._time = self._time_gen(True)
        self.noise = 0
        self.noise_signal = 0

        if len(multiple_sine) == 0:
            self._sampling_period = 1. / self._sampling_freq
            self._signal_freq = signal_freq
            self._signal_ampl = signal_ampl
            self._signal = self._amplitude_gen(True)

        else:
            self._multiple_gen_trig = True
#            self.freq_nam = "("
            self.multiple_freq = []
            self.multiple_signal_generation(multiple_sine)

    def _time_gen(self, init=True):
        self._sampling_period = 1. / self._sampling_freq
        local_time = np.arange(self._signal_start, self._signal_end + self._sampling_period, self._sampling_period)
        if init:
            return local_time
        else:
            self._time = local_time
            return None

    def _amplitude_gen(self, init=True):
        local_signal = self._signal_ampl * np.sin(2 * np.pi * self._signal_freq * self._time)
        if init:
            return local_signal
        else:
            self._signal = local_signal
            return None

    def signal_generation(self):

        if self._multiple_gen_trig:
            self._time_gen(False)
            self._m_signal_generation()

        else:
            self.single_signal_generation()
        return None

    def single_signal_generation(self):
        self._time_gen(False)
        self._amplitude_gen(False)
        return None

    def _m_signal_generation(self):

        first = True
        for (freq, ampl) in self.multiple_freq:
            if first:
                self._signal = ampl * np.sin(2 * np.pi * freq * self._time)
#                self.freq_nam += str(freq)
                first = False
            else:
                self._signal += ampl * np.sin(2 * np.pi * freq * self._time)
#                self.freq_nam += ", " + str(freq)

#        self.freq_nam += ")"
        return None

    def multiple_signal_generation(self, parameters_list=0):

        self.multiple_freq = parameters_list
        self._m_signal_generation()

        return None

    def random_multiple_signal_generation(self, min_freq, max_frq, min_ampl, max_ampl, siz_data):
        self._multiple_gen_trig = True
        freq_data = self._generate_random_freq(min_value=min_freq, max_value=max_frq, siz_value=siz_data)
        ampl_data = self._generate_random_ampl(min_value=min_ampl, max_value=max_ampl, siz_value=siz_data)

        ampl_and_freq = []
        for ind, freq in enumerate(freq_data):
            ampl_and_freq.append((freq, ampl_data[ind]))

        self.multiple_signal_generation(ampl_and_freq)


        return None

    def add_noise(self, std):

        self.noise = std
        self.noise_signal = self._signal + std*np.random.randn(len(self._time))
        return None

    @staticmethod
    def _generate_random_freq(min_value, max_value, siz_value):

        std_value = (max_value - min_value)/2
        mean_value = (min_value + max_value) / 2

        data_out = std_value * np.random.randn(siz_value) + mean_value
        data_out = np.abs(np.round(data_out, 2))
        return data_out

    @staticmethod
    def _generate_random_ampl(min_value, max_value, siz_value):

        return np.random.random_integers(min_value, max_value, siz_value)

    def plot_signal(self, show=False):
        fig, ax = plt.subplots()
        ax.set_ylabel("Amplitude")
        ax.set_xlabel("Time")

        if self._multiple_gen_trig:
            ax.plot(self._time, self.noise_signal, label=" Hz")
            ax.plot(self._time, self._signal, label=" Hz")
#            ax.plot(self._time, self._signal, label=self.freq_nam + " Hz")

        else:
            ax.plot(self._time, self.noise_signal, label="noise")
            ax.plot(self._time, self._signal, label=str(self._signal_freq) + " Hz")

        if show:
            ax.legend()
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
        self.signal_generation()

    def set_signal_freq(self, freq):
        self._signal_freq = freq
        self.signal_generation()

    def set_signal_ampl(self, ampl):
        self._signal_ampl = ampl
        self.signal_generation()

    def set_signal_length(self, start=0, end=1):
        self._signal_start = start
        self._signal_end = end
        if self._signal_start > self._signal_end:
            raise ValueError(error1)
        self.signal_generation()


def main():
    sign1 = SignalGenerator(sampling_freq=50, signal_start=0, signal_end=10)
#    sign1 = SignalGenerator(sampling_freq=500, signal_freq=2, signal_ampl=10, signal_start=0, signal_end=1)
#    sign1.plot_signal(False)
#    sign1.set_signal_length(start=1, end=15)
#    sign1.add_noise(5)
#    sign1.plot_signal(True)

    sign1.random_multiple_signal_generation(min_freq=0, max_frq=.5, min_ampl=2, max_ampl=50, siz_data=10)
    sign1.set_signal_length(start=0, end=30.0)
    sign1.add_noise(9)
    sign1.plot_signal(True)



#    sign1.set_signal_ampl(ampl=12)
#    sign1.set_signal_freq(freq=40)
#    sign1.plot_signal(True)


#    sign1.set_signal_freq(5)
#    sign1.multiple_signal_generation([(2, 5), (12, 6) ,(7, 10)])

#    sign2 = SignalGenerator()
#    sign2.set_signal_freq(2.5)
#    sign2.set_signal_length(start=2, end=5)

#    sign1.plot_signal(True)
# sign1.set_signal_ampl(10)
# sign2.set_signal_ampl(2.5)
#
# # sign1.plot_signal(False)
# # sign2.plot_signal(False)
# sign1.plot_multiple(sign2, True)


if __name__ == "__main__":
    main()
 #   print(np.random.random_integers(0, 5, 5))
 #   print(np.random.random_integers(0, 5, 5))
 #   print(3*np.random.randn(5)+10)