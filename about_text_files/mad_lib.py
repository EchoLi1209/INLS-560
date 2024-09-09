# Mad lib (example for functions
def madlib(adjective_1, noun_1, adjective_2, adverb_1, noun_2, noun_3, adverb_2):
    '''Mad lib function'''

    story = f'''
Once upon a time, there was a {adjective_1} puppy named {noun_1} . This puppy was unlike any other in the town because of its {adjective_2} fur that shined under the sunlight. Every day, the puppy would {adverb_1} wag its tail as it greeted everyone who walked by. People would stop to give it a {noun_2} , and it would always respond with a cheerful bark. One day, the puppy decided to explore the {noun_3} that was at the end of the street. It ventured out {adverb_2}.
'''
    return story

output_story = madlib('lovely', 'Jack', 'nice', 'happily', 'hug', 'garden', 'bravely')
print(output_story)
