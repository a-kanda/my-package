import plotly.graph_objects as go


def plot_linegraph(x_series, y_dataframe, y_columns):
    """折れ線グラフを描画

    Args:
        x_series (pandas.core.series.Series): X軸のリスト(pandas)
        y_dataframe (pandas.core.frame.DataFrame): Y軸のデータ(pandas)
        y_columns (list): Y軸のカラム名
    """

    fig = go.Figure()
    for i_y_col in y_columns:
        fig.add_trace(
            go.Scatter(x=x_series, y=y_dataframe[i_y_col], name=i_y_col)
        )

    fig.show()
