
diseases = {

    "Flu": (["fever", "cough", "sore throat"], "Rest and drink fluids."),
    "Cold": (["sneezing", "runny nose"], "Stay warm and use cold medicine."),
    "Malaria": (["fever", "chills"], "Visit a doctor and take antimalarial medicine."),
    "COVID-19": (["fever", "cough", "loss of taste"], "Isolate and consult a doctor.")
}

def find_disease(symptoms):

    result = ""

    for name, (symptom_list, treatment) in diseases.items():
        if any(s in symptom_list for s in symptoms):
            result += f"\n{name}: {treatment}"

    return result if result else "No matching disease found."

# Input from user
symptoms_input = input("Enter symptoms (comma-separated): ").lower()

symptom_list = [s.strip() for s in symptoms_input.split(",")]


print(find_disease(symptom_list))
