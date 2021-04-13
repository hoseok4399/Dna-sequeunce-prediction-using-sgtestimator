from collections import Counter
import pandas as pd


def generate_freq_table(samples):
    sample_histogram = Counter(samples)
    sample_histogram_val = sample_histogram.values()
    freq_table = Counter(sample_histogram_val)
    return freq_table


def cumulative_counts(samples):
    df = pd.DataFrame(samples, columns=['species'])
    df_new = ~df.duplicated()
    cum_counts = [0] + list(df_new.cumsum(axis=0))
    return cum_counts