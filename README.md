# Bachelor Graduate Design

## PyTorch_For_PoorGuys: A Deep Learning Framework for Training Large-Language-Model on Cheap Workstation with Smaller VRAM required.

NVIDIA GeForce 1080Ti/2080Ti/3090/4090 are cheaper for high-school or personal researchers.

LLM was famous and Omoshiroii since OpenAI GPT-3 proposed.

However, caused by its smaller Video-RAM, it is hard to train a LLM on orginal PyTorch.

I want to let GPU borrow some Host-RAM to buffer LLM data when its VRAM has been exhausted.

So I do a fork with original PyTorch and modified its code to enable DMA method.