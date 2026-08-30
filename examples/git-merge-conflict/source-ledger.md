# 来源台账：安全处理一个 Git 合并冲突

**核对日期：** 2026-08-30

**范围：** 只记录本示例实际使用的 Git 行为和演示证据。官方页面的文字和图片没有复制到仓库；命令、合成文本和 SVG 均为本示例自行编写。

| ID | 事实或证据 | 来源 | 证据类别 | 本示例允许的教学推论 | 状态 |
| --- | --- | --- | --- | --- | --- |
| C1 | 两个分支以不同方式修改同一文件的同一区域时，Git 可能无法自动合并；合并会暂停，等待用户解决。 | [Pro Git：Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging.html) | Git 官方在线书籍 | 冲突不是仓库损坏，而是 Git 无法替人判断两份内容的最终含义。 | `verified` |
| C2 | 未解决的路径可由 `git status` 查看；文本冲突会被标准标记包围，分隔当前内容和待合入内容。 | [Pro Git：Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging.html)、[git-merge-file](https://git-scm.com/docs/git-merge-file) | 官方说明与命令文档 | 冻结并逐段阅读标记，比直接点击 ours/theirs 更能暴露需要做的决策。 | `verified` |
| C3 | 解决者编辑文件得到最终内容，用 `git add` 标记冲突已解决，再以 `git commit` 或 `git merge --continue` 完成合并。 | [git-merge：How to resolve conflicts](https://git-scm.com/docs/git-merge#_how_to_resolve_conflicts) | Git 官方命令文档 | 教学步骤必须包含最终内容检查，不能把删除标记本身当成解决完成。 | `verified` |
| C4 | `git merge --abort` 可尝试回到合并前状态；若开始合并时已有未提交修改，重建原状态可能失败。 | [git-merge：--abort](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---abort) | Git 官方命令文档 | 把 abort 作为明确停止条件，同时要求合并前保持干净工作区。 | `verified` |
| D1 | 仓库内脚本能在临时目录复现 `UU plan.txt`、标准冲突标记、暂存解决结果和双父合并提交。 | [确定性演示](./demonstration.md)、[演示脚本](./demo.sh) | 本地可重复观察 | 视频中的终端状态可以来自真实演示，而不是重绘的虚构界面。 | `verified` |

## 程序边界与未知项

- 本示例不声称所有冲突都来自“同一行”；复杂文本、重命名、删除、二进制文件和自定义驱动可能产生不同状态。
- `HEAD`、分支标签、状态文案和编辑器行为会受版本与配置影响，教学画面应以当前演示输出为准。
- 自动脚本中的最终文本代表一个明确给出的合成需求；现实冲突必须向代码作者、需求或测试确认意图。
- 如果后续加入图形化工具、托管平台按钮或 IDE 操作，必须重新核对相应官方资料和界面版本。

## 再分发边界

- 可以按本仓库 MIT 许可复用合成文本、脚本、JSON、Markdown 和自绘 SVG。
- 外部链接仅作为事实来源；不得把 Pro Git 页面中的插图或大段文字复制后误标为本仓库资产。
- 后续加入第三方字体、截图、配音或音乐前，应单独记录许可和署名要求。
