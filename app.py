
# Danh sách lưu các công việc
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: {task_name}")

# Kiểm tra chức năng
add_task("Làm bài tập Python")
print(tasks)
