from tornado.web import RequestHandler
import json


class CorrectionHandler(RequestHandler):

    def prepare(self):
        self.auto_correct = self.settings['auto_correct']

    def get(self):
        string = self.get_argument('string')
        response_dict = dict()
        if not string:
            response_dict["none"] = True
            response_dict["results"] = ""
        else:
            response_dict["none"] = False
            words = self.auto_correct.correct(string)
            response_dict["results"] = words

        self.write(json.dumps(response_dict))
