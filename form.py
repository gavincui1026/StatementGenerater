from pdf import PDF
from statement import Statement
class StatementForm:
    def __init__(self, number_of_statements):
        self.balance = 0

        self.statement = Statement()
        self.form = []
        for _ in range(number_of_statements):
            self.form.append(self.statement.get_single_statement())
        self.sort_by_date(self.form)
        for statement in self.form:
            self.balance += statement['amount']
            statement['balance'] = self.balance



    def set_overall_date(self, date):
        for statement in self.form:
            statement['date'] = date

    def sort_by_date(self,form):
        form.sort(key=lambda x: x['date'])

if __name__ == "__main__":
    statement = StatementForm(5)
    print(statement.form)


