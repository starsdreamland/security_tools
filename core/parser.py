def build_sqlmap_command(url, options):
    """
    根据用户选项，自动构建 sqlmap 命令
    """

    cmd = [
        "python",
        "tools/sqlmap/sqlmap.py",
        "-u",
        url,
        "--batch"
    ]

    # =========================
    # 扫描模式
    # =========================

    mode = options.get("mode", "fast")

    if mode == "fast":
        cmd += ["--level=1", "--risk=1"]

    elif mode == "normal":
        cmd += ["--level=3", "--risk=2"]

    elif mode == "deep":
        cmd += ["--level=5", "--risk=3"]

    # =========================
    # 随机UA
    # =========================

    if options.get("random_agent", True):
        cmd.append("--random-agent")

    # =========================
    # WAF绕过
    # =========================

    if options.get("tamper"):
        cmd += ["--tamper=space2comment"]

    # =========================
    # POST请求
    # =========================

    if options.get("method") == "POST":

        data = options.get("data")

        if data:
            cmd += ["--data", data]

    # =========================
    # Cookie
    # =========================

    cookie = options.get("cookie")

    if cookie:
        cmd += ["--cookie", cookie]

    # =========================
    # 指定参数
    # =========================

    parameter = options.get("parameter")

    if parameter:
        cmd += ["-p", parameter]

    # =========================
    # 线程
    # =========================

    threads = options.get("threads")

    if threads:
        cmd += ["--threads", str(threads)]

        # =========================
    # Header
    # =========================

    headers = options.get("headers")

    if headers:
        cmd += ["--headers", headers]

    # =========================
    # Proxy
    # =========================

    proxy = options.get("proxy")

    if proxy:
        cmd += ["--proxy", proxy]

    # =========================
    # Technique
    # =========================

    technique = options.get("technique")

    if technique:
        cmd += ["--technique", technique]

    # =========================
    # Crawl
    # =========================

    crawl = options.get("crawl")

    if crawl:
        cmd += ["--crawl", str(crawl)]

    # =========================
    # Forms
    # =========================

    if options.get("forms"):
        cmd.append("--forms")
        
    # =========================
    # 用户自定义参数
    # =========================

    extra = options.get("extra")

    if extra:
        cmd += extra.split()

    return cmd