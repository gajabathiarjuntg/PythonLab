def assign_grade(total_score, max_possible):
    percentage = (total_score / max_possible) * 100

    if percentage >= 90:
        return "Outstanding"
    elif percentage >= 75:
        return "Excellent"
    elif percentage >= 50:
        return "Good"
    else:
        return "Fail"
