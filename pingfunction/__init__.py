


import azure.functions as func
import logging
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Ping check initiated.")

    try:
        return func.HttpResponse(
            json.dumps({"status":"service is up!"}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"An error occurred during the ping check: {e}")
        return func.HttpResponse(
            json.dumps({"error": "Ping check failed", "details": str(e)}),
            status_code=500,
            mimetype="application/json"
        )