# -*-encoding:utf-8-*-
from scan_config import ScanConfig

class FileType:
    Unknown = 0
    OfficeType = 1
    PdfType = 2
    ImageType = 3
    CadType = 4
    TextType = 5


def get_file_type(filename: str) -> int:
    dot_offset = filename.rfind('.')
    if dot_offset == -1:
        return FileType.Unknown
    suffix = filename[dot_offset:]
    lower_suffix = suffix.lower()
    if lower_suffix == ".pdf":
        return FileType.PdfType
    elif lower_suffix in ScanConfig.OfficeSuffixList:
        return FileType.OfficeType
    elif lower_suffix in ScanConfig.ImageSuffixList:
        return FileType.ImageType
    elif lower_suffix == ".dwg":
        return FileType.CadType
    elif lower_suffix in ScanConfig.TextFileSuffixList:
        return FileType.TextType
    else:
        return FileType.Unknown


class UnsupportedFileType(ValueError):
    pass
