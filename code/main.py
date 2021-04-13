import matplotlib.pyplot as plt
import numpy as np
import random
from predictors import good_toulmin_range
from utils import generate_freq_table, cumulative_counts


def generate_read_starts(G, L, N):

    f = open("sequencingsample.txt", 'w')
    sampleList = ['A', 'C', 'G', 'T']
    Total_DNA = [random.choice(sampleList) for i in range(G)]

    prob_array = np.random.uniform(0, 1, G - L + 1)
    prob_array = prob_array / np.sum(prob_array)

    prob_cumsum = np.cumsum(prob_array)
    prob_cumsum = np.insert(prob_cumsum, 0, 0)

    sample = np.random.uniform(0, 1, N)
    read_starts = np.searchsorted(prob_cumsum, sample) - 1

    for a in read_starts:
        f.write(''.join(Total_DNA[a:a + L]))
        f.write(str(a) + "\n")
    f.close()
    return read_starts


def get_samples(N,L):

    f = open("sequencingsample.txt", 'r')
    read_starts = []
    while True:
        line = f.readline()
        if not line: break
        read_starts.append(line[L:-2])
    f.close()

    read_starts = np.asarray(read_starts[:N],dtype=int)
    reads = [read_starts+shift for shift in range(L)]
    samples = np.concatenate(reads, axis=None)
    return samples

def search_read(li, value):
    a = np.searchsorted(li, value)
    if a == len(li):
            print("expected read number is bigger than %d" % len(li))
    else :
        print ("expected read number is %d " %(a))

G = 10000000
L = 100
N = 2000
t = 4
M = t * N
search_value = 250000

print("sampling reads")
read_starts = generate_read_starts(G, L, N + M)
samples = get_samples(N, L)

print("generating freq tables")
freq_table = generate_freq_table(samples)


print("estimating")
U_list = good_toulmin_range(freq_table, N, M)

print("counting cumulatives")
whole_samples = get_samples(M+N,L)
cum_counts = cumulative_counts(whole_samples)[::L]

print("plotting")

U_list = [U + cum_counts[N] for U in U_list]

plt.plot(range(N+M+1), cum_counts, range(N+1,N+M+1), U_list, 'r')
plt.show()

search_read(U_list,search_value)
