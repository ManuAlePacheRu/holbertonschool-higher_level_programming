from string import Template
import os

def generate_invitations(template, attendees):
    
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return
    if not isinstance(attendees, list):
        print("Error: attendees  is not a list of dictionaries")
        return
    if not template.strip():
        print("Error: Template is empty")
        return

    if not attendees:
        print("Error: Attendees is empty") 
        return

    def check_make_file(template):
        # TODO: RESCRIBIR
        for idx in te:
            output_file = f"output_{idx}.txt"
        # TODO: RESCRIBIR
        with open(output_file, 'w') as file:
            file.write(template)

    for attendee in attendees:
        my_template = Template(template)
        atendee_data = {key: attendee.get(key, "N/A") for key in attendee}
        new_template = my_template.safe_substitute(atendee_data)
        check_make_file(new_template)
