# wallpaper

> Get or set the desktop wallpaper

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

### .get_wallpaper(options?)

Returns the path of the current desktop wallpaper.

#### options

Type: `object`

##### screen *(macOS only)*

Type: `string | number`<br>
Values: `'all'`, `'main'`, or the index of a screen from `.screens()`<br>
Default: `'main'`

The screen to get the wallpaper from.

If you set `'all'` then `.get_wallpaper` will return a list.

### .set_wallpaper(imagePath, options?)

Returns a object.

#### imagePath

Type: `string`

The path to the image to set as the desktop wallpaper.

#### options

Type: `object`

##### screen *(macOS only)*

Type: `string | number`<br>
Values: `'all'`, `'main'`, or the index of a screen from `.screens()`
Default: `'all'`

The screen to set the wallpaper on.

##### scale *(macOS only)*

Type: `string`<br>
Values: `'auto' | 'fill' | 'fit' | 'stretch' | 'center'`<br>
Default: `'auto'`

Scaling method.

## TODO

wallpaper on Linux