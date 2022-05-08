# Copyright (c) Facebook, Inc. and its affiliates.

from app.mmf.mmf.datasets.processors.bert_processors import MaskedTokenProcessor
from app.mmf.mmf.datasets.processors.frcnn_processor import FRCNNPreprocess
from app.mmf.mmf.datasets.processors.image_processors import TorchvisionTransforms
from app.mmf.mmf.datasets.processors.prediction_processors import ArgMaxPredictionProcessor
from app.mmf.mmf.datasets.processors.processors import (
    BaseProcessor,
    BBoxProcessor,
    CaptionProcessor,
    FastTextProcessor,
    GloVeProcessor,
    GraphVQAAnswerProcessor,
    MultiHotAnswerFromVocabProcessor,
    Processor,
    SimpleSentenceProcessor,
    SimpleWordProcessor,
    SoftCopyAnswerProcessor,
    VocabProcessor,
    VQAAnswerProcessor,
)


__all__ = [
    "BaseProcessor",
    "Processor",
    "VocabProcessor",
    "GloVeProcessor",
    "FastTextProcessor",
    "VQAAnswerProcessor",
    "GraphVQAAnswerProcessor",
    "MultiHotAnswerFromVocabProcessor",
    "SoftCopyAnswerProcessor",
    "SimpleWordProcessor",
    "SimpleSentenceProcessor",
    "BBoxProcessor",
    "CaptionProcessor",
    "MaskedTokenProcessor",
    "TorchvisionTransforms",
    "FRCNNPreprocess",
    "ArgMaxPredictionProcessor",
]
