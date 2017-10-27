# coding=utf-8

import uuid
import json
import datetime
from browser import window, load, doc

import pyecharts.utils as utils
import pyecharts.template as template
import pyecharts.constants as constants


class Base(object):
    """
    `Base`类是所有图形类的基类，提供部分初始化参数和基本的方法
    """
    def __init__(self,
                 width=800,
                 height=400,
                 page_title=constants.PAGE_TITLE,
                 jshost=None):
        """

        :param width:
            画布宽度，默认为 800（px）
        :param height:
            画布高度，默认为 400（px）
        :param page_title:
            指定生成的 html 文件中 <title> 标签的值。默认为'Echarts'
        :param jshost:
            自定义每个实例的 JavaScript host
        """
        self._option = {}
        self._js_dependencies = set()
        self._chart_id = uuid.uuid4().hex
        self.width, self.height = width, height
        self._page_title = page_title
        self._jshost = jshost if jshost else constants.CONFIGURATION['HOST']
        self._js_dependencies = {'echarts'}

    @property
    def chart_id(self):
        """ 设置 chart_id 属性为可读
        """
        return self._chart_id

    @property
    def options(self):
        """ 设置 options 属性为可读
        """
        return self._option

    @property
    def js_dependencies(self):
        """ 依赖的 js 文件列表
        """
        return self._js_dependencies

    def show_config(self):
        """ 打印输出图形所有配置项
        """
        print(json_dumps(self._option, indent=4))

    def get_js_dependencies(self):
        """ 声明所有的 js 文件路径
        """
        return template.produce_html_script_list(self._js_dependencies)

    def render(self, _=None):
        for js_url in self.get_js_dependencies():
            load(constants.DEFAULT_HOST + '/' + js_url + ".js")

        while doc['me'].hasChildNodes():
            doc['me'].removeChild(doc['me'].lastChild)
        self.draw()

    def draw(self):
        div = doc.createElement('div')
        div.style.width = self._width
        div.style.height = self._height
        doc['me'].appendChild(div)
        myechart = window.echarts.init(div)
        myechart.setOption(self.options)


class UnknownTypeEncoder(json.JSONEncoder):
    """
    `UnknownTypeEncoder`类用于处理数据的编码，使其能够被正常的序列化
    """
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        else:
            try:
                return obj.astype(float).tolist()
            except:
                try:
                    return obj.astype(str).tolist()
                except:
                    return json.JSONEncoder.default(self, obj)


def json_dumps(data, indent=0):
    """ json 序列化编码处理

    :param data: 字典数据
    :param indent: 缩进量
    :return:
    """
    return json.dumps(data, indent=indent,
                      cls=UnknownTypeEncoder)
