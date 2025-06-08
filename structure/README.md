# 网站源码结构

- `_bibliography`: 论文信息
- `_config.yml`: 网站配置 (参考 al-folio)
- `_data`: yaml 数据
- `_includes`: 不同页面的 liquid 模板
- `_layouts`: 不同页面的 liquid 模板
- `_members`: 成员信息
- `_news`: 新闻信息
- `_pages`: 不同页面的 markdown
- `_plugins`: ruby 插件
- `_posts`: 著作实验
- `_projects`: 论文开源项目信息
- `_sass`: 样式文件
- `_scripts`: js 脚本
- `assets`: 网站中各类 css,js,image 资源
- `bin`: 部署脚本, 主要给 Dockerfile 用
- `docker-compose.yml`
- `Dockerfile`
- `Gemfile`
- `Gemfile.lock`
- `LICENSE`
- `node_modules`
- `package-lock.json`
- `package.json`
- `purgecss.config.js`
- `requirements.txt`
- `robots.txt`

部署命令:

```bsah
$ bundle install
$ bundle exec jekyll serve --host 0.0.0.0
```
