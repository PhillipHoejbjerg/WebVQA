# Copyright (c) Facebook, Inc. and its affiliates.
from app.mmf.mmf.common.registry import registry
from app.mmf.mmf.datasets.builders.vqacp_v2.dataset import VQACPv2Dataset
from app.mmf.mmf.datasets.mmf_dataset_builder import MMFDatasetBuilder


@registry.register_builder("vqacp_v2")
class VQACPv2Builder(MMFDatasetBuilder):
    def __init__(
        self, dataset_name="vqacp_v2", dataset_class=VQACPv2Dataset, *args, **kwargs
    ):
        super().__init__(dataset_name, dataset_class, *args, **kwargs)

    @classmethod
    def config_path(cls):
        return "configs/datasets/vqacp_v2/defaults.yaml"
