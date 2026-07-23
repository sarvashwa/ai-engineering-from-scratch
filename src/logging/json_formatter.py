import json
import logging
from datetime import datetime

class JsonFormatter(logging.Formatter):

    def format(self, record: logging.LogRecord) -> str:

        log = {
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "request_id": getattr(record, "request_id", "-"),
            "message": record.getMessage(),
        }

        return json.dumps(log)