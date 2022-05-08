# Copyright (c) Facebook, Inc. and its affiliates.
from app.mmf.mmf.common.registry import registry
from app.mmf.mmf.datasets.builders.visual_genome.detection_dataset import (
    DetectionVisualGenomeDataset,
)
from app.mmf.mmf.datasets.mmf_dataset_builder import MMFDatasetBuilder


@registry.register_builder("detection_visual_genome")
class DetectionVisualGenomeBuilder(MMFDatasetBuilder):
    def __init__(self):
        super().__init__(
            dataset_name="detection_visual_genome",
            dataset_class=DetectionVisualGenomeDataset,
        )

    @classmethod
    def config_path(cls):
        return "configs/datasets/visual_genome/detection.yaml"
