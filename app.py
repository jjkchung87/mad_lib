from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

debug = DebugToolbarExtension(app)

"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

prompts = story.prompts


@app.route('/home')
def showStories():
    


@app.route('/form')
def showMadLibForm():
    return render_template('form.html',userPrompts = prompts)

@app.route('/results')
def showResults():
    answers = {}
    for prompt in story.prompts:
        answers[prompt] = request.args[prompt]

    result = story.generate(answers)
    return render_template('/results.html',userStory = result)





    # turn user inputs into a library object
    # pass lib object into story.generate()
    # render_template the result
