from pptx import Presentation
from pptx.util import Inches
import os
import json

import logging
logging.basicConfig(level=logging.INFO)

def create_presentation_from_data(json_data: dict, file_path: str = "presentation.pptx") -> str:
    """
    Create a PowerPoint presentation from the given JSON data.

    :param json_data: A dictionary containing slide data.
    :param file_path: Path to save the generated PowerPoint file.
    :return: Path to the saved PowerPoint file.
    """
    # Initialize a PowerPoint presentation
    presentation = Presentation()

    logging.info("Creating a PowerPoint presentation from the given JSON data...")
    logging.info(f"Formatted Json: {json.dumps(json_data['slides'], indent=2)}")

    # Iterate over the slides in the JSON data
    for slide_data in json_data['slides']:
        ...





    # Save the presentation
    presentation.save(file_path)
    return os.path.abspath(file_path)
