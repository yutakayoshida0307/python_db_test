import mysql.connector as mc

class DB:
    def __init__(self):
        self.host = 'localhost' 
        self.port = 3307
        self.user = 'developer'
        self.password = 'password'
        self.database = 'test_db'
        
    def connector(self):
        """
        mysqlの接続コネクター
        :return:
        """
        conn = mc.connect(
            host=self.host,  # バックエンドのIP
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            auth_plugin='mysql_native_password'
        )
        return conn

    def select_query(self, query, is_dict=True):
        """
        select文を実行する。
        :param query: 実行するquery
        :param is_dict: Trueの場合、dict型で結果を返す。
        :return:
        """
        conn = self.connector()
        if is_dict:
            cur = conn.cursor(dictionary=True)
        else:
            cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    def exec_query(self, query):
        """
        insert文、update文を実行する。
        :param query: クエリ
        :return: None
        """
        conn = self.connector()
        cur = conn.cursor()
        try:
            cur.execute(query)
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()
        return

