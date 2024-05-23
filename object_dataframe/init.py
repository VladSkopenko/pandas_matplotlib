import pandas as pd

contacts = pd.DataFrame(
    {
        "name": [
            "Allen Raymond",
            "Chaim Lewis",
            "Kennedy Lane",
            "Wylie Pope",
            "Cyrus Jackson",
        ],
        "email": [
            "nulla.ante@vestibul.co.uk",
            "dui.in@egetlacus.ca",
            "mattis.Cras@nonenimMauris.net",
            "est@utquamvel.net",
            "nibh@semsempererat.com",
        ],
        "phone": [
            "(992) 914-3792",
            "(294) 840-6685",
            "(542) 451-7038",
            "(692) 802-2949",
            "(501) 472-5218",
        ],
        "favorite": [False, False, True, False, True],
    },
    index=[1, 2, 3, 4, 5],
)
if __name__ == "__main__":
    print("Об'єкт DataFrame це таблиця в якій ключі відповідають назві колонок а значення-списки їх рядкам")
    print(contacts)
    print("\n-----------------------------------------------\n")
    print("Можна взяти весь стовбчик за допомогою ключа словника(назви колонки)")
    print(contacts["name"])
    print("\n-----------------------------------------------\n")
    print("Метод loc дозволяє фільтрувати та вибирати потрібні рядки наприклад за индексами або іншими значеннями")
    print(contacts.loc[1])
    print(contacts.loc[contacts['favorite'] == True]) # НЕ ЕЛЕГАНТНО
    print("\n-----------------------------------------------\n")
    print("за индексом , починаючи з 0 і закінчуючи -1")
    print(contacts.iloc[1])
