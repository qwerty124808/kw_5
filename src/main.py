from src.parser import Parser
from src.query import conn, cur, write_data

parser = Parser()
employers_list = parser.get_employers()
for employer in employers_list:
    employer = employer.corect_data()
    write_data_test = write_data(employer, conn, cur)