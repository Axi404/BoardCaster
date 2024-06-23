import json

# 读取现有的 JSON 文件
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 创建一个字典，以 name 为键，存储相应的条目
schools_dict = {}
for entry in data['schools']:
    name = entry['name']
    if name not in schools_dict:
        schools_dict[name] = []
    schools_dict[name].append(entry)

# 生成 Markdown 内容
markdown_lines = []
markdown_lines.append("# CSWinterCamp2024 & CSSummerCamp2024")
markdown_lines.append("")
markdown_lines.append(">[!IMPORTANT] ")
markdown_lines.append(">1. 关于**2024年CS推免冬令营、夏令营通知公告**的汇总。欢迎大家积极分享夏令营信息，资瓷一下互联网精神吼不吼啊？（本仓库将随各校通知的发布实时更新，具体形式可参见往年：[CSSummerCamp2023](https://github.com/CS-BAOYAN/CSSummerCamp2023/tree/main)、[CSSummerCamp2022](https://github.com/LinghaoChan/CSSummerCamp2022)、[CSSummerCamp2021](https://github.com/hit-thusz-RookieCJ/CSSummerCamp2021)、[CSSummerCamp2020](https://github.com/hcy226/CSSummerCamp2020)）。")
markdown_lines.append(">")
markdown_lines.append(">2. 另附[CS-BAOYAN-2024](https://github.com/CS-BAOYAN/CS-BAOYAN-2024)，这是一份保研小白必看的往年经验贴大全，建议全部看完至少掌握保研流程，否则容易问一些很显然的问题")
markdown_lines.append(">")
markdown_lines.append(">3. 关于2024年CS保研实验室/导师招生广告的汇总请查看[CSLabInfo2024](https://github.com/CS-BAOYAN/CSLabInfo2024)。该仓库仅提供招生信息发布渠道，不负责验证这些信息的完整性、准确性、时效性，不保证使用这些信息而获得的结果。对于因信息内容可能与实际情况不一致而导致的任何正面或负面影响，仓库管理者亦不承担任何责任或义务，请各位自行辨别。")
markdown_lines.append(">4. 关于一些CS/EE专业的学生，我们也建立了[CSBasicKnowledge](https://github.com/CS-BAOYAN/CSBasicKnowledge)，这是一个记录一些基础知识的仓库，欢迎大家pr & star，将你觉得有用的知识pr上来，造福学弟学妹。")
markdown_lines.append(">5. **本仓库仅提供夏令营信息发布渠道，不负责验证这些信息的完整性、准确性、时效性，不保证使用这些信息而获得的结果。对于因信息内容可能与实际情况不一致而导致的任何正面或负面影响，仓库管理者亦不承担任何责任或义务，请各位自行辨别。**")
markdown_lines.append(">")
markdown_lines.append(">预祝大家夏令营成功上岸！都有喜欢的offer！")
markdown_lines.append("")
markdown_lines.append("# CSSummerCamp2024")
markdown_lines.append("")
for name, entries in schools_dict.items():
    markdown_lines.append(f"## {name}\n")
    for entry in entries:
        line = f"【截止日期：{entry['deadline'][0:10]} {entry['deadline'][11:19]}】[{entry['institute']}]({entry['website']}) {entry['description']}"
        markdown_lines.append(line)
        markdown_lines.append("")  # 空一行
    markdown_lines.append("")  # 空一行
    markdown_lines.append("")  # 空一行

# 将 Markdown 内容写入文件
with open('output.md', 'w', encoding='utf-8') as file:
    file.write("\n".join(markdown_lines))
