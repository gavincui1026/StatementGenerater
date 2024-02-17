import hashlib
import random
from datetime import datetime

import faker
from faker import Faker



class Statement:
    def generate_fake_name(self):
        fake = faker.Faker()
        return fake.name()

    def generate_fake_email(self, name):
        name_bytes = name.encode('utf-8')
        md5_hash = hashlib.md5(name_bytes).hexdigest()
        merged_name = name.replace(' ', '')
        if md5_hash[-1] in '1234567890':
            return merged_name + '@gmail.com'
        elif md5_hash[-1] in 'abcdef':
            return merged_name + '1127@163.com'
        elif md5_hash[-1] in 'ghijkl':
            return merged_name + 'master@protonmail.com'
        elif md5_hash[-1] in 'mnopqr':
            return merged_name + '@yahoo.com'
        elif md5_hash[-1] in 'stuvwx':
            return merged_name + '@zoho.com'

    def generate_us_address(self):
        fake = faker.Faker()
        address = fake.address()
        return address.replace('\n', ', ')


    def generate_random_date(self, start_date, end_date):
        fake = Faker()
        start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
        end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
        random_date = fake.date_between(start_datetime, end_datetime)
        # 将日期的-替换成/，以符合美国日期格式
        return random_date.strftime('%m/%d/%Y')

    def generate_description(self):
        uuid = self.generate_unique_id()
        threshold = 0.95
        rand_num = random.random()
        checkout_description = 'Checkout Payment' + "/n" + 'Transaction ID: ' + uuid
        refund_description = 'Refund Payment' + "/n" + 'Transaction ID: ' + uuid
        return checkout_description

    def generate_unique_id(self):
        fake = faker.Faker()
        return fake.uuid4()

    def get_currency_with_probability(self):
        # Set a threshold for the probability
        threshold = 0.9  # 90% probability
        # Generate a random number between 0 and 1
        rand_num = random.random()
        # Return 'USD' if the random number is less than the threshold, otherwise 'CAD'
        return 'USD' if rand_num < threshold else 'CAD'

    def generate_random_amount(self):
        random_float = round(random.uniform(100, 200), 2)
        amount = random_float
        return amount



    def get_single_statement(self):
        name = self.generate_fake_name()
        email = self.generate_fake_email(name)
        address = self.generate_us_address()
        date = self.generate_random_date('2021-01-01', '2023-12-31')
        status = 'completed'
        currency = self.get_currency_with_probability()
        description = self.generate_description()
        amount = self.generate_random_amount()

        return {
            "date": date,
            "description": description,
            "name": name,
            "email": email,
            "amount": amount,
            "fee": "0.00",
        }
if __name__ == "__main__":
    statement = Statement()
    print(statement.generate_us_address())

