# wallpaper

> Get or set the desktop wallpaper

![license-apache2](https://img.shields.io/badge/license-Apache%202-blue) ![python3+](https://img.shields.io/badge/license-python3%2B-brightgreen)

Works on macOS 10.12+ and Windows 10+, inspired by [wallpaper node](https://github.com/sindresorhus/wallpaper)

## Install

only python3 is supported

```
pip install py-wallpaper
```

## Usage

```python
from wallpaper import get_wallpaper, set_wallpaper

# get current wallpaper's path
print(get_wallpaper())
# /Users/leetao/Workspace/py/wallpaper/tests/bg.jpg # your wallpaper path

# set your photo
set_wallpaper("your photo's path")
```

## API

### get_wallpaper(**options)

```
Returns the path of the current desktop wallpaper.

param::options->dict

        screen *(macOS only)* -> str

            values: `'all'`, `'main'`

            default: `'main'`
```

The screen to get the wallpaper from. If you set `'all'` then `.get_wallpaper` will return a list.

### set_wallpaper(image_path, **options)


```
Returns a object.

param::image_path -> str

    The path to the image to set as the desktop wallpaper.


param::options -> dict

    screen *(macOS only)* ->  str

    values: `'all'`, `'main'`, or the index of a screen from `.screens()`

    default: `'all'`


The screen to set the wallpaper on.


param::scale *(macOS only)* -> str

    values: `'auto' | 'fill' | 'fit' | 'stretch' | 'center'`

    default: `'auto'`

Scaling method.
```

## TODO

wallpaper on Linux