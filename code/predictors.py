import numpy as np
import scipy.stats as stats


def good_toulmin_predictor(freq_table, t, n):
    keys = freq_table.keys()
    vals = freq_table.values()
    t_power = np.power(-t, list(keys))
    series = np.multiply(t_power, list(vals))
    if t > 1:
        r = 1/(2*t)*np.log(n*(t+1)*(t+1)/(t-1))
        prob_array = stats.poisson.sf([key-1 for key in keys], r)
        series = np.multiply(series, prob_array)
    U_predict = -np.sum(series)
    return U_predict


def good_toulmin_range(freq_table, n, m):
    U_list = []
    for idx in range(1, m+1):
        t = idx/n
        U_predict = good_toulmin_predictor(freq_table, t, n)
        U_list.append(U_predict)
    return U_list