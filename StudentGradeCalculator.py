def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 75:
        return 'C'
    else:
        return 'F'

def score_range(score):
    if score >= 90:
        return '90 and 100'
    elif score >= 80:
        return '80 and 89'
    elif score >= 75:
        return '75 and 79'
    else:
        return '0 and 74'

while True:
    try:
        java = float(input("Java Programming Score: "))
        if not (0 <= java <= 100):
            continue
            
        C = float(input("C Programming Score: "))
        if not (0 <= C <= 100):
            continue
            
        Database = float(input("Database Handling Score: "))
        if not (0 <= Database <= 100):
            continue
    except ValueError:
        continue

    total_score = (java + C + Database) / 3
    total_score = round(total_score, 2)

    print(f"Average: {total_score:.2f}")
    print(f"Grade: {grade(total_score)} because the average is between {score_range(total_score)}")

    choice = input("Do you want to continue? (YES/NO): ").strip().upper()
    if choice in ['NO', 'N']:
        print("Program terminated. Thank you!")
        break