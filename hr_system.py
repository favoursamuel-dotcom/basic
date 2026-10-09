with open('hr_system.txt') as file:
    next(file)
    for f in file:
        parts = f.strip().split(" ")
        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])
        print(f"{name} (ID: {id_number}), {job_title} - ${salary:.2f}")