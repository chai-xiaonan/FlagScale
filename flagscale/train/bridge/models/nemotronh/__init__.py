# Copyright (c) 2025, BAAI. All rights reserved.
#
# Copied from: https://github.com/NVIDIA-NeMo/Megatron-Bridge

from flagscale.train.bridge.models.nemotronh.nemotron_h_bridge import NemotronHBridge
from flagscale.train.bridge.models.nemotronh.nemotron_h_provider import (
    NemotronHModel4BProvider,
    NemotronHModel8BProvider,
    NemotronHModel47BProvider,
    NemotronHModel56BProvider,
    NemotronHModelProvider,
    NemotronHModelProvider4B,
    NemotronHModelProvider8B,
    NemotronHModelProvider47B,
    NemotronHModelProvider56B,
    NemotronNano9Bv2Provider,
    NemotronNano12Bv2Provider,
    NemotronNanoModelProvider9Bv2,
    NemotronNanoModelProvider12Bv2,
)

__all__ = [
    "NemotronHModelProvider",
    "NemotronHModelProvider4B",
    "NemotronHModelProvider8B",
    "NemotronHModelProvider47B",
    "NemotronHModelProvider56B",
    "NemotronNanoModelProvider9Bv2",
    "NemotronNanoModelProvider12Bv2",
    "NemotronHModel4BProvider",
    "NemotronHModel8BProvider",
    "NemotronHModel47BProvider",
    "NemotronHModel56BProvider",
    "NemotronNano9Bv2Provider",
    "NemotronNano12Bv2Provider",
]
