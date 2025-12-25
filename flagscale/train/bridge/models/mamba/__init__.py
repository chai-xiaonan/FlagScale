# Copyright (c) 2025, BAAI. All rights reserved.
#
# Copied from: https://github.com/NVIDIA-NeMo/Megatron-Bridge

from flagscale.train.bridge.models.mamba.mamba_provider import (
    MambaModelProvider,
    MambaModelProvider1P3B,
    MambaModelProvider2P7B,
    MambaModelProvider130M,
    MambaModelProvider370M,
    MambaModelProvider780M,
    MambaProvider,
    MambaProvider1_3B,
    MambaProvider2_7B,
    MambaProvider130M,
    MambaProvider370M,
    MambaProvider780M,
    NVIDIAMambaHybridModelProvider8B,
    NVIDIAMambaHybridProvider8B,
    NVIDIAMambaModelProvider8B,
    NVIDIAMambaProvider8B,
)

__all__ = [
    "MambaModelProvider",
    "MambaModelProvider1P3B",
    "MambaModelProvider2P7B",
    "MambaModelProvider130M",
    "MambaModelProvider370M",
    "MambaModelProvider780M",
    "NVIDIAMambaHybridModelProvider8B",
    "NVIDIAMambaModelProvider8B",
    "MambaProvider",
    "MambaProvider1_3B",
    "MambaProvider2_7B",
    "MambaProvider130M",
    "MambaProvider370M",
    "MambaProvider780M",
    "NVIDIAMambaHybridProvider8B",
    "NVIDIAMambaProvider8B",
]
