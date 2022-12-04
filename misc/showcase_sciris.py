# Define random wave generator
import numpy as np

noisevals = np.linspace(0, 10, 11)

def randwave(std, xmin=0, xmax=10, npts=50):
    np.random.seed() # Ensure differences between runs
    a = np.cos(np.linspace(xmin, xmax, npts))
    b = np.random.randn(npts)
    return a + b*std

# Other imports
import sciris as sc

# Start timing
T = sc.timer()

# Create object in parallel
output = sc.parallelize(randwave, noisevals)

# Save to files
filenames = sc.autolist()
for n,noiseval in enumerate(noisevals):
    filename = f'noise{noiseval}.obj'
    sc.save(filename, output[n])
    filenames += filename

# Create dict from files
data = sc.odict({filename:sc.load(filename) for filename in filenames})

# Create 3D plot
sc.surf3d(data[:])

# Print elapsed time
T.toc()
