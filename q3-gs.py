from math import sqrt
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt

def gaussian(count, mu=0, sigma=10, dim=1):
    return np.random.normal(mu, sigma, (count, dim))

def euclidean_norm(vec):
    if isinstance(vec, int) or isinstance(vec, float):
        return abs(vec)
    
    square_sum = reduce(lambda x, y: x + y ** 2, vec, 0)
    return sqrt(square_sum)

def average_and_stddev(iterable):
    average = sum(iterable) / len(iterable)
    norms_dev = reduce(lambda x, y: x + (y - average) ** 2, iterable, 0) / len(iterable)

    return average, sqrt(norms_dev)

def statistic_on_dim(dim, *, count):
    samples = gaussian(count, dim=dim)

    euclidean_norms = np.array([euclidean_norm(vec) for vec in samples])

    return samples, euclidean_norms, *average_and_stddev(euclidean_norms)



width = 20

def print_title_and_desc(title, *desc):
    print(' {} '.format(title).center(width, '-'))
    print('')

    for name, obj in desc:
        print(name + ':')
        print(obj)
        print('')


fig = plt.figure()

# Question a


samples, euclidean_norms_3, norms_average_3, norms_stddev_3 = statistic_on_dim(3, count=10000)

print_title_and_desc('d=3', ('sample result', samples))

samples, euclidean_norms_50, norms_average_50, norms_stddev_50 = statistic_on_dim(50, count=10000)

print_title_and_desc('d=50', ('sample result', samples))

samples, euclidean_norms_100, norms_average_100, norms_stddev_100 = statistic_on_dim(100, count=10000)

print_title_and_desc('d=100', ('sample result', samples))

samples, euclidean_norms_200, norms_average_200, norms_stddev_200 = statistic_on_dim(200, count=10000)

print_title_and_desc('d=200', ('sample result', samples))

samples, euclidean_norms_500, norms_average_500, norms_stddev_500 = statistic_on_dim(500, count=10000)

print_title_and_desc(' d=500', ('sample result', samples))

samples, euclidean_norms_1000, norms_average_1000, norms_stddev_1000 = statistic_on_dim(1000, count=10000)

print_title_and_desc('d=1000', ('sample result', samples))



# Question b
print_title_and_desc(
    'Question b-3',
    ('Euclidean norms 3', euclidean_norms_3),
    ('average', norms_average_3),
    ('standard deviation', norms_stddev_3)
)

print_title_and_desc(
    'Question b-50',
    ('Euclidean norms 50', euclidean_norms_50),
    ('average', norms_average_50),
    ('standard deviation', norms_stddev_50)
)

print_title_and_desc(
    'Question b-100',
    ('Euclidean norms', euclidean_norms_100),
    ('average', norms_average_100),
    ('standard deviation', norms_stddev_100)
)

print_title_and_desc(
    'Question b-200',
    ('Euclidean norms', euclidean_norms_200),
    ('average', norms_average_200),
    ('standard deviation', norms_stddev_200)
)

print_title_and_desc(
    'Question b-500',
    ('Euclidean norms', euclidean_norms_500),
    ('average', norms_average_500),
    ('standard deviation', norms_stddev_500)
)

print_title_and_desc(
    'Question b-1000',
    ('Euclidean norms', euclidean_norms_1000),
    ('average', norms_average_1000),
    ('standard deviation', norms_stddev_1000)
)

plt.subplot(231)
plt.title('Euclidean norms when d=3')
plt.hist(euclidean_norms_3, bins=100)

plt.subplot(232)
plt.title('Euclidean norms when d=50')
plt.hist(euclidean_norms_50, bins=100)

plt.subplot(233)
plt.title('Euclidean norms when d=100')
plt.hist(euclidean_norms_100, bins=100)

plt.subplot(234)
plt.title('Euclidean norms when d=200')
plt.hist(euclidean_norms_200, bins=100)

plt.subplot(235)
plt.title('Euclidean norms when d=500')
plt.hist(euclidean_norms_500, bins=100)

plt.subplot(236)
plt.title('Euclidean norms when d=1000')
plt.hist(euclidean_norms_1000, bins=100)

# Question c
dims = [50, 100, 200, 500, 1000]


statistics = np.array([statistic_on_dim(dim, count=10000) for dim in dims])
average_values = statistics[:, 2]
stddev_values = statistics[:, 3]

print_title_and_desc(
    'Question c',
    ('average values with incresing d', average_values),
    ('standard deviation with increasing d', stddev_values)
)
plt.figure()
x = range(len(dims))

plt.subplot(121)
plt.title('average values with increasing d')
plt.bar(x, average_values)
plt.xticks(x, dims)

plt.subplot(122)
plt.title('standard deviation with increasing d')
plt.bar(x, stddev_values)
plt.xticks(x, dims)

fig.tight_layout()
plt.show()