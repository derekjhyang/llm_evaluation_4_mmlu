# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: plot.py
# @time: 2023/10/18 21:50
import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot
# Traces
trace_1 = go.Bar(
            x = ["西南石油", "东方明珠", "海泰发展"],
            y = [4.12, 5.32, 0.60],
            name = "201609"
    )
trace_2 = go.Bar(
            x = ["西南石油", "东方明珠", "海泰发展"],
            y = [3.65, 6.14, 0.58],
            name = "201612"
    )

trace_3 = go.Bar(
            x = ["西南石油", "东方明珠", "海泰发展"],
            y = [2.15, 1.35, 0.19],
            name = "201703"
    )
trace = [trace_1, trace_2, trace_3]
# Layout
layout = go.Layout(
            title = '净资产收益率对比图'
    )
# Figure
figure = go.Figure(data = trace, layout = layout)
# Plot
pyplt(figure, filename='2.png')