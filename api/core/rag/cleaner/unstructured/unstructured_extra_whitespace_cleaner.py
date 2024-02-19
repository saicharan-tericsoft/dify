"""Abstract interface for document clean implementations."""
from typing import List, Iterator, Optional, Dict
from app.models.document import Document
from app.services.cleaner.cleaner_base import BaseCleaner
from app.services.extractor.extractor_base import BaseExtractor
from openpyxl.reader.excel import load_workbook

from app.services.extractor.helpers import detect_file_encodings


class UnstructuredNonAsciiCharsCleaner(BaseCleaner):

    def clean(self, content) -> str:
        """clean document content."""
        from unstructured.cleaners.core import clean_extra_whitespace

        # Returns "ITEM 1A: RISK FACTORS"
        return clean_extra_whitespace(content)
