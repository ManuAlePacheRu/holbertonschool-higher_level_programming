from string import Template
import logging
import os

def generate_invitations(template, attendees):
    
    if not isinstance(template, str):
        print(type(template).__name__)
        return
    if not isinstance(attendees, list):
        print(type(attendees).__name__)
        return
    for element in attendees:
        if not isinstance(element, dict):
            print(type(element).__name__)
            return

    if not template.strip():
        print("Error: Template is empty")
        return

    if not attendees():
        print("Error: Attendees is empty") 
        return
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
