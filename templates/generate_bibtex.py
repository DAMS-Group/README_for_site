#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import sys


def generate_bibtex_from_json(json_file_path):
    # 读取JSON文件
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # 提取所需信息
    tool_name = data.get("工具名", "")
    paper_title = data.get("论文名", "")
    authors = " and ".join(data.get("论文作者", []))
    first_author_first_name = authors.split(" and ")[0].split(",")[1].strip()
    abstract = data.get("论文摘要", "")
    year = data.get("会议年份", "")
    conference_full_name = data.get("会议英文全称", "")
    preview_image = data.get("文章架构图", "")
    tags = data.get("论文标签", "")
    ccf_level = data.get("CCF等级", "")

    # 生成BibTeX条目
    bibtex_entry = f"""@article{{{first_author_first_name.lower()}{year}{tool_name.replace(' ', '').lower()},
  title={{ {paper_title} }},
  author={{ {authors} }},
  abstract={{ {abstract} }},
  year={{ {year} }},
  note={{ {conference_full_name} }},
  bibtex_show={{ true }},
  preview={{ {preview_image} }},
  type={{ inproceedings }},
  tags={{ {tags} }},
  ccf={{ {ccf_level} }}
}}
"""

    # 输出BibTeX条目
    print(bibtex_entry)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"请指定JSON文件路径: python3 {sys.argv[0]} [JSON_FILE]")
        sys.exit(1)
    generate_bibtex_from_json(sys.argv[1])
