import json
import logging
import requests

def add_ifbid_vehicles(details):
    data = {
        "Name":"test",
        "VIN": details.get("Vin"),
        "Make": details.get("Make"),
        "Model": details.get("Model"),
        "Price": details.get("Reserve Price"),
        # "Seller_ID": details.get("Consigner"),
        # "vehicle_url": details.get("Vehicle URL"),
        "Year": details.get("Vehicle Year"),
        "Mileage": details.get("Odometer Amount"),
        "Trim": details.get("Trim"),
        "Declarations": details.get("Vehicle Declarations"),
        # "vehicle_description": details.get("Vehicle Description"),
        # "vehicle_condition_score": details.get("Vehicle Condition Score"),
        # "vehicle_capture_type": details.get("Vehicle Capture Type"),
        "Carfax_URL": details.get("Carfax_URL"),
        "Carfax": details.get("Carfax_Odo"),
        "Vehicle_Image_Url": "//example.com",#details.get("Image_Link"),
        "Source":"IN_IFBID"
    }
    url = "https://bubble-service-major.azurewebsites.net/api/register-vehicle-lead?code=Pc80TXSbJT1UL5dmCcZJmFWndDQLKT8-2oqxkK43PgEAAzFuBPsS-A%3D%3D"

    response = requests.post(url,data=data )
    logging.info(response.json())

    # apis.VehicleApi.add_vehicle_into_crm(access_token,data)
    pass


def update_vehicle_status(details):
    new_status = details.get("InStatus")
    vin = details.get("Vin")

    url = "https://bubble-service-major.azurewebsites.net/api/vehicle-update?code=NWFfiNpmUBfEQaW-YfzRz3wjusFP1Z_RC683eEP9BWH0AzFuIcWS4Q%3D%3D"
    data = {
        "data":
            [
                {
                    "Vin":vin,
                    "Status":new_status
                }
            ]

        }
    response = requests.post(url,json=data)
    logging.info(response.json())


def main(changes):
    logging.info("SQL Changes: %s", json.loads(changes))
    changes = json.loads(changes)
    #operation 0 means insert
    for change in changes:
        if change['Operation'] == 0:
            add_ifbid_vehicles(change['Item'])

        elif change['Operation'] == 1:
            update_vehicle_status(change['Item'])
            
    #operation 1 means update
    #operation 2 means delete


