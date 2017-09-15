#!/usr/bin/env python
# coding=utf-8

import pyecharts.constants as constants
from pyecharts.template import (
    produce_html_script_list)


class Page(object):
    """
    A composite object to present multiple charts vertically in a single page
    """
    def __init__(self, jshost=None, page_title=constants.PAGE_TITLE):
        """

        :param jshost:
            custom javascript host for the particular chart only
        """
        self.__charts = []
        self._page_title = page_title
        self._jshost = jshost if jshost else constants.CONFIGURATION['HOST']

    def add(self, achart_or_charts):
        """
        Append chart(s) to the rendering page

        :param achart_or_charts:
        :return:
        """
        if isinstance(achart_or_charts, list):
            self.__charts.extend(achart_or_charts)
        else:
            self.__charts.append(achart_or_charts)

    def render(self, path="render.html"):
        """
        Produce rendered charts in a html file

        :param path:
        :return:
        """
        raise Exception("Not Implemented")

    def get_js_dependencies(self):
        """
        Declare its javascript dependencies for embedding purpose
        """
        unordered_js_dependencies = self._merge_dependencies()
        return produce_html_script_list(unordered_js_dependencies)

    def _merge_dependencies(self):
        dependencies = set()
        for chart in self.__charts:
            dependencies = dependencies.union(chart._js_dependencies)
        # make sure echarts is the item in the list
        # require(['echarts'....], function(ec) {..}) need it to be first
        # but dependencies is a set so has no sequence
        if len(dependencies) > 1:
            dependencies.remove('echarts')
            dependencies = ['echarts'] + list(dependencies)
        return dependencies
