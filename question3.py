# Knowledge base: Employee data with skills
employees = [
    {"name": "Alice", "skills": ["Python", "Django", "Machine Learning"]},
    {"name": "Bob", "skills": ["JavaScript", "React", "Node.js"]},
    {"name": "Charlie", "skills": ["Java", "Spring", "SQL"]},
    {"name": "David", "skills": ["Python", "Flask", "Data Science"]},
    {"name": "Eva", "skills": ["Java", "Angular", "SQL"]},
]

# Knowledge base: Project data with required skills
projects = [
    {"project_name": "AI Research", "required_skills": ["Python", "Machine Learning", "Data Science"]},
    {"project_name": "Web Development", "required_skills": ["JavaScript", "React", "Node.js"]},
    {"project_name": "Backend Development", "required_skills": ["Java", "Spring", "SQL"]},
    {"project_name": "Data Analysis", "required_skills": ["Python", "Flask", "Data Science"]},
]

# Function to find matching employees for a project based on required skills
def match_employees_to_project(project_name):
    # Find the project in the projects knowledge base
    project = next((p for p in projects if p["project_name"] == project_name), None)
    
    if not project:
        return f"Project '{project_name}' not found."

    required_skills = set(project["required_skills"])
    matched_employees = []

    # Loop through employees to check if they have all required skills for the project
    for employee in employees:
        employee_skills = set(employee["skills"])
        if required_skills.issubset(employee_skills):
            matched_employees.append(employee["name"])
    
    # Return matched employees or indicate no matches
    if matched_employees:
        return f"Employees matched for project '{project_name}': " + ", ".join(matched_employees)
    else:
        return f"No employees match the required skills for project '{project_name}'."

# Main function to get user input and display results
def main():
    # Ask user for the project name
    project_name = input("Enter the project name: ")

    # Find and display the employees matched to the project
    result = match_employees_to_project(project_name)
    print(result)

# Ensure the script runs only when it is executed directly
if __name__ == "__main__":
    main()
