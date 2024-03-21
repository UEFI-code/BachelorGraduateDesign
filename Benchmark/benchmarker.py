import pycuda.driver as cuda
import GPUEnergy
import time
import torch
from tqdm import tqdm
import sys

cuda.init()
device = cuda.Device(0)
context = device.make_context()
gpuName = device.name()
cpuName = open('/proc/cpuinfo').read().split('model name\t: ')[1].split('\n')[0]

# Init PyTorch operations on GPU
LinearA = torch.nn.Linear(4096, 4096).cuda()
TensorA = torch.randn(4096, 4096).cuda()

# Allocate Huge GPU Memory
free, total = cuda.mem_get_info()
print(f'GPU Memory Free: {free / 1024 / 1024} MB')
p = cuda.mem_alloc(free - 1020 * 1024 * 1024)
free, total = cuda.mem_get_info()
print(f'Now GPU Memory Free: {free / 1024 / 1024} MB')

# Then the following code will be run via DMA, GPU accessing CPU's memory
LinearB = torch.nn.Linear(4096, 4096).cuda()
TensorB = torch.randn(4096, 4096).cuda()

# Init PyTorch operations on CPU
LinearC = torch.nn.Linear(4096, 4096)
TensorC = torch.randn(4096, 4096)

# Init Compute
LinearA(TensorA)
LinearB(TensorB)
LinearC(TensorC)

# OK, Let's go!

myGPUConsume = GPUEnergy.GPUEnergy(0, 0.1)

def doTestGPU(myGPUConsume, Linear, Tensor):
    myGPUConsume.energyConsumed = 0
    start = time.time()
    for _ in range(1000):
        Linear(Tensor)
    timeElapsed = time.time() - start
    energyConsumed = myGPUConsume.energyConsumed
    print(f'Time Elapsed: {timeElapsed} s, Energy Consumed: {energyConsumed} J')

def doTestCPU(Linear, Tensor):
    start = time.time()
    for _ in tqdm(range(1000)):
        Linear(Tensor)
    timeElapsed = time.time() - start
    print(f'Time Elapsed: {timeElapsed} s')

print('-----------------Benchmark Start-----------------')
print(f'Test 1: 4096x4096 Tensor on 4096x4096 Linear, 1000 times, {gpuName}, VRAM')
doTestGPU(myGPUConsume, LinearA, TensorA)
print(f'Test 2: 4096x4096 Tensor on 4096x4096 Linear, 1000 times, {gpuName}, DMA')
doTestGPU(myGPUConsume, LinearB, TensorB)
### Test3 will be run on CPU, so we need to stop the GPU energy consumption
myGPUConsume.gameOver = True
print(f'Test 3: 4096x4096 Tensor on 4096x4096 Linear, 1000 times, {cpuName}, RAM')
doTestCPU(LinearC, TensorC)
print('-----------------Benchmark End-----------------')
context.pop()