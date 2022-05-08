# Copyright (c) Facebook, Inc. and its affiliates.

from app.mmf.mmf.common.registry import registry
from app.mmf.mmf.datasets.builders.gqa.builder import GQABuilder
from app.mmf.mmf.datasets.builders.gqa.masked_dataset import MaskedGQADataset


@registry.register_builder("masked_gqa")
class MaskedGQABuilder(GQABuilder):
    def __init__(self):
        super().__init__()
        self.dataset_name = "masked_gqa"
        self.dataset_class = MaskedGQADataset

    @classmethod
    def config_path(cls):
        return "configs/datasets/gqa/masked.yaml"
