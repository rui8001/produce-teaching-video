# 来源台账：为什么不是每个月都有日食

**核对日期：** 2026-08-28

**范围：** 只记录本示例实际使用的事实和迁移结论。NASA 页面中的图片、视频和文字没有被复制到仓库；仓库画面为独立绘制。

| ID | 事实主张 | 权威来源 | 证据类别 | 本示例允许的教学推论 | 状态 |
| --- | --- | --- | --- | --- | --- |
| C1 | 日食的几何条件包含月球位于太阳和地球之间，月球的影子落到地球上。 | [NASA Science：Why Do Eclipses Happen?](https://science.nasa.gov/eclipses/geometry/) | 机构科普说明 | 新月是日食的必要条件，但不是充分条件。 | `verified` |
| C2 | 月球轨道相对黄道面倾斜约五度；多数新月时月球从太阳视方向的上方或下方经过，影子错过地球。 | [NASA Science：Why Do Eclipses Happen?](https://science.nasa.gov/eclipses/geometry/)、[NASA Science：2017 Eclipse and the Moon's Orbit](https://science.nasa.gov/resource/2017-eclipse-and-the-moons-orbit/) | 机构科普说明与可视化说明 | 俯视投影不足以判断是否发生日食，必须补充侧视关系。 | `verified` |
| C3 | 月球轨道与黄道面相交于两个交点；新月在交点附近时，才可能发生日食。 | [NASA GSFC：Periodicity of Solar Eclipses](https://eclipse.gsfc.nasa.gov/SEsaros/SEperiodicity.html) | NASA GSFC 天文计算说明 | 给初学者的判断规则可简化为“新月 + 接近交点”，同时保留“可能”而不是“一定”。 | `verified` |
| C4 | 月食发生在满月阶段、地球位于太阳与月球之间且月球进入地球阴影时；多数满月会因轨道倾角从地球阴影上方或下方通过。 | [NASA Science：Eclipses and the Moon](https://science.nasa.gov/moon/eclipses/) | 机构科普说明 | 同一交点模型可迁移为“满月 + 接近交点 → 可能发生月食”。 | `verified` |

## 模型与未知项

- 示意图不是观测证据，不用于预测某次日食的日期、类型、可见区域或食分。
- 图中的天体大小、距离、轨道曲率和倾角不按比例；倾角被视觉放大以便比较。
- “交点附近”是入门教学表述。本示例不引入角距离阈值、月球视直径、地月距离、半影和本影等进阶变量。
- 如果后续脚本加入具体日期、发生频率或可见地点，必须新增对应来源，不能从当前台账外推。

## 再分发边界

- 可以按本仓库 MIT 许可复用文字结构、JSON 和自绘 SVG。
- 外部链接只作为事实来源；不得把 NASA 页面中的图片或视频误标为本仓库资产。
- 后续加入任何第三方视觉、字体、配音或音乐前，应单独记录许可和署名要求。
