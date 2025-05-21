#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import sys

# 生成Markdown内容
repo_projects_content = f"""---
layout: page
title: {tool_name}
description: {paper_title}
img: {img_link}
pub_year: {pub_year}
importance: 1
category: Publications
related_publications: true
redirect: {redirect_link}
---

{abstract}
"""


def generate_repo_projects(json_file_path):
    # 读取JSON文件
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # 提取所需信息
    tool_name = data.get("工具名", "")
    paper_title = data.get("论文名", "")
    abstract = data.get("摘要", "")
    img_link = data.get("配图", "https://octodex.github.com/images/red-polo.png")
    pub_year = data.get("会议年份", "")
    redirect_link = data.get("GitHub链接", "javascript:void(0)")

    # 生成Markdown文件名
    markdown_file_name = f"{tool_name.lower().replace(':', '').replace(' ', '-')}.md"

    # 写入Markdown文件
    with open(
        os.path.join(os.path.dirname(json_file_path), markdown_file_name),
        "w",
        encoding="utf-8",
    ) as file:
        file.write(md_content)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请指定JSON文件路径")
        sys.exit(1)
    generate_repo_projects(sys.argv[1])
