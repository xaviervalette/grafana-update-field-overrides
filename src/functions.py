import json
import requests

def generateOverrides(deviceList, colorPalette):
    overrides = []
    with open('ressources/fieldOverrideTemplate.json', 'r') as f:
        overrideTemplate = json.load(f)
    i = 0
    for device in deviceList:
        try:
            color = colorPalette[i]
        except:
            color = "#049fd9"
        overrideTemplate["matcher"]["options"] = device["mac"]
        overrideTemplate["properties"][0]["value"] = device["name"]
        overrideTemplate["properties"][1]["value"]["fixedColor"] = f"{color}"
        overrides.append(json.loads(json.dumps(overrideTemplate)))
        i = i + 1
    print(overrides)
    return overrides

def getDashboardsDetails(host, api_key):
    url = f"http://{host}/api/search"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "text/plain; charset=utf-8",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, data={})

    dashboards = []

    for dashboard in response.json():
        try:
            dashboards.append({"uid":dashboard["uid"], "folderUid":dashboard["folderUid"]})
        except:
            try:
                dashboards.append({"uid":dashboard["uid"], "folderUid":""})
            except:
                print("Error in dashboard")
    return dashboards

def updateDashboardFieldOverrides(host, api_key, dashboardUid, dashboardFolderUid, dashboardFieldOverrides, colorPalette):
    # Define the API endpoint URL
    endpoint_url = f'http://{host}/api/dashboards/uid/{dashboardUid}'

    # Define the API headers with the Grafana API key
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}

    # Send a GET request to retrieve the dashboard configuration
    response = requests.get(endpoint_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Retrieve the dashboard configuration JSON
        dashboard_config = response.json()['dashboard']

        overrides = []
        overrides = generateOverrides(dashboardFieldOverrides, colorPalette)

        for panel in dashboard_config["panels"]:
            try:
                panel["fieldConfig"]["overrides"]=overrides
            except:
                print("No fieldConfig in panel")
        
        response = requests.post("http://10.142.78.4:3000/api/dashboards/db", headers=headers, json={'dashboard': dashboard_config, 'folderUid': dashboardFolderUid, 'overwrite': True})
        
        # Check if the request was successful
        if response.status_code == 200:
            print(f'Dashboard {dashboardUid} overrides updated successfully')
        else:
            print(f'Error updating dashboard {dashboardUid} overrides')
    else:
        print(f'Error retrieving dashboard {dashboardUid} configuration')