"""Use this library to interact with the MADS Scoreboard."""

import os
import requests


BASE_URL = os.environ.get("SCOREBOARD_URL", "https://scoreboard.mads.tools")


class Response:
    """Wrapper around the API response so we can better control when API changes."""

    body: requests.Response
    student_key: str

    def __init__(self, response):
        # If we don't return a 201, we want to make that very well known.
        response.raise_for_status()
        self.body = response.json()
        data = self.body["submission"]
        self.student_key = data["student_key"]


def submit(
    *, course_name: str, api_key: str, board_name: str, student_id: str, score: str
) -> Response:
    """
    Send a student score to the scoreboard API.

    If anonymize is set to True, the student will need to see their returned key in
    order to find themselves on the scoreboard. Make sure to pass this key back to the
    grader.
    """

    response = Response(
        requests.post(
            BASE_URL + "/boards/" + course_name + "/" + board_name,
            json={"student_key": student_id, "score": score},
            auth=(course_name, api_key),
        )
    )

    return response
