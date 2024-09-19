import json
import logging
import requests

def add_ifbid_vehicles(details):
    try:
        name = f"{details.get('Year', '')} {details.get('Make', '')} {details.get('Model', '')} {details.get('Trim', '')} - {details.get('Odometer Amount', '')} - {details.get('Vin', '')}"

        data = {
            "Name":name,
            "VIN": details.get("Vin"),
            "Make": details.get("Make"),
            "Model": details.get("Model"),
            "Auction_Date": details.get("Auction Date"),
            "Price": details.get("Reserve Price"),
            "SellerName": details.get("Consigner"),
            "Auction_URL": details.get("Auction Item Id"),
            "Year": details.get("Vehicle Year"),
            "Mileage": details.get("Odometer Amount"),
            "Trim": details.get("Trim"),
            "Declarations": details.get("Vehicle Declarations"),
            "VehicleDescription": details.get("Vehicle Description"),
            "VehicleConditionScore": details.get("Vehicle Condition Score"),
            "VehicleCaptureType": details.get("Vehicle Capture Type"),
            "Carfax_URL": details.get("Carfax_URL"),
            "Vehicle_Image_Url": "//example.com",#details.get("Image_Link"),
            "Source":"IN_IFBID"
        }
        url = "https://bubble-service-major.azurewebsites.net/api/register-vehicle-lead?code=Pc80TXSbJT1UL5dmCcZJmFWndDQLKT8-2oqxkK43PgEAAzFuBPsS-A%3D%3D"

        response = requests.post(url,data=data )
        logging.info(response.json())
    
    except Exception as e:
        logging.error(f"An error occurred during the vehicle registration: {e}")

def update_vehicle_status(details):
    try:
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
    except Exception as e:
        logging.error(f"An error occurred during the vehicle status update: {e}")


def delete_vehicle(details):
    try:
        vin = details.get("Vin")
        data = {
            "data" : [
                {
                "Vin":vin
                }
            ]
        }
        url = "https://bubble-service-major.azurewebsites.net/api/vehicle-delete?code=duroxFxv3kfBGDqPyrN9_lzIgTkvsMj2QpIzGVEdRafbAzFuU3ht1Q%3D%3D"
        response = requests.post(url,json=data)
        logging.info(response.json())

    except Exception as e:
        logging.error(f"An error occurred during the vehicle deletion: {e}")

def main(changes):
    logging.info("SQL Changes: %s", json.loads(changes))
    changes = json.loads(changes)
    #operation 0 means insert
    for change in changes:
        if change['Operation'] == 0:
            add_ifbid_vehicles(change['Item'])

        elif change['Operation'] == 1:
            update_vehicle_status(change['Item'])

        elif change['Operation'] == 2:
            delete_vehicle(change['Item'])
            
    #operation 1 means update
    #operation 2 means delete


