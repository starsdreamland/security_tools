import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from core.parser import build_sqlmap_command
from core.runner import Task, run


# =====================================
# 实时更新命令
# =====================================

def update_command():

    url = url_entry.get()

    options = {
        "mode": mode_var.get(),
        "random_agent": random_agent_var.get(),
        "tamper": tamper_var.get(),

        "threads": threads_var.get(),

        "parameter": parameter_entry.get(),

        "cookie": cookie_entry.get(),

        "headers": headers_entry.get(),

        "proxy": proxy_entry.get(),

        "technique": technique_var.get(),

        "crawl": crawl_var.get(),

        "forms": forms_var.get(),

        "method": method_var.get(),

        "data": post_data_box.get("1.0", tk.END).strip(),

        "extra": extra_entry.get()
    }

    cmd = build_sqlmap_command(url, options)

    command_box.delete("1.0", tk.END)
    command_box.insert(tk.END, " ".join(cmd))


# =====================================
# 开始扫描
# =====================================

def start_scan():

    def log_callback(line):

        log_box.insert(tk.END, line + "\n")

        log_box.see(tk.END)

        root.update_idletasks()


    url = url_entry.get().strip()

    if not url:
        log_box.insert(tk.END, "[ERROR] URL不能为空\n")
        return

    options = {
        "mode": mode_var.get(),
        "random_agent": random_agent_var.get(),
        "tamper": tamper_var.get(),

        "threads": threads_var.get(),

        "parameter": parameter_entry.get(),

        "cookie": cookie_entry.get(),

        "headers": headers_entry.get(),

        "proxy": proxy_entry.get(),

        "technique": technique_var.get(),

        "crawl": crawl_var.get(),

        "forms": forms_var.get(),

        "method": method_var.get(),

        "data": post_data_box.get("1.0", tk.END).strip(),

        "extra": extra_entry.get(),

        "log_callback": log_callback
    }

    task = Task(
        task_id=1,
        task_type="sqlmap",
        target=url,
        options=options
    )

    log_box.delete("1.0", tk.END)

    log_box.insert(tk.END, "[INFO] 开始扫描...\n\n")

    result = run(task)

    log_box.insert(tk.END, f"状态: {result['status']}\n\n")

    log_box.insert(tk.END, result["details"])


# =====================================
# 主窗口
# =====================================

root = tk.Tk()

root.title("SQLMap 智能控制台")
root.geometry("1200x850")


# =====================================
# URL
# =====================================

tk.Label(root, text="Target URL").pack(anchor="w", padx=10)

url_entry = tk.Entry(root, width=140)
url_entry.pack(fill="x", padx=10, pady=5)

url_entry.bind("<KeyRelease>", lambda e: update_command())


# =====================================
# 扫描模式
# =====================================

mode_var = tk.StringVar(value="fast")

frame_mode = tk.LabelFrame(root, text="扫描模式")
frame_mode.pack(fill="x", padx=10, pady=5)

tk.Radiobutton(
    frame_mode,
    text="快速扫描",
    variable=mode_var,
    value="fast",
    command=update_command
).pack(side="left", padx=10)

tk.Radiobutton(
    frame_mode,
    text="标准扫描",
    variable=mode_var,
    value="normal",
    command=update_command
).pack(side="left", padx=10)

tk.Radiobutton(
    frame_mode,
    text="深度扫描",
    variable=mode_var,
    value="deep",
    command=update_command
).pack(side="left", padx=10)


# =====================================
# 请求方式
# =====================================

method_var = tk.StringVar(value="GET")

frame_method = tk.LabelFrame(root, text="请求方式")
frame_method.pack(fill="x", padx=10, pady=5)

tk.Radiobutton(
    frame_method,
    text="GET",
    variable=method_var,
    value="GET",
    command=update_command
).pack(side="left", padx=10)

tk.Radiobutton(
    frame_method,
    text="POST",
    variable=method_var,
    value="POST",
    command=update_command
).pack(side="left", padx=10)


# =====================================
# 功能选项
# =====================================

frame_options = tk.LabelFrame(root, text="功能选项")
frame_options.pack(fill="x", padx=10, pady=5)

random_agent_var = tk.BooleanVar(value=True)
tamper_var = tk.BooleanVar(value=False)
forms_var = tk.BooleanVar(value=False)

tk.Checkbutton(
    frame_options,
    text="Random-Agent",
    variable=random_agent_var,
    command=update_command
).pack(side="left", padx=10)

