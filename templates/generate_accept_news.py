#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import sys


def generate_accept_news(json_file_path):
    # 读取JSON文件
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # 提取所需信息
    author = data.get("第一作者", "")
    paper_title = data.get("论文名", "")
    acceptance_date = data.get("录用日期", "")
    conference_year = data.get("会议年份", "")
    conference_abbreviation = data.get("会议英文缩写", "")
    conference_full_name = data.get("会议英文全称", "")
    paper_intro = data.get("一句话论文简介", "")
    other_content = data.get("其他内容", "")
    other_content = "" if other_content == "可不填" else other_content

    # 生成Markdown内容
    accept_news_content = f"""---
layout: post
title: 【论文录用】{conference_abbreviation} {conference_year}
date: {acceptance_date} 14:00:00+0800
inline: false
related_posts: false
giscus_comments: false
category: 学术活动
---

恭喜{author}的论文《{paper_title}》被 {conference_full_name} 录用。{paper_intro}

{other_content}
"""

    # 生成Markdown文件名
    output_filename = (
        f"{acceptance_date}-accept@{conference_abbreviation}{conference_year}.md"
    )

    # 写入Markdown文件
    with open(
        os.path.join(os.path.dirname(json_file_path), output_filename),
        "w",
        encoding="utf-8",
    ) as file:
        file.write(accept_news_content)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"请指定JSON文件路径: python3 {sys.argv[0]} [JSON_FILE]")
        sys.exit(1)
    generate_accept_news(sys.argv[1])
