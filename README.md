# crtsearch
# 证书信息查询工具

该工具可以查询指定域名或一组域名的 SSL 证书信息。它使用 crt.sh 提供的 API，通过网络请求获取 SSL 证书的详细信息，并将结果保存为 CSV 文件。

## 功能特性

1. **单个域名查询：** 通过提供 `-t` 或 `--domain` 参数，用户可以查询单个域名的 SSL 证书信息。

2. **批量查询：** 使用 `-T` 或 `--txtfile` 参数，用户可以从包含多个域名的文本文件中一次性查询多个域名的 SSL 证书信息。

3. **结果保存：** 查询结果以 CSV 格式保存，包括证书的公共名称、匹配的标识、颁发者名称、有效起始日期和过期日期。

4. **单个域名结果：** 生成的 CSV 文件以查询的域名为文件名，方便用户查阅单个域名的证书信息。

5. **批量结果：** 如果提供了域名列表文件，脚本会生成一个名为 `all_results.csv` 的 CSV 文件，其中包含所有查询结果的摘要。

## 如何使用

![image1](https://github.com/himay1/crtsearch/blob/main/img/1.jpg)
### 安装
```bash
python -r requirements.txt
```
### 单个域名查询
```bash
python crtsearch.py -t example.com
```
### 批量域名查询
```bash
python crtsearch.py -T domain.txt
```
![image1](https://github.com/himay1/crtsearch/blob/main/img/2.jpg)
![image1](https://github.com/himay1/crtsearch/blob/main/img/3.jpg)
