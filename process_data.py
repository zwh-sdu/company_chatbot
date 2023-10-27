import os

def split_text_file(input_file_path, max_length, file_name):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    chunks = []
    current_chunk = ""
    lines = content.split('\n')

    for line in lines:
        if len(current_chunk) + len(line) + 1 <= max_length:
            current_chunk += line + '\n'
        else:
            chunks.append(file_name + "\n" + current_chunk)
            current_chunk = line + '\n'

    if current_chunk:
        chunks.append(file_name + "\n" + current_chunk)

    return chunks

def split_and_save_files(input_folder, output_folder, max_length):
    for root, _, files in os.walk(input_folder):
        for file_name in files:
            if file_name.endswith('.txt'):
                input_file_path = os.path.join(root, file_name)
                chunks = split_text_file(input_file_path, max_length, os.path.splitext(file_name)[0])
                for i, chunk in enumerate(chunks):
                    output_file_name = f"{os.path.splitext(file_name)[0]}_{i + 1}.txt"
                    output_file_path = os.path.join(output_folder, output_file_name)
                    with open(output_file_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(chunk)

input_folder = "/data/zhangwenhao-slurm/code/company_langchain/txt"  # 输入文件夹的路径
output_folder = "/data/zhangwenhao-slurm/code/company_langchain/txt_split"  # 输出文件夹的路径
max_length = 1000  # 设置最大长度

split_and_save_files(input_folder, output_folder, max_length)
