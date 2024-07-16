import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return
    if not isinstance(attendees, list):
        print("Error: attendees is not a list of dictionaries")
        return
    if not template.strip():
        print("Error: Template is empty")
        return
    if not attendees:
        print("Error: Attendees is empty")
        return
    
    with open('template.txt', 'r') as f:
        temp_base = f.read()
    
    output_directory = 'output_files/'
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for idx, person in enumerate(attendees):
        get_name = person.get("name") if person.get("name") else "N/A"
        get_event = person.get("event_title") if person.get("event_title") else "N/A"
        get_date = person.get("event_date") if person.get("event_date") else "N/A"
        get_location = person.get("event_location") if person.get("event_location") else "N/A"

        name_rep = temp_base.replace("{name}", get_name)
        event_rep = name_rep.replace("{event_title}", get_event)
        date_rep = event_rep.replace("{event_date}", get_date)
        loc_rep = date_rep.replace("{event_location}", get_location)
        
        output_filename = f'output_{idx}.txt'
        output_path = os.path.join(output_directory, output_filename)
        
        with open(output_path, 'w') as file:
            file.write(loc_rep)