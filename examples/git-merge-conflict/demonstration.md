# 确定性演示：一个文本合并冲突

这个演示只在 `mktemp` 创建的临时目录中运行，并在退出时清理目录。它不会读取、修改或合并调用者当前仓库。

脚本在自己的 Bash 子进程中清除继承的 `GIT_*` 环境变量，禁用系统与用户 Git 配置，使用空模板，并在临时仓库中禁用外部 hooks、attributes 和 ignore 文件。这样，调用者的 `GIT_DIR`、索引位置、签名要求或模板钩子不会将合成操作导向其他仓库，也不会改动调用者的配置。请使用下面的 `bash` 命令执行，不要用 `source` 加载脚本。

## 合成情形

初始文件 `plan.txt` 的截止时间是“周五 17:00”。随后：

- `main` 分支把时间提前到“周五 15:00”；
- `feature` 分支把日期提前到“周四 17:00”；
- 合成需求明确要求同时保留“周四”和“15:00”，所以最终文本是“周四 15:00”。

Git 能检测两边对同一区域的修改，但“最终会议应该在什么时候”不是版本控制系统可以推断的事实，因此脚本先验证冲突，再显式写入合成需求的答案。

## 运行

需要 Bash、Git 2.32 或更新版本，以及常见 POSIX 命令（如 `mktemp`、`grep`、`sed`）。脚本会拒绝旧版本，以确保支持用于隔离配置的 [`GIT_CONFIG_GLOBAL`](https://git-scm.com/docs/git-config/2.32.0#Documentation/git-config.txt-GITCONFIGGLOBAL)。

```bash
bash examples/git-merge-conflict/demo.sh
```

成功输出：

```text
merge_result=conflict
unmerged_status=UU plan.txt
conflict_markers=present
resolved_line=截止时间：周四 15:00
merge_commit_parents=2
```

## 可验证不变量

1. `git merge feature` 必须以冲突停止，而不是静默成功。
2. `git status --short` 必须把文件显示为 `UU plan.txt`。
3. 文件必须同时出现 `<<<<<<< HEAD`、`=======` 和 `>>>>>>> feature`。
4. 解决后的文件必须先进入暂存区，才能继续合并。
5. 最终提交必须有两个父提交，证明流程确实完成了合并，而不是另建普通提交。

命令输出可能随 Git 版本、语言和配置变化；本仓库自动检查使用这里列出的可观察不变量，而不是依赖完整提示文案。

隔离边界的回归测试使用临时合成仓库，对比执行前后调用者文件、Git 配置与索引的字节内容，并检查签名配置、环境注入和模板钩子不会影响演示：

```bash
python3 -m unittest discover -s tests -v
```

这些测试不访问真实生产仓库，也不验证音频或最终视频。
