import pytest
from wallpaper_platform import get_wallpaper, set_wallpaper


def test_get_wallpaper():
    result_str = get_wallpaper()
    assert len(result_str) != 0
    result_list = get_wallpaper('all')
    assert type(result_list) == list