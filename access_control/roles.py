def filter_fields(role: str, record: dict) -> dict:
    if role == "H":
        return record

    if role == "R":
        record = dict(record)  # copy
        record.pop("first_name", None)
        record.pop("last_name", None)
        return record

    raise ValueError("Unknown role")
