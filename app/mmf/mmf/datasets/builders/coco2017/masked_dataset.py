# Copyright (c) Facebook, Inc. and its affiliates.

from app.mmf.mmf.common.typings import MMFDatasetConfigType
from app.mmf.mmf.datasets.builders.localized_narratives.masked_dataset import (
    MaskedLocalizedNarrativesDatasetMixin,
)
from app.mmf.mmf.datasets.mmf_dataset import MMFDataset


class MaskedCoco2017Dataset(MaskedLocalizedNarrativesDatasetMixin, MMFDataset):
    def __init__(
        self,
        config: MMFDatasetConfigType,
        dataset_type: str,
        index: int,
        *args,
        **kwargs,
    ):
        super().__init__(
            "masked_coco2017", config, dataset_type, index, *args, **kwargs
        )
