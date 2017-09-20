from browser import document as doc, alert
import pyecharts
import editor

doc['run'].bind('click', editor.run)
editor.run()
