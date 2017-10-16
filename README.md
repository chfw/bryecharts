# pyecharts.js

pyecharts.js is a [Brython](https://github.com/brython-dev/brython) port of pyecharts to generate echarts directly in modern browsers.

It is a fun project to play with Brython, which let you run pure python code in browsers.

## Installation

```
npm install --save pyecharts
```

## Demo

1. Visit https://chfw.github.io/pyecharts/
1. Paste your [sample codes](https://github.com/chenjiandongx/pyecharts/blob/master/docs/zh-cn/documentation.md) into the editor or write your own code from scratch
1. Press 'Run'


### Offline demo

1. Clone it
1. Run a static http server
1. Open a browser and visit http://localhost:8000

Here are all the commands:

```
$ git clone https://github.com/chfw/pyecharts/
$ cd pyecharts
$ python -m http.server # python 2, please use python -m SimpleHTTPServer
```

Then you can do paste and run.

## Development

You will need python 3 for development and can develop it like any other python packages. Once
you are happy with your changes, here is the command for packaging:

```
make
```

The hard work is to find out the relevant dependency for packaging and list them in bp-requirements.txt. The current practices is trial the demo in your browser and
see which standard module are missing. Place its name in bp-requirements.txt. Repeat it until you get zero import errors.


## Baselines


1. pyecharts v0.2.6
1. Brython 3.3.2

## License

pyecharts.js will be released under the MIT License. See LICENSE for more information.

