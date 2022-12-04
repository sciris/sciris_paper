# Define random wave generator
import numpy as np

def randwave(std, xmin=0, xmax=10, npts=50):
    np.random.seed() # Ensure differences between runs
    a = np.cos(np.linspace(xmin, xmax, npts))
    b = np.random.randn(npts)
    return a + b*std

# Other imports
import time
import multiprocessing as mp
import pickle
import gzip
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Unused but must be imported

# Start timing
start = time.time()

# Calculate output in parallel
multipool = mp.Pool(processes=mp.cpu_count())
waves = multipool.map(randwave, np.arange(11))
multipool.close()
multipool.join()

# Save to files
filenames = []
for i in range(len(waves)):
    filename = f'noise{i}.obj'
    with gzip.GzipFile(filename, 'wb') as fileobj:
        fileobj.write(pickle.dumps(waves[i]))
    filenames.append(filename)

# Create dict from files
data_dict = {}
for fname in filenames:
    with gzip.GzipFile(fname) as fileobj:
        filestring = fileobj.read()
        data_dict[fname] = pickle.loads(filestring)

# Create 3D plot
data = np.array([data_dict[fname] for fname in filenames])
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.view_init(elev=45, azim=30)
ny,nx = np.array(data).shape
x = np.arange(nx)
y = np.arange(ny)
X, Y = np.meshgrid(x, y)
surf = ax.plot_surface(X, Y, data, cmap='viridis')
fig.colorbar(surf)

# Print elapsed time
elapsed = time.time() - start
print(f'Elapsed time: {elapsed:0.1f} s')
