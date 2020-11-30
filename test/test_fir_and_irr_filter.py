import sys
from os.path import abspath
sys.path.append(abspath('../include'))

# from os.path import dirname, abspath
# d = dirname(dirname(abspath(__file__)))
from signal_generation import SignalGenerator
from signal_filter import iirFilter
from signal_filter import firFilter


def test_iir_filter():
    sign = SignalGenerator(sampling_freq=50, signal_freq=2, signal_ampl=25, signal_length=10)
    sign.add_noise(3.5)
    data = sign.get_data_into_pandas_format()
    nb_lin, nb_col = data.shape

    assert nb_lin == 501
    assert nb_col == 2

    iir_design = iirFilter(sampling_freq=50,
                           low_freq=3,
                           high_freq=4,
                           attenuation_pass=1,
                           attenuation_stop=60,
                           typ='cheby2')
    freq_response = iir_design.compute_frequency_response(sampling_res=.1, display=False)
    nb_lin_fr, _ = freq_response.shape
    assert nb_lin_fr == 250

    filter_out = iir_design.apply_filter(data)
    nb_lin_filt, nb_col_filt = filter_out.shape

    assert nb_lin_filt == 501
    assert nb_col_filt == 2
    return None


def test_fir_filter():
    sign = SignalGenerator(sampling_freq=50, signal_freq=2, signal_ampl=25, signal_length=10)
    sign.add_noise(3.5)
    data = sign.get_data_into_pandas_format()
    nb_lin, nb_col = data.shape

    assert nb_lin == 501
    assert nb_col == 2

    fir_design = firFilter(num_taps=50,
                           cut_off=3.,
                           width=1.0,
                           window=('gaussian', 11),
                           fs=50)
    freq_response = fir_design.compute_frequency_response(sampling_res=.1, display=False)
    nb_lin_fr, _ = freq_response.shape
    assert nb_lin_fr == 250

    filter_out = fir_design.apply_filter(data)
    nb_lin_filt, nb_col_filt = filter_out.shape

    assert nb_lin_filt == 501
    assert nb_col_filt == 2
    return None
