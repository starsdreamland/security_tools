# Vuln Toolkit
一个基于 GUI 的漏洞测试工具箱，通过图形化界面封装增强 SQLMap 等主流安全工具，为漏洞测试与安全研究提供便捷、直观的操作体验。

相比传统命令行操作，本项目核心聚焦：
- 极致用户体验
- 参数可视化配置
- 实时日志输出展示
- 自动化命令拼接生成
- 多安全工具统一管理

## 项目特点
### SQLMap 图形化控制台
已完整实现以下核心功能：
- SQLMap 全流程图形化操作
- 实时自动生成扫描命令
- 扫描日志实时输出监控
- GET / POST 双请求方式支持
- Cookie 注入测试
- 自定义请求 Headers
- Proxy 代理配置支持
- SQL 注入 Technique 技术自选
- 爬虫 Crawl 深度控制
- 页面 Forms 自动表单扫描
- WAF 绕过参数一键启用
- 多线程并发控制
- 高级自定义参数扩展

## 项目结构
```text
project/
│
├── main.py                 # 项目入口文件
│
├── core/                   # 核心功能模块
│   ├── parser.py           # 参数解析器
│   └── runner.py           # 命令执行器
│
├── tools/                  # 安全工具集成目录
│   ├── sqlmap/             # 原生 SQLMap 工具
│   ├── sqlmap_tool.py      # SQLMap 封装逻辑
│   ├── ssrf_tool.py        # SSRF 工具模块
│   ├── xss_tool.py         # XSS 工具模块
│   └── xxe_tool.py         # XXE 工具模块
│
└── ui/                     # 图形界面模块
    └── app.py              # GUI 主界面
```

## 安装方法
### 1. 克隆项目
```bash
git clone https://github.com/YOUR_USERNAME/vuln_toolkit.git
cd vuln_toolkit
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

## 使用方法
### 启动 GUI
在项目**根目录**执行启动命令：
```bash
python -m ui.app
```
启动后直接进入 SQLMap 图形化操作界面。

## GUI 功能说明
### 1. Target URL
输入待测试的目标地址，示例：
```text
http://testphp.vulnweb.com/listproducts.php?cat=1
```

### 2. 扫描模式
提供三种适配不同场景的扫描模式：
| 模式   | 说明        |
| ---- | --------- |
| 快速扫描 | 基础注入测试，执行速度快 |
| 标准扫描 | 常规安全检测，平衡效率与全面性 |
| 深度扫描 | 全面漏洞检测，覆盖所有测试场景 |

### 3. 请求方式
支持 HTTP 主流请求方式，适配不同业务场景：
- GET：常规 URL 参数测试
- POST：表单/接口数据测试，支持自定义 POST Data

### 4. 功能选项
一键启用高频实用功能：
- Random-Agent：随机请求头，绕过基础防护
- WAF 绕过：自动加载 tamper 脚本绕过防护
- Forms 自动扫描：自动识别页面表单并测试

### 5. 高级参数
精细化配置扫描参数，满足专业测试需求：
| 参数        | 作用           |
| --------- | ------------ |
| Threads   | 设置多线程扫描数量 |
| Parameter | 指定目标测试参数 |
| Cookie    | 自定义身份认证 Cookie |
| Headers   | 自定义 HTTP 请求头 |
| Proxy     | 配置 HTTP/SOCKS 代理 |
| Technique | 指定 SQLMap 注入测试技术 |
| Crawl     | 设置站点爬虫深度 |
| Extra     | 自定义额外 SQLMap 参数 |

### 6. 实时命令生成
GUI 自动根据配置拼接完整 SQLMap 命令，无需手动编写，示例：
```bash
python tools/sqlmap/sqlmap.py -u http://testphp.vulnweb.com/listproducts.php?cat=1 --batch --random-agent
```

### 7. 实时日志输出
扫描过程中实时展示日志：
- 无需等待扫描结束即可查看进度
- 实时监控测试细节，便于问题排查
- 清晰展示扫描执行状态

## 已支持的 SQLMap 功能
| 功能         | 状态 |
| ---------- | ---- |
| GET 扫描     | ✅   |
| POST 扫描    | ✅   |
| Cookie 注入  | ✅   |
| Header 自定义 | ✅   |
| Proxy 支持   | ✅   |
| Crawl 爬虫   | ✅   |
| Forms 扫描   | ✅   |
| Technique 自选 | ✅  |
| Tamper 绕过  | ✅   |
| 多线程控制    | ✅   |
| 实时日志输出  | ✅   |

## 项目定位
本项目**不重复造轮子**，不重新实现 SQLMap 核心逻辑，而是：
> 通过图形化界面 + 自动化逻辑，
> 降低安全工具使用门槛，让用户高效、便捷地使用强大的安全工具。

**适用人群/场景**：
- 网络安全初学者学习练习
- CTF 竞赛快速漏洞测试
- 本地靶场实战演练
- 授权渗透测试练习
- 安全研究与实验

## 未来计划
### 工具集成（持续拓展）
- XSStrike（XSS 漏洞检测）
- SSRFMap（SSRF 漏洞检测）
- XXE Injector（XXE 漏洞利用）
- 子域名扫描工具
- 网站目录扫描工具
- WAF 检测与识别工具

### 功能升级
- 多工具独立页签管理
- 扫描任务批量调度
- 日志语法高亮与筛选
- 扫描报告自动导出（PDF/HTML）
- 插件扩展系统
- 历史扫描记录保存
- 深色/浅色主题切换

## 注意事项
⚠️ **本项目仅用于合法用途**，仅限以下场景使用：
- 安全技术学习与研究
- 获得**合法授权**的渗透测试
- 本地实验环境/私有靶场测试
- CTF 竞赛练习

**严禁用于**未授权的网络攻击、非法入侵等违法活动，使用者需自行承担所有相关法律责任。

## 致谢
- [SQLMap](https://sqlmap.org/)：业界领先的 SQL 注入检测工具
- Python：项目开发基础语言
- Tkinter：Python 原生 GUI 框架

## License
MIT License（开源免费，可自由学习、修改和使用）