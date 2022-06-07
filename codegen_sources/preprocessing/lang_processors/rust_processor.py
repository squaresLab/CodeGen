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
from codegen_sources.preprocessing.lang_processors.tree_sitter_processor import (
    TreeSitterLangProcessor,
    NEW_LINE,
)
from codegen_sources.preprocessing.lang_processors.java_processor import (
    JAVA_TOKEN2CHAR,
    JAVA_CHAR2TOKEN,
)

import tokenize
from io import BytesIO
import re

RUST_CHAR2TOKEN=JAVA_CHAR2TOKEN.copy()
RUST_TOKEN2CHAR=JAVA_TOKEN2CHAR.copy()

ast_nodes_type_string = [
    # Comments
    "line_comment",
    "block_comment",
    "inner_line_doc",
    "inner_block_doc",
    "outer_line_doc",
    "outer_block_doc",
    # String literals
    "byte_literal",
    "byte_string_literal",
    "raw_byte_string_literal",
    "string_literal",
    "raw_string_literal"
    "char_literal",
]

class RustProcessor(TreeSitterLangProcessor):
    def __init__(self, root_folder=None):
        super().__init__(
            language = "rust",
            ast_nodes_type_string=ast_nodes_type_string,
            stokens_to_chars=RUST_TOKEN2CHAR,
            chars_to_stokens=RUST_CHAR2TOKEN,
            root_folder=root_folder,
        )


    # def tokenize_code(self, code, keep_comments=False, process_strings=True):
    #     raise NotImplementedError

    def detokenize_code(self, code):
        raise NotImplementedError

    def extract_functions(self, code):
        raise NotImplementedError

    def get_function_name(self, function):
        raise NotImplementedError

    def extract_arguments(self, function):
        raise NotImplementedError
