from py3nvml import py3nvml
import time
import threading

class GPUEnergy:
    def __init__(self, gpu_num=0, dt=0.1):
        self.dt = dt
        self.energyConsumed = 0
        py3nvml.nvmlInit()
        try:
            self.handle = py3nvml.nvmlDeviceGetHandleByIndex(gpu_num)
            self.gameOver = False
            threading.Thread(target=self.integralEnergy).start()
        except:
            print("GPU not found")
            return
    
    def integralEnergy(self):
        while not self.gameOver:
            power = py3nvml.nvmlDeviceGetPowerUsage(self.handle) / 1000
            self.energyConsumed += power * self.dt
            time.sleep(self.dt)