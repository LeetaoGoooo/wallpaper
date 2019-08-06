import platform

if platform.system() == 'Darwin':
    from .mac import get_wallpaper, set_wallpaper
if platform.system() == 'Windows':
    from .win import get_wallpaper, set_wallpaper