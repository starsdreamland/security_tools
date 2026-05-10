from core.runner import Task, run
from core.parser import build_sqlmap_command


def choose_mode():
    print("\n选择扫描模式：")
    print("1. 快速扫描")
    print("2. 标准扫描")
    print("3. 深度扫描")

    choice = input("请选择 (1/2/3): ").strip()

    mode_map = {
        "1": "fast",
        "2": "normal",
        "3": "deep"
    }

    return mode_map.get(choice, "fast")


def yes_or_no(question):
    choice = input(f"{question} (y/n): ").strip().lower()
    return choice == "y"


def main():

    print("=" * 60)
    print("        SQLMap 智能扫描控制台")
    print("=" * 60)

    # =========================
    # URL
    # =========================

    url = input("\nTarget URL: ").strip()

    # =========================
    # 模式
    # =========================

    mode = choose_mode()

    # =========================
    # 高级选项
    # =========================

    print("\n高级功能选项：")

    random_agent = yes_or_no("启用随机 User-Agent")
    tamper = yes_or_no("启用 WAF 绕过")
    use_cookie = yes_or_no("是否使用 Cookie")
    use_post = yes_or_no("是否为 POST 请求")
    specify_param = yes_or_no("是否指定测试参数")

    cookie = None
    data = None
    parameter = None

    if use_cookie:
        cookie = input("请输入 Cookie: ").strip()

    if use_post:
        data = input("请输入 POST 数据: ").strip()

    if specify_param:
        parameter = input("请输入参数名: ").strip()

    # =========================
    # 线程
    # =========================

    threads_input = input("线程数（默认5）: ").strip()

    if threads_input.isdigit():
        threads = int(threads_input)
    else:
        threads = 5

    # =========================
    # 额外参数
    # =========================

    extra = input("额外 sqlmap 参数（可留空）: ").strip()

    # =========================
    # options
    # =========================

    options = {
        "mode": mode,
        "random_agent": random_agent,
        "tamper": tamper,
        "cookie": cookie,
        "method": "POST" if use_post else "GET",
        "data": data,
        "parameter": parameter,
        "threads": threads,
        "extra": extra
    }

    # =========================
    # 实时命令生成
    # =========================

    cmd = build_sqlmap_command(url, options)

    print("\n" + "=" * 60)
    print("实时生成命令：")
    print("=" * 60)

    print(" ".join(cmd))

    print("=" * 60)

    # =========================
    # 用户确认
    # =========================

    confirm = input("\n开始执行扫描？(y/n): ").strip().lower()

    if confirm != "y":
        print("已取消扫描")
        return

    # =========================
    # 创建任务
    # =========================

    task = Task(
        task_id=1,
        task_type="sqlmap",
        target=url,
        options=options
    )

    # =========================
    # 执行
    # =========================

    print("\n[INFO] 开始扫描...\n")

    result = run(task)

    # =========================
    # 输出结果
    # =========================

    print("\n" + "=" * 60)
    print("扫描结果")
    print("=" * 60)

    print(f"类型: {result['type']}")
    print(f"状态: {result['status']}")

    print("\n详细信息：")
    print(result["details"])


if __name__ == "__main__":
    main()