# sentence-url

A port of the NPM package [readable-url](https://github.com/sharadbhat/ReadableURL) to generate readable random phrases to add to dynamically generated URLs.

[GitHub repository](https://github.com/Jabbey92/sentence-url)

To generate readable URLs like Twitch's clips.

Example: https://clips.twitch.tv/WiseAcceptableSnoodPupper

## Get started

To install:

    pip install readable-url

To import:

    from sentence-url import SentenceURL

## Usage Instructions

    """
    Takes 3 parameters.
    1. An integer value - The number of words to be generated in the string. (Between 2 and 10).
    2. A boolean value - If true, returns string in CamelCase, else lowercase.
    3. A string - The seperator between the words.
    """

    generator = SentenceURL() # 3, True, '' are the default values.

    #generator = SentenceURL(False, 5, '-') # Other options.

To generate a random phrase:

    url = generator.generate()
    print(url); # Prints out 'ForgetfulHarshEgg'


This can be used to add to the end of a URL.

Example: https://example.com/photos/ForgetfulHarshEgg

For best results, use an integer value of 3, 4, or 5.
