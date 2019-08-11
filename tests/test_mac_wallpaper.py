import pytest
from wallpaper import get_wallpaper, set_wallpaper
import platform
import os

real_path = os.path.realpath(__file__)
wallpaper_path = os.path.join(os.path.dirname(real_path), 'bg.jpg')

@pytest.mark.mac
def test_get_wallpaper():
    result_str = get_wallpaper()
    assert type(result_str) == str
    result_list = get_wallpaper('all')
    assert type(result_list) == list

@pytest.mark.mac
def test_set_wallpaper():
    resulut_str = set_wallpaper(wallpaper_path)

    with pytest.raises(FileNotFoundError):
        set_wallpaper('')
    
    with pytest.raises(TypeError):
        set_wallpaper(0)

