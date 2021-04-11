# -*- coding: utf-8 -*-
"""example-plot-function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iUd1zhs5_8bo28Y2VqVSmZfCEFp0TnqZ
"""

# Commented out IPython magic to ensure Python compatibility.
# General Purpose
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
import ipyvuetify as v

# Jupyter Specifics
from IPython.display import HTML
from ipywidgets.widgets import interact, IntSlider, FloatSlider, Layout

# %matplotlib inline

style = {'description_width': '150px'}
slider_layout = Layout(width='99%')



def main(initial_salary, savings_ratio, extraordinary_expenses, fixed_costs, days):
    saving_limit = savings_ratio * initial_salary

    def function(capital, time):
        if capital <= saving_limit:
            out_rate = 0
        else:
            out_rate = extraordinary_expenses * (capital - saving_limit)
        return -fixed_costs - out_rate

    time = np.linspace(0, days, days * 10)

    solution = odeint(function, initial_salary, time)

    #Graphic details
    fig, ax = plt.subplots(figsize=(15, 10))

    ax.plot((0, days), (saving_limit, saving_limit), label='Saving Limit')
    ax.plot(time, solution, label='Capital(t)')

    if days <= 60:
        step = 1
        rotation = "horizontal"
    elif days <= 300:
        step = 5
        rotation = "vertical"
    else:
        step = 10
        rotation = "vertical"

    ax.set_xticklabels(np.arange(0, days + 1, step, dtype=np.int), rotation=rotation)
    ax.set_xticks(np.arange(0, days + 1, step))

    ax.set_yticks(np.arange(0, initial_salary * 1.1, initial_salary / 20))

    ax.set_xlim([0, days])
    ax.set_ylim([0, initial_salary * 1.1])
    ax.set_xlabel('Days')
    ax.set_ylabel('Capital $')
    ax.legend(loc='best')
    ax.grid()

    plt.show()

interact(main, initial_salary=IntSlider(min=0, max=25000, step=500, value=15000, description='Initial Salary', style=style, layout=slider_layout),
               savings_ratio=FloatSlider(min=0, max=1, step=0.01, value=0.2, description='Savings Ratio', style=style, layout=slider_layout),
               extraordinary_expenses=FloatSlider(min=0, max=1, step=0.005, description='Extraordinary Expenses', style=style, value=0.3, layout=slider_layout),
               fixed_costs=IntSlider(min=1, max=1000, step=1, value=100, description='Fixed Costs', style=style, layout=slider_layout),
               days=IntSlider(min=1, max=600, step=5, value=30, description='Total Number of Days', style=style, layout=slider_layout)
        );