from src.query import conn, cur

class DBManager:
    
    def __init__(self, conn, cur):
        self.conn = conn
        self.cur = cur

    def get_companies_and_vacancies_count(self):
        res = self.cur.execute("select e.name, a.count from (select employer_id, count(id) from vacancies group by employer_id) as a inner join employers e on a.employer_id=e.id;")
        print(self.cur.fetchall())


test = DBManager(conn, cur)
test.get_companies_and_vacancies_count()