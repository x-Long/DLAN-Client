from app_config import AppMetaInfo


class ScanConfig:
    IsStatisticTime = False
    EnableScanImage = AppMetaInfo.enable_scan_img()
    EnablePngAndBmp = AppMetaInfo.enable_scan_img()
    EnableScanText = False
    EnableScanCompressedFile = True
    EnableDwg = AppMetaInfo.is_enable_scan_dwg()

    MinAcceptImgResolution = 500

    CadSuffix = ".dwg"
    OfficeSuffixList = [".doc", ".docx", ".wps",
                              ".xls", ".xlsx",
                              ".ppt", ".pptx",
                        ".pdf",
                       ]

    DefaultScanSuffix = OfficeSuffixList[:]
    if EnableDwg:
        DefaultScanSuffix.append(CadSuffix)

    ImageSuffixList = [
            ".tif", ".jpg", ".jpeg"
            ]
    if EnablePngAndBmp:
        # Boss Liu do not want scan below img files
        ImageSuffixList.extend([".png", ".bmp"])

    # mark it to False if do not allow client scan pictures
    if EnableScanImage:
        DefaultScanSuffix.extend(ImageSuffixList)

    TextFileSuffixList = [
        ".txt",
        ".inf",
        ".log",
        ".ini"
    ]
    if EnableScanText:
        DefaultScanSuffix.extend(TextFileSuffixList)

    CompressedSuffix = [".zip", ".rar"]

    BLACK_LIST = [
        'MicrosoftEdgeBackups',
        'AppData',
        'Local Settings',
        '3D Objects',
        'AndroidStudioProjects',
        'Application Data',
        'Cookies',
        'Links',
        'IntelGraphicsProfiles',
        '「开始」菜单',
        'Roaming',
    ]
    EnableWhileList = True
    WHITE_LIST = [
        'Downloads',
        "下载",

        'Documents',
        "文档",

        'Pictures',
        "照片",

        'Desktop',
        "桌面",

        # third part applications data dir
        'Dropbox',
    ]


if __name__ == '__main__':
    print(ScanConfig.DefaultScanSuffix)
    # print(ScanConfig.OfficeSuffixList)
