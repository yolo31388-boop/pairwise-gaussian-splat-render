# pairwise-gaussian-splat-render

## 领域

游戏、图形与多媒体

## 主题

高斯泼溅渲染

## 说明

逐点排序、协方差重算与线性混合。

初始状态下 `render/gaussian_splat_render.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