tk.Checkbutton(
    frame_options,
    text="WAF绕过",
    variable=tamper_var,
    command=update_command
).pack(side="left", padx=10)

tk.Checkbutton(
    frame_options,
    text="Forms",
    variable=forms_var,
    command=update_command
).pack(side="left", padx=10)


# =====================================
# 高级参数
# =====================================

frame_advanced = tk.LabelFrame(root, text="高级参数")
frame_advanced.pack(fill="x", padx=10, pady=5)


# Threads

tk.Label(frame_advanced, text="Threads").grid(row=0, column=0)

threads_var = tk.IntVar(value=5)

threads_spin = tk.Spinbox(
    frame_advanced,
    from_=1,
    to=20,
    textvariable=threads_var,
    command=update_command,
    width=5
)

threads_spin.grid(row=0, column=1, padx=5, pady=5)


# Parameter

tk.Label(frame_advanced, text="Parameter").grid(row=0, column=2)

parameter_entry = tk.Entry(frame_advanced, width=20)
parameter_entry.grid(row=0, column=3, padx=5, pady=5)

parameter_entry.bind("<KeyRelease>", lambda e: update_command())


# Technique

tk.Label(frame_advanced, text="Technique").grid(row=0, column=4)

technique_var = tk.StringVar(value="")

technique_box = ttk.Combobox(
    frame_advanced,
    textvariable=technique_var,
    values=[
        "",
        "B",
        "E",
        "U",
        "S",
        "T",
        "Q",
        "BEUSTQ"
    ],
    width=15
)

technique_box.grid(row=0, column=5, padx=5, pady=5)

technique_box.bind(
    "<<ComboboxSelected>>",
    lambda e: update_command()
)


# Crawl

tk.Label(frame_advanced, text="Crawl").grid(row=0, column=6)

crawl_var = tk.IntVar(value=0)

crawl_spin = tk.Spinbox(
    frame_advanced,
    from_=0,
    to=10,
    textvariable=crawl_var,
    command=update_command,
    width=5
)

crawl_spin.grid(row=0, column=7, padx=5, pady=5)


# Cookie

tk.Label(frame_advanced, text="Cookie").grid(row=1, column=0)

cookie_entry = tk.Entry(frame_advanced, width=100)
cookie_entry.grid(row=1, column=1, columnspan=7, padx=5, pady=5)

cookie_entry.bind("<KeyRelease>", lambda e: update_command())


# Headers

tk.Label(frame_advanced, text="Headers").grid(row=2, column=0)

headers_entry = tk.Entry(frame_advanced, width=100)
headers_entry.grid(row=2, column=1, columnspan=7, padx=5, pady=5)

headers_entry.bind("<KeyRelease>", lambda e: update_command())


# Proxy

tk.Label(frame_advanced, text="Proxy").grid(row=3, column=0)

proxy_entry = tk.Entry(frame_advanced, width=100)
proxy_entry.grid(row=3, column=1, columnspan=7, padx=5, pady=5)

proxy_entry.bind("<KeyRelease>", lambda e: update_command())


# Extra

tk.Label(frame_advanced, text="Extra").grid(row=4, column=0)

extra_entry = tk.Entry(frame_advanced, width=100)
extra_entry.grid(row=4, column=1, columnspan=7, padx=5, pady=5)

extra_entry.bind("<KeyRelease>", lambda e: update_command())


# =====================================
# POST Data
# =====================================

frame_post = tk.LabelFrame(root, text="POST Data")
frame_post.pack(fill="x", padx=10, pady=5)

post_data_box = ScrolledText(frame_post, height=5)

post_data_box.pack(fill="x", padx=5, pady=5)

post_data_box.bind("<KeyRelease>", lambda e: update_command())


# =====================================
# 实时命令
# =====================================

tk.Label(root, text="实时生成命令").pack(anchor="w", padx=10)

command_box = ScrolledText(root, height=6)

command_box.pack(fill="x", padx=10, pady=5)


# =====================================
# 开始扫描按钮
# =====================================

scan_button = tk.Button(
    root,
    text="开始扫描",
    command=start_scan,
    height=2
)

scan_button.pack(pady=10)


# =====================================
# 日志输出
# =====================================

tk.Label(root, text="扫描日志").pack(anchor="w", padx=10)

log_box = ScrolledText(root, height=20)

log_box.pack(fill="both", expand=True, padx=10, pady=5)


# =====================================
# 初始化
# =====================================

update_command()

root.mainloop()