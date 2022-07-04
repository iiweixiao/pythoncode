import markdown
import pdfkit
# 还要安装wkhtmltopdf，[github下载地址](https://github.com/wkhtmltopdf/wkhtmltopdf)


def md2pdf(md_file):
    html_file = md_file.rsplit('/', 1)[0]+'/html.html'
    pdf_file = md_file.rsplit('.', 1)[0]+'.pdf'


    str = "<meta charset='utf-8'>"

    with open(md_file, "r", encoding="utf-8") as f:
        text = f.read()

    html = markdown.markdown(text)

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(str)
        f.write(html)

    # options = {
    #     'page-size': 'A4',
    #     # 'orientation': 'Landscape',
    #     'margin-top': '0.7in',
    #     'margin-right': '0.75in',
    #     'margin-bottom': '0.7in',
    #     'margin-left': '0.75in',
    #     'encoding': 'UTF-8',
    # }
    pdfkit.from_file(html_file, pdf_file)


md_file = '/Users/abc/Downloads/demo-batch-markdown-to-pdf-master/README.md'
md2pdf(md_file)