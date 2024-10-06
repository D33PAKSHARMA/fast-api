def get_single_value(data) -> dict:
    if data:
        data["_id"] = str(data["_id"])
    return data

def list_values(data) -> list:
    return [get_single_value(x) for x in data]