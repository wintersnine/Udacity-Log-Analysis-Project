#!/usr/bin/env python
# log analysis porject udacity

# psycopg2 is a PostgreSQL adapter for the Python programming language
import psycopg2

dbname = "news"


def get_results(query):
    try:
        db = psycopg2.connect(database=dbname)
        c = db.cursor()
        c.execute(query)
        return c.fetchall()
        db.close()
        return results
    except psycopg2.Error as e:
        print(e)
        exit(1)


# what are the most popular three articles of all time?"
query_1 = ('''
    SELECT title, count(*) as views
    FROM articles
    JOIN log ON articles.slug = substring(log.path, 10)
    GROUP BY title
    ORDER BY views DESC LIMIT 3;
          ''')


# who are the most popular article authors of all time?
query_2 = ('''
    SELECT authors.name, count(*) as views
    FROM articles JOIN authors ON articles.author = authors.id
    JOIN log ON articles.slug = substring(log.path, 10)
    GROUP BY authors.name
    ORDER BY views DESC;
          ''')


# on which days did more than 1% of requests lead to errors?
query_3 = ('''
    SELECT * FROM (SELECT date(time),round(100.0*sum(case log.status
    WHEN '200 OK'  then 0 else 1 end)/count(log.status),2) as percentage
    FROM log
    GROUP BY date(time)
    ORDER BY percentage desc) as error_percentage
    WHERE percentage > 1;
          ''')


def print_query_1_answers(query):
    answers = get_results(query)
    print('\n What are the most popular three articles of all time?')
    for title, views in answers:
        print("\t{} - {} views".format(title, views))


def print_query_2_answers(query):
    answers = get_results(query)
    print('\n Who are the most popular article authors of all time?')
    for title, views in answers:
        print("\t{} - {} views".format(title, views))


def print_query_3_answers(query):
    answers = get_results(query)
    print('\n On which days did more than 1% of requests lead to errors?')
    for answer in answers:
        print('\t' + str(answer[0]) + ' - ' + str(answer[1]) + '% errors')


# prints out the resulting three questions and answers
if __name__ == "__main__":
    print_query_1_answers(query_1)
    print_query_2_answers(query_2)
    print_query_3_answers(query_3)
