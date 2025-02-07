import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

file_url = "https://s3-us-west-1.amazonaws.com/umbrella-static/top-1m.csv.zip"

file_path = "top-1m.csv.zip"

# 下载文件
try:
    # 打开URL并读取内容
    response = urllib.request.urlopen(file_url)
    # 写入文件
    with open(file_path, 'wb') as out_file:
        out_file.write(response.read())
    print(f"文件已成功下载并保存为 {file_path}")
except Exception as e:
    print(f"下载文件时发生错误: {e}")
