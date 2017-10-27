# coding=utf-8

from browser import doc, load
import pyecharts.template as template
import pyecharts.constants as constants


class Page(object):
    """
    A composite object to present multiple charts vertically in a single page
    """

    def __init__(self, jshost=None, page_title=constants.PAGE_TITLE):
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
        for js_url in self.get_js_dependencies():
            load(constants.DEFAULT_HOST + '/' + js_url + ".js")
        while doc['me'].hasChildNodes():
            doc['me'].removeChild(doc['me'].lastChild)
        self.draw()

    def draw(self):
        """
        add all charts to dom
        """
        for chart in self.__charts:
            chart.draw()

    def get_js_dependencies(self):
        """
        Declare its javascript dependencies for embedding purpose
        """
        unordered_js_dependencies = self._merge_dependencies()
        return template.produce_html_script_list(unordered_js_dependencies)

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

    @property
    def charts(self):
        return self.__charts

    @property
    def js_dependencies(self):
        return self._merge_dependencies()
