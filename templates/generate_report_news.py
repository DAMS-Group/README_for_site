#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import sys


def generate_report_news(json_file_path):
    # 读取JSON文件
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # 提取所需信息
    author = data.get("作者", "")
    paper_title = data.get("论文名", "")
    conference_date = data.get("参会日期", "")
    month, day = conference_date.split("-")[1:]
    month = month.lstrip("0")
    day = day.lstrip("0")
    chinese_conference_date = f"{conference_date.split('-')[0]}年{month}月{day}日"
    conference_location = data.get("参会地点", "")
    conference_year = data.get("会议年份", "")
    conference_abbreviation = data.get("会议英文缩写", "")
    conference_full_name_en = data.get("会议英文全称", "")
    conference_full_name_cn = data.get("会议中文全称", "")
    paper_intro = data.get("论文介绍", "")
    other_content = data.get("其他内容", "")
    other_content = "" if other_content == "可不填" else other_content

    # 生成Markdown内容
    report_news_content = f"""---
layout: post
title: 【学术报告】{author}的报告 @ {conference_abbreviation}{conference_year}
date: {conference_date} 14:00:00+0800
inline: false
related_posts: false
giscus_comments: false
category: 学术活动
---

{author}于{chinese_conference_date}在{conference_location}参加{conference_full_name_cn}（{conference_full_name_en}, {conference_abbreviation}{conference_year}），在会议上汇报了题为《{paper_title}》的学术研究成果。

{paper_intro}。

{other_content}
"""

    # 生成Markdown文件名
    output_filename = (
        f"{conference_date}-{author}@{conference_abbreviation}{conference_year}.md"
    )

    # 写入Markdown文件
    with open(
        os.path.join(os.path.dirname(json_file_path), output_filename),
        "w",
        encoding="utf-8",
    ) as file:
        file.write(report_news_content)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"请指定JSON文件路径: python3 {sys.argv[0]} [JSON_FILE]")
        sys.exit(1)
    generate_report_news(sys.argv[1])
