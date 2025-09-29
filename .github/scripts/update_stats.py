import os
import re

repo_path = "."
problems = []

for entry in os.listdir(repo_path):
    folder = os.path.join(repo_path, entry)
    if os.path.isdir(folder) and re.match(r"^\d{4}-", entry):
        # Tách id + title
        parts = entry.split("-", 1)
        qid = parts[0]
        title = parts[1].replace("-", " ").title() if len(parts) > 1 else "Unknown"

        # Kiểm tra Solution.java
        solution_file = os.path.join(folder, "Solution.java")
        if os.path.exists(solution_file):
            problems.append((qid, title, "Java", os.path.relpath(solution_file, repo_path)))
        else:
            # fallback: lấy file .cpp nếu có
            for f in os.listdir(folder):
                if f.endswith(".cpp") or f.endswith(".java"):
                    problems.append((qid, title, f.split(".")[-1].upper(), os.path.join(entry, f)))

# Sort theo id
problems.sort(key=lambda x: int(x[0]))

# --- Update README.md ---
readme = "README.md"
with open(readme, "r", encoding="utf-8") as f:
    content = f.read()

# Tạo bảng markdown
table_header = "| # | Tiêu đề | Ngôn ngữ | File |\n|---|----------|----------|------|"
table_rows = []
for qid, title, lang, path in problems:
    row = f"| {qid} | {title} | {lang} | [link]({path}) |"
    table_rows.append(row)

table_md = table_header + "\n" + "\n".join(table_rows)

content = re.sub(
    r"<!-- TABLE:START -->(.*?)<!-- TABLE:END -->",
    f"<!-- TABLE:START -->\n{table_md}\n<!-- TABLE:END -->",
    content,
    flags=re.S,
)

with open(readme, "w", encoding="utf-8") as f:
    f.write(content)
