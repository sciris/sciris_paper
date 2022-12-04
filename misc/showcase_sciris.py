# Define random wave generator
import numpy as np

def randwave(std, xmin=0, xmax=10, npts=50):
    np.random.seed() # Ensure differences between runs
    a = np.cos(np.linspace(xmin, xmax, npts))
    b = np.random.randn(npts)
    return a + b*std

# Other imports
import sciris as sc

# Start timing
T = sc.timer()

# Calculate output in parallel
waves = sc.parallelize(randwave, np.arange(11))

# Save to files
filenames = [sc.save(f'noise{i}.obj', waves[i]) for i in range(len(waves))]

# Create dict from files
data = sc.odict({fname:sc.load(fname) for fname in filenames})

# Create 3D plot
sc.surf3d(data[:])

# Print elapsed time
T.toc()
