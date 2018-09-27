"""Main TODO

"""
from . import rda


if __name__ == '__main__':
    for episode in rda.episodes:
        if episode.title == "L'enrôlement":
            print(episode.chapters[0].lines[0].content)
            print(episode.chapters[0].lines[2].content)
