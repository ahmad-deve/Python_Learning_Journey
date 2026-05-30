def https_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknow status"
print(https_status(200))