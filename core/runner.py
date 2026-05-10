from tools.sqlmap_tool import run_sqlmap


class Task:
    def __init__(self, task_id, task_type, target, options=None):
        self.id = task_id
        self.type = task_type
        self.target = target
        self.options = options or {}


def run(task: Task):
    if task.type == "sqlmap":
        return run_sqlmap(
            task.target,
            task.options,
            task.options.get("log_callback")
        )
        return result

    return {
        "type": "Unknown",
        "status": "failed",
        "details": [f"Unsupported task type: {task.type}"]
    }