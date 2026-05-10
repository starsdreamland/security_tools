import subprocess

from core.parser import build_sqlmap_command


def run_sqlmap(url, options=None, log_callback=None):

    if options is None:
        options = {}

    cmd = build_sqlmap_command(url, options)

    try:

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        output_lines = []

        # =========================
        # 实时读取输出
        # =========================

        for line in process.stdout:

            line = line.rstrip()

            output_lines.append(line)

            # GUI实时输出
            if log_callback:
                log_callback(line)

        process.wait()

        output = "\n".join(output_lines)

    except Exception as e:

        return {
            "type": "SQL Injection",
            "status": "error",
            "details": f"执行异常: {str(e)}"
        }

    # =========================
    # 漏洞判断
    # =========================

    output_lower = output.lower()

    if "is vulnerable" in output_lower:
        status = "vulnerable"

    elif (
        "unable to retrieve page content" in output_lower
        or
        "connection timed out" in output_lower
    ):
        status = "error"

    else:
        status = "not vulnerable"

    return {
        "type": "SQL Injection",
        "status": status,
        "details": output
    }