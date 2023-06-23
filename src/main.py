from src.parser import Parser
from src.query import conn, cur, write_data
from src.db_manager import DBManager

parser = Parser()
employers_list = parser.get_employers()
for employer in employers_list:
    employer = employer.corect_data()
    write_data_test = write_data(employer, conn, cur)

db_manager = DBManager(conn, cur)

while True:
    user_input = int(input("Cписок всех компаний и количество вакансий у каждой компании: 1\n" \
                            "Cписок всех вакансий с указанием названия компании, названия вакансии и зарплаты: 2\n" \
                            "Cреднюю зарплату по вакансиям: 3\n" \
                            "список всех вакансий, у которых зарплата выше средней по всем вакансиям: 4\n" \
                            "Cписок всех вакансий, в названии которых содержется переданное в метод слово: 5\n" \
                            "Завершить программу: 6\n" \
                            "Введите число из списка: "))
    if user_input == 1:
        db_manager.get_companies_and_vacancies_count()
    elif user_input == 2:
        db_manager.get_all_vacancies()
    elif user_input == 3:
        avg = db_manager.get_avg_salary()
        print(avg[0])
    elif user_input == 4:
        db_manager.get_vacancies_with_higher_salary()
    elif user_input == 5:
        key_word = input("Введите ключевое слово: ")
        db_manager.get_vacancies_with_keyword(key_word)
    elif user_input == 6:
        break 