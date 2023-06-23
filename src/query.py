import psycopg2
from src.parser import Parser
import os

conn = psycopg2.connect(host="192.168.0.22", port=49153, database="cw_5", user="postgres", password="123456")
cur = conn.cursor()


def write_data(employer, conn, cur):
    """
        записывает данные в базу
    """
    employer_name = employer["name"]
    employer_id = employer["id"]
    cur.execute("INSERT INTO employers VALUES (%s, %s)", (employer_id, employer_name))
    for vacanci in employer["vacancies"]:
        print(vacanci)
        vacanci_id = vacanci["id"]
        vacanci_name = vacanci["name"]
        employer_url = vacanci["employer_url"]
        area = vacanci["area"]
        salary_from = vacanci["salary_min"]
        salary_to = vacanci["salary_max"]
        curency = vacanci["currency"]
        avg_salary = vacanci["avg_salary"]
        cur.execute("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (vacanci_id, 
                                                                                      vacanci_name, 
                                                                                      employer_url, 
                                                                                      area, 
                                                                                      salary_from, 
                                                                                      salary_to,
                                                                                      avg_salary,
                                                                                      curency,
                                                                                      employer_id))
    conn.commit()