from Main import MainPage
from NewIdea import NewIdea
from SingleIdea import SingleIdea
handlers = [
    ('/', MainPage),
    ('/compose', NewIdea),
    ('/idea/(\d+)', SingleIdea),
]
