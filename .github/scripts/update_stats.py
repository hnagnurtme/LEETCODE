import os
import re

repo_path = "."
img_entries = []

# Quét toàn bộ thư mục dạng "0001-title"
for entry in os.listdir(repo_path):
    folder = os.path.join(repo_path, entry)
    if os.path.isdir(folder) and re.match(r"^\d{4}-", entry):
        # Lấy ID và tiêu đề
        parts = entry.split("-", 1)
        qid = parts[0]
        title = parts[1].replace("-", " ").title() if len(parts) > 1 else "Unknown"

        # Tìm file .png
        for f in os.listdir(folder):
            if f.lower().endswith(".png"):
                img_path = os.path.join(entry, f)
                img_entries.append((int(qid), title, img_path))
                break  # Mỗi bài chỉ cần 1 ảnh
                

# Sort theo ID
img_entries.sort(key=lambda x: x[0])

# ====== Tạo markdown list ======
if img_entries:
    img_md = "\n".join([f"- **{qid:04d} - {title}**  \n  ![]({path})" for qid, title, path in img_entries])
else:
    img_md = "_Chưa có hình minh họa nào._"

# ====== Cập nhật README.md ======
readme = "README.md"
with open(readme, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"<!-- IMG:START -->(.*?)<!-- IMG:END -->"
replacement = f"<!-- IMG:START -->\n{img_md}\n<!-- IMG:END -->"

if re.search(pattern, content, flags=re.S):
    content = re.sub(pattern, replacement, content, flags=re.S)
else:
    # Nếu chưa có block IMG thì thêm vào cuối file
    content += f"\n\n## 🖼️ Visual Notes\n\n{replacement}"

with open(readme, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Updated README with {len(img_entries)} image notes.")
