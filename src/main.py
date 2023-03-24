from functions import *
import yaml

# Open the config.yml file and load its contents into the 'config' variable
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

dashboards = getDashboardsDetails(host=config["host"], api_key=config["api_key"])

for dashboard in config["dashboards"]:
    updateDashboardFieldOverrides(host=config["host"], api_key=config["api_key"], dashboardUid=dashboard["uid"], dashboardFolderUid=dashboard["folderUid"], dashboardFieldOverrides=dashboard["fieldOverrides"], colorPalette=config["colorPalette"])