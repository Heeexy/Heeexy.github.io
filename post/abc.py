import os

def process_markdown_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)
            process_file(file_path)

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        new_lines = []
        for line in lines:
            # 查找categories并修改
            if line.strip().startswith('categories:'):
                # 替换categories为no-categories
                new_line = line.replace('categories:', 'no-categories:')
                new_lines.append(new_line)
            else:
                new_lines.append(line)

        # 重新写入文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)
        
        print(f"Processed {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

# Replace 'your_directory_path' with your actual directory path containing Markdown files.
process_markdown_files('/Users/hexiaoyu/code/hugo-blog/content/post')

