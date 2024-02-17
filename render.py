from jinja2 import FileSystemLoader, Environment
from form import StatementForm

class RenderStatement(StatementForm):
    def __init__(self, number_of_statements):
        super().__init__(number_of_statements)

    def render_form(self):
        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)
        template = env.get_template('transaction_form.html')
        output = template.render(transactions=self.form)
        return output
    def render_page(self):
        rendered_form = self.render_form()
        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)
        template = env.get_template('base.html')
        output = template.render(table=rendered_form)
        return output

    def render_to_pdf(self):
        import subprocess
        html_path = 'output.html'
        pdf_path = 'output.pdf'
        subprocess.run(['wkhtmltopdf', html_path, pdf_path])

if __name__ == "__main__":
    statement = RenderStatement(5)
    # with open('output.html', 'w') as f:
    #     f.write(statement.render_page())
    statement.render_to_pdf()












