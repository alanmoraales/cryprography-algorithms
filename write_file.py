def write_file(file_dir, content):
    file = open(file_dir, "w", encoding='utf-8', newline="")
    file.write(content)
    file.close()
