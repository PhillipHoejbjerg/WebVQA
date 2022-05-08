# Copyright (c) Facebook, Inc. and its affiliates.
from app.mmf.mmf.common.registry import registry
from app.mmf.mmf.datasets.builders.vizwiz.dataset import VizWizDataset
from app.mmf.mmf.datasets.builders.vqa2 import VQA2Builder


@registry.register_builder("vizwiz")
class VizWizBuilder(VQA2Builder):
    def __init__(self):
        super().__init__()
        self.dataset_name = "vizwiz"
        self.set_dataset_class(VizWizDataset)

    @classmethod
    def config_path(cls):
        return "configs/datasets/vizwiz/defaults.yaml"

    def update_registry_for_model(self, config):
        super().update_registry_for_model(config)
