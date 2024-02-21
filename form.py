import random
from datetime import datetime, timedelta
from random import choice

from _decimal import Decimal

from statement import Statement
from settings import settings
class StatementForm:
    def __init__(self, items_per_page=10):
        number_of_statements = int(settings.transaction_amount)
        self.balance = self.set_random_balance()
        self.items_per_page = items_per_page
        self.statement = Statement()
        self.form = []
        for _ in range(number_of_statements):
            self.form.append(self.statement.get_single_statement())
        withdraw_dates = self.withdraw()
        for date in withdraw_dates:
            self.form.append(self.statement.set_withdraw_statement(date))
        self.sort_by_date(self.form)
        for statement in self.form:
            if 'General Withdrawal' in statement['description']:
                amount = self.balance * -1
                statement['amount'] = Decimal(str(amount))
            amount = Decimal(str(statement['amount']))
            self.balance += amount
            statement['balance'] = '{:.2f}'.format(self.balance)
        self.total_pages = len(self.form) // items_per_page + (1 if len(self.form) % items_per_page > 0 else 0)
        self.start, self.end = self.set_overall_date()
        self.set_email()

    def withdraw(self):
        withdraw_data = []
        # 计算所有的withdrawdate，两周一次，在self.start_date和self.end_date之间
        start_datetime = datetime.strptime(self.statement.start_date, '%Y-%m-%d')
        end_datetime = datetime.strptime(self.statement.end_date, '%Y-%m-%d')
        current_datetime = start_datetime
        while current_datetime < end_datetime:
            withdraw_data.append(current_datetime.strftime('%m/%d/%Y'))
            current_datetime += timedelta(days=14)
        return withdraw_data


    def set_overall_date(self):
        start_date = self.form[0]['date']
        end_date = self.form[-1]['date']
        # 提取年月
        start_month, start_date, start_year = start_date.split('/')
        end_month, end_date, end_year = end_date.split('/')
        start=start_month+'/'+start_year
        end=end_month+'/'+end_year
        return start, end

    def sort_by_date(self, form):
        # 使用datetime.strptime来解析日期字符串，然后根据日期进行排序
        form.sort(key=lambda x: datetime.strptime(x['date'], '%m/%d/%Y'))


    def get_page(self, page_number):
        start = (page_number - 1) * self.items_per_page
        end = start + self.items_per_page
        return self.form[start:end]

    def generate_random_mid(self):
        template="PB239A69GK7G"
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        result = "PB"
        for char in template[2:]:
            if char.isalpha():
                result += choice(letters)
            elif char.isdigit():
                result += choice(numbers)
        return result

    def set_email(self):
        self.email = settings.email

    def set_random_balance(self,min_balance=1000, max_balance=10000):
        """
        Generate a random balance within specified range and ensure it has two decimal places.

        :param min_balance: Minimum possible balance
        :param max_balance: Maximum possible balance
        :return: A Decimal representing the balance with two decimal places
        """
        balance = Decimal(random.uniform(min_balance, max_balance)).quantize(Decimal('0.00'))
        return balance


if __name__ == "__main__":
    statement = StatementForm(5)
    print(statement.form)


