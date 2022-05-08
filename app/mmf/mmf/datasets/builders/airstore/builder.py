# Copyright (c) Facebook, Inc. and its affiliates.

from app.mmf.mmf.common.registry import registry
from app.mmf.mmf.datasets.builders.airstore.dataset import AirstoreDataset
from app.mmf.mmf.datasets.mmf_dataset_builder import MMFDatasetBuilder


@registry.register_builder("airstore")
class AirstoreDatasetBuilder(MMFDatasetBuilder):
    def __init__(
        self, dataset_name="airstore", dataset_class=AirstoreDataset, *args, **kwargs
    ):
        super().__init__(dataset_name)
        self.dataset_class = AirstoreDataset

    @classmethod
    def config_path(cls):
        return "configs/datasets/airstore/defaults.yaml"
