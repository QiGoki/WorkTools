from faker import Faker

fake = Faker(locale='zh_CN')

fakeData = [{"content": fake.paragraph(nb_sentences=6), "date": fake.date()} for _ in range(20)]
