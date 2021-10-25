class DB_wrap:
    def __init__(self):
        pass


class Bugge:
    def __init__(self):
        self.config_dict = {}
    
    def read_config(self, url):
        config_file_handle = open(url, 'r')
        config_file_lines = config_file_handle.readlines()

        for line in config_file_lines:
            # Ignore empty lines and lines starting with "#" (comments)
            if(len(line) == 0 or line[0] == "#"):
                continue

            line = line.replace(' ', '').replace('\t', '')
            
            [key, value] = line.split("=")
            value = value.strip('\n')
            self.config_dict[key] = value
        
        config_file_handle.close()
        pass

    def read_environment(self):
        pass

    def add_route(self, route, method, function):
        pass

    def route(self, url, method):
        pass

    def extract_url_params(self):
        pass

    def read_table(self, table_name):
        pass

    def add_to_table(self, table_name, *cols):
        pass

    def respond_HTML(self):
        pass

    def respond_JSON(self):
        pass

    
