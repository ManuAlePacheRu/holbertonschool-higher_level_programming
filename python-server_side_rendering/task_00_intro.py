from string import Template
import logging
import os

def generate_invitations(template, attendees):
    
    if not isinstance(template, str):
        logging.error("Error: Template is not a string")

    if not isinstance(attendees, list):
        logging.error("Error: attendees  is not a list of dictionaries")

    if not template.strip():
        logging.error("Error: Template is empty")
    
    if not attendees():
        logging.error("Error: Attendees is empty") 

    inv = []

    for attendee in attendees:
        atendee_data = {key: attendee.get(key, "N/A") for key in attendee}
        new_template = Template.safe_substitute(atendee_data)

        return inv

    def check_make_file(num):
        for idx, inv in enumerate(inv, start=1):
            output_file = f"output_{idx}.txt"
            with open(output_file, 'w') as file:
                file.write(inv)
