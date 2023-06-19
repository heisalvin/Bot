import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "live your best moments"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response