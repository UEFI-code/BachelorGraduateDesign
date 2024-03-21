import pycuda.driver as cuda
import GPUEnergy
import time
import torch

cuda.init()
device = cuda.Device(0)
context = device.make_context()
print(f'GPU: {device.name()}')

# Init PyTorch computation
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

# Init Compute
LinearA(TensorA)
LinearB(TensorB)

# OK, Let's go!
myGPUConsume = GPUEnergy.GPUEnergy(0, 0.1)
print('-----------------Benchmark Start-----------------')
print('Test 1: 4096x4096 Tensor on 4096x4096 Linear, 1000 times, VRAM')
myGPUConsume.energyConsumed = 0
start = time.time()
for i in range(1000):
    LinearA(TensorA)
timeElapsed = time.time() - start
energyConsumed = myGPUConsume.energyConsumed
print(f'Time Elapsed: {timeElapsed} s, Energy Consumed: {energyConsumed} J')
print('Test 2: 4096x4096 Tensor on 4096x4096 Linear, 1000 times, DMA')
myGPUConsume.energyConsumed = 0
start = time.time()
for i in range(1000):
    LinearB(TensorB)
timeElapsed = time.time() - start
energyConsumed = myGPUConsume.energyConsumed
print(f'Time Elapsed: {timeElapsed} s, Energy Consumed: {energyConsumed} J')
print('-----------------Benchmark End-----------------')

context.pop()


