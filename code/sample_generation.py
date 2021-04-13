import numpy as np


def generate_samples_zipf(a, n):
    return np.random.zipf(a, size=n)


def generate_samples_uniform(N, n):
    return np.random.randint(N, size=n)


generate_samples_dict = {"unif": generate_samples_uniform,
                         "zipf": generate_samples_zipf}


def generate_samples(type, param, n):
    generate_samples_fcn = generate_samples_dict[type]
    return generate_samples_fcn(param, n)