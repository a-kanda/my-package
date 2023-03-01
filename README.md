# my-package

## インストール方法
```
pip install git+https://github.com/a-kanda/my-package.git
```

## 使い方
### データ可視化
#### 折れ線グラフの描画
```
import tools

tools.plot_linegraph(pd["timestamp"], pd, ["open", "high", "low", "close"])
```

#### ヒストグラムの描画
```
import tools

tools.plot_histgram(pd, ["open", "high", "low", "close"], 7)
```
