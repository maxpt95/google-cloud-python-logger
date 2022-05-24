"""API for testing cloud logging with a Cloud Run Service"""
import logging
import os

import setup_log
import write_in_all_severities

from flask import Flask, request
from flask_restful import Api, Resource
from google.cloud.exceptions import GoogleCloudError
from werkzeug.exceptions import BadRequest


app = Flask(__name__)
api = Api(app)

logger = logging.getLogger(__name__)
setup_log.setup_logging()
setup_log.setup_cloud_logging(logger)
# Pipeline request handlers
class WriteContent(Resource):


    def post(self):
        try:
            data = request.get_json()
            logger.info(data["content"])

            return {"status": "completed"}
        except BadRequest as e:
            logging.exception(
                "400 Bad request error: %s", e.description)
            return {"code": "400", "description": e.description}
        except GoogleCloudError as e:
            return {"code": e.code, "description": e.message}

class WriteOnAllSeverities(Resource):


    def post(self):
        try:
            write_in_all_severities.write()

            return {"status": "completed"}
        except BadRequest as e:
            logging.exception(
                "400 Bad request error: %s", e.description)
            return {"code": "400", "description": e.description}
        except GoogleCloudError as e:
            return {"code": e.code, "description": e.message}

api.add_resource(WriteContent, "/write-content")
api.add_resource(WriteOnAllSeverities, "/write-on-all-severities")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))