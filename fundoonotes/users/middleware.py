from tabulate import tabulate
from loghandler import logger


class JSONTranslationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.num_exceptions = 0
        self.num_windows = 0
        self.num_mac = 0
        self.num_iPhone = 0
        self.num_Android = 0
        self.other_os = 0
        self.num_postman = 0

    def stats(self, os_info):
        if "Windows" in os_info:
            self.num_windows += 1
            os = "Windows"
        elif "mac" in os_info:
            self.num_mac += 1
            os = "mac"
        elif "iPhone" in os_info:
            self.num_iPhone += 1
            os = "iPhone"
        elif "Android" in os_info:
            self.num_Android += 1
            os = "Android"
        elif "PostmanRuntime" in os_info:
            self.num_postman +=1
            os = "PostmanRuntime"
        else:
            self.other_os += 1
            os = "other"

        self.capture_user_data(os)

    def __call__(self, request):
        self.path = request.path
        self.host = request.headers['Host']
        self.method = request.META['REQUEST_METHOD']
        if "admin" not in request.path:
            self.stats(request.META['HTTP_USER_AGENT'])
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        self.num_exceptions += 1
        print(f'Exception count: {self.num_exceptions}')

    def capture_user_data(self,os):
        datasets = {"Windows":{'OS': os, 'os visit count': self.num_windows, 'method name': self.method, "Path": self.path, "Host ": self.host},
                    "mac":{'OS': os, 'os visit count': self.num_mac, 'method name': self.method, "Path": self.path, "Host ": self.host},
                    "other":{'OS': os, 'os visit count': self.other_os, 'method name': self.method, "Path": self.path, "Host ": self.host},
                    "iPhone": {'OS': os, 'os visit count': self.num_iPhone, 'method name': self.method, "Path": self.path, "Host ": self.host},
                    "Android": {'OS': os, 'os visit count': self.num_Android, 'method name': self.method,"Path": self.path, "Host ": self.host},
                    "PostmanRuntime": {'OS': os, 'os visit count': self.num_postman, 'method name': self.method,"Path": self.path, "Host ": self.host},
                    }
        datasets.get(os)
        dataset = [datasets.get(os)]

        header = dataset[0].keys()
        rows = [x.values() for x in dataset]
        print(tabulate(rows, header, tablefmt='rst'))
        logger.info(tabulate(rows, header, tablefmt='rst'))
