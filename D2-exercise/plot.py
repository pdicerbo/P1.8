import numpy as np
import matplotlib.pyplot as plt

dat = np.loadtxt('ResultsToPlotCPU')

matsize = dat[:,0]
flops   = dat[:,1]

plt.plot(matsize, flops, '-o')
plt.title('HPL - Cuda Benchmark')
plt.xlabel('Matrix size')
plt.ylabel('GFLOPS')
# plt.show()
plt.savefig('HPL_CPU_Benchmark.png')
