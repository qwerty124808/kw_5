from src.query import conn, cur

class DBManager:
    
    def __init__(self, conn, cur):
        self.conn = conn
        self.cur = cur

    def get_companies_and_vacancies_count(self):
        """
            Принтанёт список всех компаний и количество вакансий у каждой компании.
        """
        res = self.cur.execute("select e.name, a.count from (select employer_id, count(id) from vacancies group by employer_id) as a inner join employers e on a.employer_id=e.id;")
        print(self.cur.fetchall())

    def get_all_vacancies(self):
        """
            Принтит список всех вакансий с указанием названия компании, названия вакансии и зарплаты
        """
        res = self.cur.execute("select employers.name, vacancies.name, vacancies.salary_from, vacancies.salary_to from vacancies join employers on vacancies.employer_id = employers.id;")
        print(self.cur.fetchall())

    def get_avg_salary(self):
        """
           Возвращает среднюю зарплату по вакансиям
        """
        res = self.cur.execute("select ROUND(avg(avg_salary), -1) from vacancies")
        return self.cur.fetchone()

    def get_vacancies_with_higher_salary(self):
        """
            Принтит список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        res = self.cur.execute("select * from vacancies where avg_salary > (select round(avg(avg_salary), -1) from vacancies)")
        print(self.cur.fetchall())

    def get_vacancies_with_keyword(self, key_word):
        """
            Cписок всех вакансий, в названии которых содержется переданное в метод слово
        """
        res = self.cur.execute(f"select * from vacancies where name like '%{key_word}%';")
        print(self.cur.fetchall())