import psycopg2
from src.parser import Parser
import os

conn = psycopg2.connect(host="192.168.0.22", port=49153, database="cw_5", user="postgres", password="123456")
cur = conn.cursor()


def write_data(employer, conn, cur):
    empoer_name = employer["name"]
    emploer_id = employer["id"]
    cur.execute("INSERT INTO employers VALUES (%s, %s)", (emploer_id, empoer_name))
    for vacanci in employer["vacancies"]:
        vacanci_id = vacanci["id"]
        vacanci_name = vacanci["name"]
        employer_url = vacanci["employer_url"]
        area = vacanci["area"]
        salary_from = vacanci["salary_min"]
        salary_to = vacanci["salary_max"]
        curency = vacanci["currency"]
        cur.execute("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (vacanci_id, 
                                                                                      vacanci_name, 
                                                                                      employer_url, 
                                                                                      area, salary_from, 
                                                                                      salary_to,
                                                                                      curency,
                                                                                      emploer_id))
        


    conn.commit()