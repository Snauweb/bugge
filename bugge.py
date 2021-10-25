class DB_wrap:
    def __init__(self):
        pass
    
class Bugge:
    def __init__(self):
        self.config_dict = {}
        self.routes = {}
    
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

    ### Requests and routing
    # Decorator used to add route, to create a pattern resembeling flask
    def route(self, route, method):
        def decorator(route_handler):
            self.add_route(route_handler, route, method)
        return decorator
    
    def add_route(self, handler, route, method):
        # Keyed by a concatenation of method and url
        # Only saves the handler function, not the context
        route_key = method + ":" + route
        self.routes[route_key] = handler

    def read_request(self):
        pass
        
    def handle_request(self, route, method):
        route_key = method + ":" + route

        if route_key in self.routes:
            self.routes[route_key](); # Execute handler function
        else:
            self.respond_error("HTML", 404) # Return a 404 not found in html format

    # Reads request paramters with read request, reads payload if the request is POST.
    # Uses the aquired input to handle the request and call the correct response.
    # Not sure what cases this will be able to cover, but a lot of cases should be possible to automate
    def read_and_handle_request(self):
        pass
            
    def extract_url_params(self):
        pass

    ### DB methods
    def read_table(self, table_name):
        pass

    def add_to_table(self, table_name, *cols):
        pass

    ### Response handlers
    def respond_HTML(self, body, status=200):
        header = \
        "Content-type: text/html" + \
        "Status: " + str(status) + "\n\n"
            
        response = header + body
        print(response)

    def respond_JSON(self):
        pass

    def respond_error(self, type, error_code):
        if(type == "HTML"):
            self.respond_HTML("<h1>Error " + str(error_code) + "</h1>", status=404)

    
