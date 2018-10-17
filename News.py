import psycopg2

DBNAME = "news"


def run_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    posts = c.fetchall()
    db.close()
    return posts


def get_top_articles():
    """Top 3 most popular articles"""

    # Query String
    query = """
        select articles.title, count(*) as views
        from articles join log
        on log.path like concat('/article/%',articles.slug)
        group by articles.title order by views desc limit 3;
    """

    # Run Query
    results = run_query(query)

    # Results
    print('\nTop three articles:')
    count = 1
    for i in results:
        number = '(' + str(count) + ') "'
        title = i[0]
        views = '" with ' + str(i[1]) + " views"
        print(number + title + views)
        count += 1


def get_top_article_authors():
    """Top 3 most popular authors"""

    # Query String
    query = """
        select authors.name, count (*) as views
        from authors join articles
        on authors.id= articles.author
        join log on log.path like concat('/article/%', articles.slug)
        group by authors.name order by views desc limit 3;
    """

    # Run Query
    results = run_query(query)

    # Results
    print('\nTop three authors:')
    count = 1
    for i in results:
        print('(' + str(count) + ') ' + i[0] + ' with ' + str(i[1]) + " views")
        count += 1


def get_days_with_errors():
    """Days with more than 1% errors"""

    # Query String
    query = """
         select sum day, round((errors.error*1.0) / sum.requests) as perc
         from (select date_trunc( 'day', time) "day", count(*) as error
         from log where status != '200 OK' group by day ) as errors
         join ( select date_trunc('day' ,time) "day", count(*) as requests
         from log group by day) as sum on sum.day = errors.day
         where (round((errors.error*1.0) / sum.requests) > 0.01)
         order by perc desc ;
    """

    # Run Query
    results = run_query(query)

    # Results
    print('\nDays with more than 1% errors:')
    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print(date + " -- " + errors)

print('Log Results:\n')
get_top_articles()
get_top_article_authors()
get_days_with_errors()
