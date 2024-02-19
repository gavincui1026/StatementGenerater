from jinja2 import FileSystemLoader, Environment
from form import StatementForm

class RenderStatement(StatementForm):
    def __init__(self, page_size=10):
        super().__init__()
        self.page_size = page_size
        self.env = Environment(loader=FileSystemLoader('templates'))
    def paginate(self, items, page_size):
        """将items分割为多个子列表，每个子列表代表一页"""
        for i in range(0, len(items), page_size):
            yield items[i:i + page_size]

    def render_form(self, transactions):
        """渲染单页表格"""
        template = self.env.get_template('transaction_form.html')
        return template.render(transactions=transactions)

    # def render_pages(self):
    #     """渲染所有页面，并返回包含所有页面HTML字符串的列表"""
    #     pages_content = []
    #     # 根据self.form和self.page_size进行分页
    #     for page_transactions in self.paginate(self.form, self.page_size):
    #         page_html = self.render_form(page_transactions)
    #         pages_content.append(page_html)
    #     return pages_content
    def render_pages(self):
        """渲染所有页面，并返回包含所有页面HTML字符串的列表"""
        self.pages_content = []
        # 根据self.form和self.page_size进行分页
        for page_transactions in self.paginate(self.form, self.page_size):
            page_html = self.render_form(page_transactions)
            self.pages_content.append(page_html)
        return self.pages_content



    def render_to_html(self):
        """渲染所有页面，并返回HTML字符串"""
        pages_content = []
        for form in self.render_pages():
            # 在每个表格后添加分页符
            form += '<div style="page-break-after: always;"></div>'
            pages_content.append(form)

        template = self.env.get_template('base.html')
        return template.render(tables=pages_content, overall_start=self.start, overall_end=self.end, total_pages=self.total_pages, email=self.email)

if __name__ == "__main__":
    statement = RenderStatement(20)
    html=statement.render_to_html()
    with open('output.html', 'w') as f:
        f.write(html)












