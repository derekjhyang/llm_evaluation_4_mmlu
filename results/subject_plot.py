# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: subject_plot.py.py
# @time: 2023/10/18 22:32
import os
import json

import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot


model_list = ['llama2-7b-hf',
              'Baichuan-7B',
              'Mistral-7B-v0.1',
              'Baichuan2-7B-Base',
              'Baichuan2-13B-Base',
              'llama2-13b-hf',
              'internlm-20b',
              'llama2-70b-hf',
              'Mixtral-8x7B-v0.1']

y_list = []
model_metric_dict = {}
for file in os.listdir('.'):
    if file.endswith("json"):
        model_name = file.split("_")[-1].replace(".json", "")
        if model_name in model_list:
            with open(file, "r") as f:
                content = json.loads(f.read())
                metrics = list(content["subcategories"].values())
                x_list = list(content["subcategories"].keys())
                model_metric_dict[model_name] = metrics

trace = []
for model_name in model_list:
    trace.append(go.Bar(x=x_list,
                        y=model_metric_dict[model_name],
                        name=model_name))

# Layout
layout = go.Layout(title='MMLU Subject Evaluation with LLM')
# Figure
figure = go.Figure(data=trace, layout=layout)
# Plot
pyplt(figure, filename='subject.html')