# import logging
#
# import pandas as pd
# import pymysql
# import requests
# import sshtunnel
#
# from project import Project
#
# url = 'https://trackify.onweb.host/'
#
# def open_ssh_tunnel(verbose=False):
#     if verbose:
#         sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG
#     return sshtunnel.SSHTunnelForwarder(
#         ('162.0.217.84', 21098),
#         ssh_username='akbacbqg',
#         ssh_password='RfCf67!344d%F2c7',
#         remote_bind_address=('127.0.0.1', 3306)
#     )
#
# def mysql_connect(tunnel):
#     return pymysql.connect(
#         host='127.0.0.1',
#         user='akbacbqg_trackify1admin',
#         passwd='D7#{j(1&&M@K',
#         db='akbacbqg_trackify1',
#         port=tunnel.local_bind_port
#     )
#
# def execute_query(query,connection):
#     return pd.read_sql_query(query, connection)
#
#
#
# def sign_in(email: str, password: str):
#     tunnel = open_ssh_tunnel()
#     tunnel.start()
#     connection = mysql_connect(tunnel)
#     data_frame = execute_query(connection, 'SELECT * FROM ')
#     response = requests.post(
#         url=url + 'auth/jwt/create/',
#         data={
#             'username': email,
#             'password': password
#         }
#     )
#     try:
#         return response.json()['access']
#     except KeyError:
#         return None
#
#
# def get_projects(user_id: str):
#     response = requests.get(
#         url=url + 'api/projects/?get'
#     )
#     json_formatted = response.json()
#     current_user_data = []
#     for key in json_formatted:
#         if key['user'] == user_id:
#             current_user_data.append(key)
#     return current_user_data
#
#
# def get_my_id(access_token: str):
#     response = requests.get(
#         url=url + 'auth/users/me/',
#         headers={
#             'Authorization': 'JWT ' + access_token
#         }
#     )
#     try:
#         return response.json()['id']
#     except KeyError:
#         return ''
#
#
# def add_new_project(user_id: str, project_name: str):
#     response = requests.post(
#         url=url + 'api/projects/',
#         data={
#             'user': user_id,
#             'name': project_name,
#             'idol': '00:00:00'
#         }
#     )
#     return response.status_code == 200
#
#
# def update_project(project: Project):
#     print(project.presses)
#     response = requests.patch(
#         url=url + 'api/projects/' + str(project.id) + '/',
#         data={
#             'time': project.project_time,
#             'idol': project.project_idol_time,
#             'pressess': project.presses,
#             'clicks': project.clicks
#         }
#     )
#     return response.status_code == 200
#
#
# def update_screenshots(project: Project):
#     responses = []
#     for screenshot in project.screen_shots:
#         screenshot_file = open(screenshot, 'rb')
#         response = requests.post(
#             url=url + 'api/projects/' + str(project.id) + '/screenshots/',
#             files={
#                 'screenshot': screenshot_file
#             }
#         )
#         print(response.content)
#         print(response.status_code)
#         responses.append(response.status_code == 201)
#         screenshot_file.close()
#     return False not in responses
#
