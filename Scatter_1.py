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
    a="test"
    # 数据
    data=CreData()
    # 表
    trace=go.Scatter(
        cliponaxis=a,
        connectgaps=a,
        customdata=a,
        customdatasrc=a,
        dx=a,
        dy=a,
        error_x=a,
        error_y=a,
        fill=a,
        fillcolor=a,
        hoverinfo=a,
        hoverinfosrc=a,
        hoverlabel=a,
        hoveron=a,
        hovertext=a,
        hovertextsrc=a,
        ids=a,
        idssrc=a,
        legendgroup=a,
        line=a,
        marker=a,
        mode=a,
        name=a,
        opacity=a,
        r=a,
        rsrc=a,
        selected=a,
        selectedpoints=a,
        showlegend=a,
        stream=a,
        t=a,
        text=a,
        textfont=a,
        textposition=a,
        textpositionsrc=a,
        textsrc=a,
        tsrc=a,
        type=a,
        uid=a,
        unselected=a,
        visible=a,
        x=a,
        x0=a,
        xaxis=a,
        xcalendar=a,
        xsrc=a,
        y=a,
        y0=a,
        yaxis=a,
        ycalendar=a,
        ysrc=a

    )

    # 布局
    layout=go.Layout(
        angularaxis=a,
        annotations=a,
        autosize=a,
        bargap=a,
        bargroupgap=a,
        barmode=a,
        barnorm=a,
        boxgap=a,
        boxgroupgap=a,
        boxmode=a,
        calendar=a,
        colorway=a,
        datarevision=a,
        direction=a,
        dragmode=a,
        font=a,
        geo=a,
        grid=a,
        height=a,
        hiddenlabels=a,
        hiddenlabelssrc=a,
        hidesources=a,
        hoverdistance=a,
        hoverlabel=a,
        hovermode=a,
        images=a,
        legend=a,
        mapbox=a,
        margin=a,
        orientation=a,
        paper_bgcolor=a,
        plot_bgcolor=a,
        polar=a,
        radialaxis=a,
        scene=a,
        selectdirection=a,
        separators=a,
        shapes=a,
        showlegend=a,
        sliders=a,
        spikedistance=a,
        ternary=a,
        title=a,
        titlefont=a,
        updatemenus=a,
        violingap=a,
        violingroupgap=a,
        violinmode=a,
        width=a,
        xaxis=a,
        yaxis=a
    )

    #页面
    fig=go.Figure(fig=[trace],layout=layout)

    plot.plot(data=fig,filename="Scatter.html")






if __name__ == '__main__':
    main()