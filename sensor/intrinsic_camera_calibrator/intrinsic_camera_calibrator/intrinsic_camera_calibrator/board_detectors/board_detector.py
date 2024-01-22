#!/usr/bin/env python3

# Copyright 2022 Tier IV, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABC
from abc import abstractmethod
import threading
from typing import Dict
from typing import Optional
from typing import Tuple

from PySide2.QtCore import QObject
from PySide2.QtCore import Signal
from intrinsic_camera_calibrator.board_parameters.board_parameters import BoardParameters
from intrinsic_camera_calibrator.parameter import ParameterizedClass


class BoardDetector(ParameterizedClass, QObject, ABC):
    """Base class of board detectors."""

    detection_results_signal = Signal(object, object)

    def __init__(
        self, lock: threading.RLock, board_parameters: BoardParameters, cfg: Optional[Dict] = {}
    ):
        ParameterizedClass.__init__(self, lock)
        QObject.__init__(self, None)
        self.board_parameters = board_parameters

        self.set_parameters(**cfg)

    @abstractmethod
    def detect(self, img):
        pass

    @abstractmethod
    def single_shot_calibration_error(self, object_points, image_points) -> Tuple[float, float]:
        pass
