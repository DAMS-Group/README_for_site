# 网站更新模板

## 被录用论文时

- `ACCEPT.json`: 论文录用通知
    - 执行 `python3 generate_accept_news.py ACCEPT.json`, 将生成的文件放到网站的 `_news` 目录下
- `BIB.json`: 论文引用信息, 论文架构图
    - 执行 `python3 generate_bib_news.py BIB.json`, 将输出的内容添加到放到网站的 `_bibliography/papers.bib` 文件中

## 参加会议汇报论文时

- `PAPER.json`: 参会情况介绍, 会议照片
    - 执行 `python3 generate_paper_news.py PAPER.json`, 将生成的文件添加到放到网站的 `_news` 目录下
