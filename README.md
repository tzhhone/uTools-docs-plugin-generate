<h2 align="center">uTools 文档插件生成器 (uTools-docs-plugin-generate)</h2>
<p align="center">
  <a href="https://blog.tzhhone.cn">
    <img src="https://img.shields.io/badge/author-tzhhone-blue" alt="tzhhone">
  </a>
  <img src="https://img.shields.io/badge/python3.7%2B-brightgreen" alt="python">
  <a href="https://github.com/tzhhone/uTools-docs-plugin-generate/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/tzhhone/uTools-docs-plugin-generate" alt="license">
  </a>
</p>

### 项目简介
本项目是一个用于生成 uTools 文档插件的工具，可以通过简单的配置文件，快速生成一个 uTools 看云文档插件。

### 开发环境
- python 3.7

### 目前支持
- [看云](https://www.kancloud.cn)

### 使用方法
1. 运行命令 `pip install -r requirements.txt` 安装pip包
2. 修改 main.py 中的 url 和 dir（其中url为看云文档地址，dir为目录名）
3. 根目录下的 thinkphp6 是使用本项目生成的 [ThinkPHP6.0完全开发手册](https://www.kancloud.cn/manual/thinkphp6_0/1037479) uTools 插件
4. 在 uTools 中搜索 thinkphp6，即可看到效果

