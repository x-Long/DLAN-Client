from scan_config import ScanConfig
ENABLE_OPENCV = True
try:
    from utils.ocr_preprocessing import ocr_preprocessing
except Exception as ex:
    print("import opencv error", ex)
    ENABLE_OPENCV = False

try:
    from PIL import Image
except Exception as ex:
    print("import PIL error", ex)



def get_pic_size(pic_path) -> tuple:
    try:
        im = Image.open(pic_path)
        return im.size
    except Exception:
        return 0, 0


def is_img_resolution_enough_to_scan(file_path: str) -> bool:
    """
    analyze picture only its bigger_size >= min_size skip small pictures which always being applications icons or emojis
    """
    small, big, = get_pic_size(file_path)
    if big < small:
        big = small
    return big >= ScanConfig.MinAcceptImgResolution


def is_img_contain_text(img_path, threshold=5) -> bool:
    if ENABLE_OPENCV:
        return ocr_preprocessing(img_path, threshold) == 1
    else:
        return True
