import sys

CONFIG_FILE_URL = "../configMysql.txt"
LIB_DIR = "./bugge"

sys.path.append(LIB_DIR)
from bugge import Bugge
from bugge import DB_wrap

def setup_routes(app):
    app.read_config(CONFIG_FILE_URL)
    
    @app.route("/hallo", "GET")
    def say_hello():
        app.respond_JSON({"message": "Halla", "numbers": [1,3,5,2]})

    @app.route("/frukt", "GET")
    def show_fruit():
        fruits = app.read_table("frukt");
        print(fruits)
        app.respond_JSON({"message": "All the fruits!"})

    @app.route("/forslag", "GET")
    def show_suggestions():
        print("Showing suggestions")
        cursor_rows = app.get_DB_cursor()
        query_rows = "SELECT * FROM suggestion"
        cursor_rows.execute(query_rows);
                
        cursor_cols = app.get_DB_cursor()
        query_cols = "SHOW COLUMNS FROM suggestion"
        cursor_cols.execute(query_cols)
        
        app.respond_JSON(result)
        cursor_cols.close()
        cursor_rows.close()

def main():
    bugge_app = Bugge()
    bugge_app.read_config(CONFIG_FILE_URL)
    bugge_app.init_DB()

    setup_routes(bugge_app)

    request_url = "/forslag";
    request_method = "GET"
    
    bugge_app.route_request(request_url, request_method)

if(__name__ == "__main__"):
    main()
