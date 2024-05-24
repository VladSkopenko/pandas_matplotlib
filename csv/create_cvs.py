import csv


data = [
    ["name", "email", "phone", "favorite"],
    ["Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", "False"],
    ["Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", "False"],
    ["Kennedy Lane", "mattis.Cras@nonenimMauris.net", "(542) 451-7038", "True"],
    ["Wylie Pope", "est@utquamvel.net", "(692) 802-2949", "False"],
    ["Cyrus Jackson", "nibh@semsempererat.com", "(501) 472-5218", "True"]
]

# Створення та запис у файл contacts.csv
with open('users.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV файл успішно створено.")