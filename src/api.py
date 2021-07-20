from tempoapiclient import client
import requests
import json


def cloud(api_token, accountId):
    tempo = client.Tempo(auth_token=api_token, base_url="https://api.tempo.io/core/3")

    def get_func(start, end):
        worklogs = tempo.get_worklogs(dateFrom=start, dateTo=end, accountId=accountId)
        return worklogs

    return get_func


def non_cloud(url, api_token, accountId):
    auth_header = {"Authorization": f"Bearer {api_token}"}
    session = requests.Session()
    session.headers.update(auth_header)

    def get_func(start, end):
        payload = {"from": start, "to": end, "worker": [accountId]}
        response = session.post(
            f"{url}/rest/tempo-timesheets/4/worklogs/search", json=payload
        )
        return response.json()

    return get_func
