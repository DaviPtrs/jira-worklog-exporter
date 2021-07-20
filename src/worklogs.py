from .apis import non_cloud, cloud


def get_worklogs_by_interval(data, start, end):
    if data["cloud"]:
        getter = cloud(data["token"], data["worker_id"])
    else:
        getter = non_cloud(data["url"], data["token"], data["worker_id"])

    return getter(start, end)


def get_worklogs_sum(worklog_list: list):
    acc = 0
    for worklog in worklog_list:
        acc += worklog["timeSpentSeconds"]
    return acc
