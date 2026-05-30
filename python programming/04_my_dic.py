first_person = {"name":"Ahmad","age":20,"passion":"computer"}
print(f"This person name is {first_person.get("name")} and He is {first_person.get("age")}. His interset in {first_person.get("passion")}.")

if "name" in first_person:
    print("name is persent in first_person")

first_person["name"] = "lahore"
print(first_person.get("name"))

removed_value = first_person.pop("age")
print(removed_value)