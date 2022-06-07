# Copyright (c) 2022-present, Jeremy Lacomis
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
from codegen_sources.preprocessing.lang_processors.tokenization_utils import (
    process_string,
)
from codegen_sources.preprocessing.lang_processors.lang_processor import LangProcessor

import tokenize
from io import BytesIO
import re


class FortranProcessor(LangProcessor):
    def __init__(self, root_folder=None):
        self.language = "fortran"

    def tokenize_code(self, code, keep_comments=False, process_strings=True):
        raise NotImplementedError

    def detokenize_code(self, code):
        raise NotImplementedError

    def extract_functions(self, code):
        raise NotImplementedError

    def get_function_name(self, function):
        raise NotImplementedError

    def extract_arguments(self, function):
        raise NotImplementedError
