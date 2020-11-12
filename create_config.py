import json
import os

try: 
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

config = {
    "data": {
        "weight_start_date"             : "01/01/2016",
        "sleep_start_date"              : "01/01/2016",
        "rhr_start_date"                : "01/01/2016",
        "monitoring_start_date"         : "01/01/2016",
        "download_days"                 : 31,
        "download_latest_activities"    : 10000,
        "download_all_activities"       : 10000,
        "download_days_overlap"         : 3
    }
}

config["credentials"] = {
        "user" : os.getenv('garmin_username'),
        "password": os.getenv('garmin_password')
    }

with open('GarminConnectConfig.json', 'w') as f:
    f.write(json.dumps(config, indent=4))