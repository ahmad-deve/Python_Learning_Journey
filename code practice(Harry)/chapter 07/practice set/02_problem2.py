n = ["Ahmad","Roman","Ameen", "Abdullah","Hamza", "Ali","Faizan"]
for i in n:
    if (i.startswith("A")):
        print(f"Hello  {i}")
    elif(i.startswith("R")):
        print(f"Sr. {i}")
    else:
        print(f"on_inter {i}")