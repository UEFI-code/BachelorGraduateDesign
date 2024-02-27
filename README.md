# My Bachelor Graduation Design

```
On the lonely road of coding, long and winding,
Poverty's shackles often leave hearts pining.
But I believe, despite all the pain and sorrow,
My thesis shall bring forth a brighter tomorrow.

PyTorch_For_PoorGuys, a name not renowned,
Yet with dreams in my heart, aspirations unbound.
Harnessing CPU might to transcend VRAM's plight,
May my design illuminate, dispelling the night.

In the ocean of tech, I journey with zest,
Exploring, challenging limits, never at rest.
May my thesis, like the North Star, guide the way,
Breaking poverty's chains, bringing forth a new day.


Poem written by OpenAI's ChatGPT 3.5
```

###### PyTorch_For_PoorGuys: A Deep Learning Framework for Training Large-Language-Model on Cheap Workstation with Smaller VRAM required.

NVIDIA GeForce 1080Ti/2080Ti/3090/4090 are cheaper for Universitys or personal researchers.

LLM was famous and Omoshiroii since OpenAI GPT-3 proposed.

However, caused by its smaller Video-RAM, it is hard to train a LLM on orginal PyTorch.

I want to let GPU borrow some Host-RAM to buffer LLM data when its VRAM has been exhausted.

So I do a fork with original PyTorch and modified its code to enable DMA method.

You can download the prebuilt wheel installer file of the hacked version of PyTorch from [here](https://github.com/UEFI-code/PyTorch_For_PoorGuys/releases), or build it yourself from source code!

### Features

- Allocated Memory Buffer on VRAM first for Lower Latency, once the VRAM exhausted, it automatic allocated from Host RAM
- Create a Memory Pointer which can be both accessed from CPU or GPU side (Need hacking code yourself for completely using DMA)
- Zero-copy method possible to speed up (Also need yourself hacking code)

### Future

- Hacking the GPU Driver to DIY Memory-Management-Unit, enable more flexable way to play with GPU
- Let GPU controlling Hardware (Like Servo Motors) using Host Physic-Address via DMA directly
- Use FPGA to design a Physics Address Listener via PCI-E and DMA to interaction with GPU
- It will be interesting when Sensor signal can be passed to the Deep-Learning-Model in parallel directly, and the Model output signal can controlling device in parallel directly, just let CPU to sleep!

### Hardware Requirement

- NVIDIA Gefore 1080Ti/2080Ti/3090/4090 Graphic Card
- Compatible motherboard and Power Supply
- Intel Xeon E5-2620 V4 or Higher CPU
- 128GB DDR4 RAM or Higher
- 1TB SSD or Higher

### Software Requirement

- Debian Style of Linux, Ubuntu 20.04 LTS is suggested
- PyTorch 2.0 Compatible GPU Driver
- PyTorch 2.0 Compatible CUDA Developer Toolkit. See Build sections for details in Backend modules README.md file
- A GUI environment with browser to run frontend HTML code (Can be on your laptop or another computer)

### File Directory Structure

- Backend
    - [PyTorch_For_PoorGuys](https://github.com/UEFI-code/PyTorch_For_PoorGuys): The Core Module I have been proposed.
    - [DeepSpeedExamples](https://github.com/UEFI-code/DeepSpeedExamples): The LLM training & infering code that I forked and modified from Microsoft's Repo
- Frontend
    - playground.html: The HTML & Javascript Demo site that connect to Backend.
    - dummyBackend.py: The Python & Flask code that mook Backend response to debugging Frontend

### Sync the Repo

```bash
git clone --recursive https://github.com/UEFI-code/BachelorGraduationDesign
```

Or if you have already cloned the repo, you can sync the submodules by:

```bash
git submodule update --init --recursive
```

If the sync of submodules has error, then you can try to reset the submodules by:

```bash
git submodule foreach git reset --hard
```

### Notice

- This code will not Allocate Pageable Host Memory, which means it occupy Physic RAM at runtime
- Never pass a Memory Pointer which need CPU do Exception-Handling to GPU, or you will get crash