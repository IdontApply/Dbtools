import psycopg2

class Mydatabase():
    def __init__(self, db="eco", user=input('user>'), passw=input('passw>'),host="192.168.0.22"): # todo config host in the config
        self.conn = psycopg2.connect(database=db, user=user, password=passw, host=host)
        self.cur = self.conn.cursor()


    def query(self, query, parameters = None):
        self.cur.execute(query, parameters)


    def fetch1(self):
        return self.cur.fetchone()[0]

    def fetcha(self):
        return self.cur.fetchall()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()

    def cr(self):
        return self.cur

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
        '''
        ,

        '''
        WITH sell_key(sellerid) as (
        INSERT INTO seller (name)
        VALUES (%s) ON CONFLICT (name)
        DO UPDATE SET name=EXCLUDED.name
        RETURNING  sellerid)
        INSERT INTO product (seller_id, date, Page, rating, link, price, info)
        SELECT  sellerid, %s, %s, %s, %s, %s, %s FROM sell_key;
        '''
        ,
        '''
        SELECT * FROM seller
        WHERE totalsales IS NULL
        FETCH FIRST ROW ONLY;
        '''
        ]
        return list_queries
