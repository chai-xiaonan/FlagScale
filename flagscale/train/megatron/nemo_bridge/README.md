#Before using this function, you need to install megatron-bridge
git clone https://github.com/NVIDIA-NeMo/Megatron-Bridge.git
cd Megatron-Bridge
pip install --no-build-isolation megatron-bridge

#You must install Megatron-Bridge first, and then install the Megatron-LM-FL version of Megatron-Core.
git clone https://github.com/flagos-ai/Megatron-LM-FL.git
cd Megatron-LM-FL
pip install --no-build-isolation .
