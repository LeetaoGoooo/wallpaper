import os

real_path = os.path.realpath(__file__)

macos_wallpaper_path = os.path.join(os.path.dirname(real_path), 'macos-wallpaper')

def get_wallpaper(screen='main'):
    result_str = os.popen(f'{macos_wallpaper_path} get --screen {screen}').read().strip()
    if screen == 'all':
        return result_str.split("\n")
    return result_str


def set_wallpaper(file_path, screen = 'all', scale='auto'):
    if type(file_path) != str:
        raise TypeError("file path was expected a string")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'wallpaper file was not found in {file_path}')
    return os.popen(f"{macos_wallpaper_path} set '{file_path}' --screen {screen} --scale {scale}")
