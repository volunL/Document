# coding=UTF-8
import plotly.offline as plot
import plotly.graph_objs as go
import numpy as np

def CreData():
    #构建Sin函数 数组
    x = np.arange(-np.pi,np.pi,0.01)
    y = np.sin(x)
    dataD=dict(x=x,y=y)
    return dataD

def main():
    data=CreData()
    #数据图
    trace=go.Scatter(
        x=data['x'],
        y=data['y'],
        mode='lines',
        line=go.Line(
            width=5,
            color='#AA2233'
        )
    )
    #布局
    layout=go.Layout(
        showlegend=True,
        plot_bgcolor='#A9A9A9'
    )
    #窗口对象
    fig = go.Figure(data=[trace],
                    layout=layout
                    )
    plot.plot(fig,filename="start.html")

if __name__ == '__main__':
    main()