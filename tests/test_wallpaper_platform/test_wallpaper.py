import pytest
from wallpaper_platform import get_wallpaper, set_wallpaper
import platform
import os

real_path = os.path.realpath(__file__)
wallpaper_path = os.path.join(os.path.dirname(real_path), 'bg.jpg')


def test_set_wallpaper():
    resulut_list = set_wallpaper(wallpaper_path)
    assert type(resulut_list) == list

    with pytest.raises(FileNotFoundError):
        set_wallpaper('')
    
    with pytest.raises(TypeError):
        set_wallpaper(0)
    

def test_get_wallpaper():
    result_str = get_wallpaper()
    assert len(result_str) != 0
    assert result_str == wallpaper_path
    
    if platform.system() == 'Darwin':
        result_list = get_wallpaper('all')
        assert type(result_list) == list
