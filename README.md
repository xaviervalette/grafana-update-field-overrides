# Grafana update field overrides


## What is it ?
Python script to update field overrides on Grafana Dashboards via API

<table>
<tr>
<th width="800px"> Before </th> <th width="800px"> After </th>
</tr>
<tr>
<td>

<img width="612" alt="image" src="https://user-images.githubusercontent.com/28600326/227658919-f456d47c-9feb-40b1-8969-59fa332de0fc.png">

</td>
<td>
    
<img width="612" alt="image" src="https://user-images.githubusercontent.com/28600326/227658933-dd3b79b2-88db-4b8a-86a4-36de869d3592.png">
    
</td>
</tr>
</table>


## Prerequisites
- Grafana Dashboard
- Grafana API key
- List of field to overrides with the new value

## Get started
1. Clone or download this repo
```console
git clone https://github.com/xaviervalette/grafana-update-field-overrides
```
2. Install required packages
```console
python3 -m pip install -r requirements.txt
```
3. Add a ```config.yml``` file as follow:
```diff
└── meraki-network-event-log-collector/
+   ├── config.yml
    ├── ressources
    │   └── fieldOverrideTemplate.json
    └── src/
        ├── functions.py
        └── main.py  
```
4. In the ```config.yml``` file, add the following variables:
```yaml
#config.yml
---
api_key: "<grafanaApiKey>"
host: "<grafanaHost>"
dashboards:
- uid: "<firstDashboardUid>"
  folderUid: "<firstDashboardFolderUid>"
  fieldOverrides:
  - mac: "<firstField>"
    name: "<firstFieldTargetName>"
#[...]
  - mac: "<lastField>"
    name: "<lastFieldTargetName>"
#[...]
- uid: "<lastDashboardUid>"
  folderUid: "<lastDashboardFolderUid>"
  fieldOverrides:
  - mac: "<firstField>"
    name: "<firstFieldTargetName>"
#[...]
  - mac: "<lastField>"
    name: "<lastFieldTargetName>"
colorPalette:
- "#DFFF00"
#[...]
...

```
> ⓘ You can add as many colors you want in the ```colorPalette``` list. Those colors will be use to override sequentially the field color

5. Now you can run the code by using the following command:
```console
python3 src/main.py
```

## Output
The output should be as followed:
```console
Dashboard <firstDashboardUid> overrides updated successfully
[...]
Dashboard <lastDashboardUid> overrides updated successfully
```
Example:
```console
Dashboard UdGt5bb4z overrides updated successfully
Dashboard ynTKlg-Vz overrides updated successfully
```
