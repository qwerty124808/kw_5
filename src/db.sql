CREATE TABLE vacancies(
    id varchar(255),
    name varchar(255),
    employer_url varchar(255),
    area varchar(255),
    salary_from integer,
    salary_to integer,
    avg_salary integer,
    curency varchar(255),
    PRIMARY KEY (id)
);

CREATE TABLE employers(
    id varchar(255),
    name varchar(255),
    PRIMARY KEY (id)
);

ALTER TABLE vacancies ADD COLUMN  employer_id varchar(255) NOT NULL
CONSTRAINT employer_id REFERENCES employers (id)
ON UPDATE CASCADE ON DELETE CASCADE;



