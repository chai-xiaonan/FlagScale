# Copyright (c) 2025, BAAI. All rights reserved.
#
# Copied from: https://github.com/NVIDIA-NeMo/Megatron-Bridge

from flagscale.train.bridge.models.nemotron.nemotron_bridge import NemotronBridge
from flagscale.train.bridge.models.nemotron.nemotron_provider import (
    Nemotron3ModelProvider4B,
    Nemotron3ModelProvider8B,
    Nemotron3ModelProvider22B,
    Nemotron4ModelProvider15B,
    Nemotron4ModelProvider340B,
    NemotronModelProvider,
)

__all__ = [
    "NemotronBridge",
    "NemotronModelProvider",
    "Nemotron3ModelProvider4B",
    "Nemotron3ModelProvider8B",
    "Nemotron3ModelProvider22B",
    "Nemotron4ModelProvider15B",
    "Nemotron4ModelProvider340B",
]
