class Data:
    """ Класс для обработки данных о работодателях и их вакансиях """

    def __init__(self, employer_name, employer_id, employer_url, vacansys_list):
        self.employer_name = employer_name
        self.employer_id = employer_id
        self.employer_url = employer_url
        self.vacansys_list = vacansys_list

    
    @staticmethod
    def corect_vacansys(vacansys_list):
        correct_vacansys_list = []
        for vacansys in vacansys_list:
            data_vacansy = {}
            id = vacansys["id"]
            vacansys_name = vacansys["name"]
            url = vacansys['apply_alternate_url']
            area = vacansys['area']["name"]
            if vacansys["salary"] is None:
                data_vacansy["salary_min"] = None
                data_vacansy["salary_max"] = None
                data_vacansy["currency"] = None
            else:
                data_vacansy["salary_min"] = vacansys["salary"]["from"]
                data_vacansy["salary_max"] =  vacansys["salary"]["to"]
                data_vacansy["currency"] = vacansys["salary"]["currency"]
            data_vacansy["id"] = id
            data_vacansy["name"] = vacansys_name
            data_vacansy["employer_url"] = url
            data_vacansy["area"] = area
            correct_vacansys_list.append(data_vacansy)
        return correct_vacansys_list
        

    def corect_data(self):
        return {
            "name": self.employer_name,
            "id": self.employer_id,
            "url": self.employer_url,
            "vacancies": self.corect_vacansys(self.vacansys_list)
            }