import psycopg2

class Mydatabase():
    def __init__(self, db="eco", user="hmayt", passw="911750750",host="192.168.0.22"):
        self.conn = psycopg2.connect(database=db, user=user, password=passw, host=host)
        self.cur = self.conn.cursor()


    def query(self, query, parameters):
        self.cur.execute(query, parameters)


    def ru(self):
        return self.cur.fetchone()[0]

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
    def commans(self):
        list_queries = ['''
        INSERT INTO search(searchterm) VALUES (%s)
        ON CONFLICT (searchterm)
        DO UPDATE SET searchterm=EXCLUDED.searchterm
        RETURNING idsearch
        '''
        ,
        '''
        INSERT INTO pdates (search)
        VALUES (%s)
        RETURNING datesid;
        ''',
        '''
        WITH sell_key(sellerid) as (
        INSERT INTO seller (name)
        VALUES (%s) ON CONFLICT (name)
        DO UPDATE SET name=EXCLUDED.name
        RETURNING  sellerid
        )
        INSERT INTO product (seller_id, date, Page, rating, link, price, info)
        SELECT  sellerid, %s, %s, %s, %s, %s, %s FROM sell_key;
        ''']
        return list_queries
