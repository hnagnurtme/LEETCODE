import os
import re

repo_path = "."
problems = []

# Quét toàn bộ thư mục để tìm bài LeetCode
for entry in os.listdir(repo_path):
    folder = os.path.join(repo_path, entry)
    if os.path.isdir(folder) and re.match(r"^\d{4}-", entry):
        # Tách id + title từ tên folder
        parts = entry.split("-", 1)
        qid = parts[0]
        title = parts[1].replace("-", " ").title() if len(parts) > 1 else "Unknown"

        # Kiểm tra Solution.java
        solution_file = os.path.join(folder, "Solution.java")
        if os.path.exists(solution_file):
            problems.append((qid, title, "Java", os.path.relpath(solution_file, repo_path)))
        else:
            # fallback: lấy file .cpp hoặc .java khác nếu có
            for f in os.listdir(folder):
                if f.endswith(".cpp") or f.endswith(".java"):
                    problems.append((qid, title, f.split(".")[-1].upper(), os.path.join(entry, f)))

# Sort theo ID
problems.sort(key=lambda x: int(x[0]))

# Tạo bảng markdown
table_header = "| # | Tiêu đề | Ngôn ngữ | File |\n|---|----------|----------|------|"
table_rows = []
for qid, title, lang, path in problems:
    row = f"| {qid} | {title} | {lang} | [link]({path}) |"
    table_rows.append(row)

table_md = table_header + "\n" + "\n".join(table_rows)

# ========== PHẦN MỚI: Tạo Notes Section ==========
notes_sections = []

for entry in os.listdir(repo_path):
    folder = os.path.join(repo_path, entry)
    note_file = os.path.join(folder, "NOTE.md")
    
    # Chỉ xử lý folder có NOTE.md
    if os.path.isdir(folder) and re.match(r"^\d{4}-", entry) and os.path.exists(note_file):
        parts = entry.split("-", 1)
        qid = parts[0]
        title = parts[1].replace("-", " ").title() if len(parts) > 1 else "Unknown"
        
        # Đọc nội dung NOTE.md
        with open(note_file, "r", encoding="utf-8") as nf:
            note_content = nf.read().strip()
        
        # Tạo section cho bài này
        note_section = f"""### {qid} - {title}
<details>
<summary>📖 Xem ghi chú</summary>

{note_content}

> _[Xem file gốc]({entry}/NOTE.md)_

</details>

---
"""
        notes_sections.append((int(qid), note_section))

# Sort notes theo ID
notes_sections.sort(key=lambda x: x[0])
notes_md = "\n".join([section for _, section in notes_sections])

# Nếu không có notes nào thì để trống
if not notes_md:
    notes_md = "_Chưa có ghi chú nào. Thêm file `NOTE.md` vào folder bài tập để hiển thị ở đây._"

# ========== Cập nhật README.md ==========
readme = "README.md"
with open(readme, "r", encoding="utf-8") as f:
    content = f.read()

# Update bảng problems
pattern_table = r"<!-- TABLE:START -->(.*?)<!-- TABLE:END -->"
replacement_table = f"<!-- TABLE:START -->\n{table_md}\n<!-- TABLE:END -->"

if re.search(pattern_table, content, flags=re.S):
    content = re.sub(pattern_table, replacement_table, content, flags=re.S)
else:
    content += "\n\n" + replacement_table

# Update notes section
pattern_notes = r"<!-- NOTES:START -->(.*?)<!-- NOTES:END -->"
replacement_notes = f"<!-- NOTES:START -->\n{notes_md}\n<!-- NOTES:END -->"

if re.search(pattern_notes, content, flags=re.S):
    content = re.sub(pattern_notes, replacement_notes, content, flags=re.S)
else:
    # Nếu chưa có block NOTES thì thêm vào sau TABLE
    notes_block = f"\n\n## 📝 Notes & Showcases\n\nCác ghi chú chi tiết cho từng bài đã hoàn thành:\n\n{replacement_notes}"
    content = re.sub(r"(<!-- TABLE:END -->)", r"\1" + notes_block, content)

with open(readme, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Updated {len(problems)} problems")
print(f"📝 Found {len(notes_sections)} notes")