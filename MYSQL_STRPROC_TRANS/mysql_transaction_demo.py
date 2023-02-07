from mysql.connector import Error
from hcl_database_connection import MysqlDatabaseConnection
class HclPythonTransaction(MysqlDatabaseConnection):
    def execute_transaction_query(self):
        cust_id=1
        sql="delete from customer where cust_id=%s"
        try:
            self.cursor.execute(sql,(cust-id))
            self.connection.commit()
        except:
            self.connection.rollback()
            print("Something goes wrong")
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
connect_obj=HclPythonTransaction()
connect_obj.connect("localhost","root","MaHi@2623","hcl_vijayawada")
connect_obj.execute_transaction_query()
