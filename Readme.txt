# Vuln Toolkit

一个基于 GUI 的漏洞测试工具箱。

本项目旨在通过图形化界面，对 SQLMap 等安全工具进行封装与增强，帮助用户更加方便、直观地进行漏洞测试与安全研究。

相比传统命令行操作，本项目更加注重：

- 用户体验
- 参数可视化
- 实时日志输出
- 自动化命令拼接
- 多工具统一管理

---

# 项目特点

## SQLMap 图形化控制台

目前已经实现：

- SQLMap 图形化操作
- 实时命令生成
- 实时扫描日志输出
- GET / POST 请求支持
- Cookie 注入
- 自定义 Headers
- Proxy 代理支持
- Technique 技术选择
- Crawl 深度控制
- Forms 自动表单扫描
- WAF 绕过参数
- 多线程控制
- 高级参数扩展

---

# 项目结构

```text
project/
│
├── main.py
│
├── core/
│   ├── parser.py
│   └── runner.py
│
├── tools/
│   ├── sqlmap/
│   ├── sqlmap_tool.py
│   ├── ssrf_tool.py
│   ├── xss_tool.py
│   └── xxe_tool.py
│
└── ui/
    └── app.py
````

---

# 安装方法

## 1. 克隆项目

```bash
git clone https://github.com/YOUR_USERNAME/vuln_toolkit.git
cd vuln_toolkit
```

---

## 2. 安装依赖

```bash
pip install -r requirements.txt
```

---

# 使用方法

## 启动 GUI

在项目根目录执行：

```bash
python -m ui.app
```

启动后将进入 SQLMap 图形化界面。

---

# GUI 功能说明

## 1. Target URL

输入目标地址：

```text
http://testphp.vulnweb.com/listproducts.php?cat=1
```

---

## 2. 扫描模式

支持：

| 模式   | 说明        |
| ---- | --------- |
| 快速扫描 | 基础测试，速度较快 |
| 标准扫描 | 常规安全测试    |
| 深度扫描 | 更全面的漏洞检测  |

---

## 3. 请求方式

支持：

* GET
* POST

选择 POST 后可填写 POST Data。

---

## 4. 功能选项

支持：

* Random-Agent
* WAF 绕过
* Forms 自动扫描

---

## 5. 高级参数

支持：

| 参数        | 作用           |
| --------- | ------------ |
| Threads   | 多线程扫描        |
| Parameter | 指定测试参数       |
| Cookie    | 自定义 Cookie   |
| Headers   | 自定义请求头       |
| Proxy     | 设置代理         |
| Technique | 指定 SQLMap 技术 |
| Crawl     | 爬取深度         |
| Extra     | 额外 SQLMap 参数 |

---

## 6. 实时命令生成

GUI 会自动生成对应 SQLMap 命令。

例如：

```bash
python tools/sqlmap/sqlmap.py -u http://testphp.vulnweb.com/listproducts.php?cat=1 --batch --random-agent
```

无需手动拼接复杂参数。

---

## 7. 实时日志输出

扫描过程中：

* 日志会实时显示
* 无需等待扫描结束
* 更方便观察测试过程

---

# 已支持的 SQLMap 功能

| 功能         | 状态 |
| ---------- | -- |
| GET 扫描     | ✅  |
| POST 扫描    | ✅  |
| Cookie 注入  | ✅  |
| Header 自定义 | ✅  |
| Proxy 支持   | ✅  |
| Crawl      | ✅  |
| Forms      | ✅  |
| Technique  | ✅  |
| Tamper     | ✅  |
| 多线程        | ✅  |
| 实时日志       | ✅  |

---

# 项目目标

本项目并不是重新实现 SQLMap。

而是：

> 通过 GUI 与自动化逻辑，
> 帮助用户更加高效、便捷地使用强大的安全工具。

尤其适合：

* 安全学习
* CTF
* 本地靶场测试
* 渗透测试练习
* 安全研究

---

# 未来计划

计划继续集成：

* XSStrike
* SSRFMap
* XXE Injector
* 子域名扫描
* 目录扫描
* WAF 检测

后续还计划加入：

* 多工具页签
* 扫描任务管理
* 日志高亮
* 扫描报告导出
* 插件系统
* 历史记录

---

# 注意事项

本项目仅供：

* 学习研究
* 合法授权测试
* 本地实验环境
* CTF 练习

请勿用于任何非法用途。

使用者需自行承担相关责任。

---

* SQLMap
* Python
* Tkinter


