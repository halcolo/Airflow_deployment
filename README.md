# ETL-flow

* **category**    Data engeneering  📡
* **author**      Juan Diego Alfonso <jalfons.ocampo@gmail.com>
* **copyright**   [GNU General Public Licence](https://www.gnu.org/licenses/gpl.txt)
* **source**  [GitHub](https://github.com/halcolo/ETL-flow.git)


## Description

This is a lab created to understand the process of ETL, and after I pass this process to an AirFlow schedule.

## Virtual enviroment

You can create a virtual environment using following commands.

In linux maybe you need the following package `sudo apt-get install python3-venv`

| Description|Linux| Win|
| ------ | ------ |------|
| Install virtenv| `python3 -m pip install --user virtualenv` |`py -m pip install --user virtualenv`|
| Create enviroment | `python3 -m venv modelTrainerEnv` |`py -m venv modelTrainerEnv`|
| Activate enviroment | `source modelTrainerEnv/bin/activate` |`.\modelTrainerEnv\Scripts\activate`|
| Install packages | `pip install --upgrade -r requirements.txt`  |`pip install --upgrade -r requirements.txt` |
| Inactivate  | `deactivate`  | `deactivate`  |

## USE

The principal files are.

├── bucketlist
    ├── Airflow
    │   ├── main.py
    │   └── flow
    |       └──clean_data.py 
    ├── pipeline.py
    ├── clean_data.txt
    ├── spreadsheet.txt
    └── variables.py

With the three files from root, you can see the classes at 'spreadsheet.py' and 'clean_data.py', and the 'variables.py' have the variables to call the process, please change the variables before run the application, to run you can install the requirements in your virtualEnv or in your localEnv, to run the process at Airflow, just upload the files 'main.py' and 'clean_data.py' located at Airflow Dag's folder, change the variables from the 'clean_data.py'.

| Aplication| Version|
| ------ | ------ |
| Python| `Python 3.6` |
| Pandas| `0.24.2` |
| Pandas_bq| `0.10.0` |
| tqdm| `4.31.1`  |
| Google-apitools| `0.5.26` |
| Google-auth| `1.6.3` |
| Google-auth-httplib2| `0.0.3` |
| Ggoogle-auth-oauthlib| `0.3.0` |
| future| `0.17.1` |
