"""Definition of Saga objects and subsequent objects.

"""

import os
import re
import glob
from dataclasses import dataclass

from . import commons
from .commons import REG_CHAPTER, REG_CHARACTER, TEMPLATE_PATH, UNPARSABLES
from .parse_line import parse_line


@dataclass
class Saga:
    uid:str
    name:str
    episodes:tuple

    def __init__(self, name:str):
        self.uid = name
        self.name = commons.SAGA_NAME[name]
        self.__load(name)

    def __call__(self, name:str):
        raise NotImplementedError('TODO')

    def __load(self, name:str):
        # TODO: pkg_resources to embed data in package
        path = TEMPLATE_PATH.format(saga_name=name)
        def filenames() -> [str]:
            for fname in glob.glob(path + '*.html'):
                if fname not in UNPARSABLES:
                    yield fname
        def build_episodes():
            # print('TARGET:', path + '*.html')
            for idx, fname in enumerate(filenames(), start=1):
                # print('FILE:', fname)
                with open(fname) as fd:
                    yield Episode.build_from(fd.readlines(), number=idx)
        self.episodes = tuple(build_episodes())




@dataclass
class Episode:
    number:int
    title:str
    chapters:tuple


    @staticmethod
    def build_from(lines:[str], number:int=0) -> object:
        """Build an Episode instance from given file lines"""
        have_chapter = any(REG_CHAPTER.fullmatch(line.strip()) for line in lines)
        lines = iter(lines)
        # get title, and waste the next line, that should be empty
        title = next(lines).strip()
        empty = next(lines).strip()
        assert not empty, f"an empty line should follow any episode title, not '{empty}' !"
        if have_chapter:
            chapters = Chapter.build_from(lines)
        else:  # make a phony chapter, populate it with all text
            chapters = [Chapter(1, '', tuple(Line.build_from(lines)))]
        return Episode(number, title, tuple(chapters))



@dataclass
class Chapter:
    number:int
    title:str
    lines:tuple


    @staticmethod
    def build_from(lines:[str]) -> [object]:
        """Build Chapter instances from given file lines"""
        lines = iter(lines)
        while True:
            try:
                line = next(lines).strip()
            except StopIteration:
                break
            match = REG_CHAPTER.match(line)
            if match:  # new chapter
                number, title = match.groups(0)
                next_line = next(lines).strip()
                if next_line:  # not an empty line !
                    print(f"ERROR: an empty line should follow any chapter, not '{next_line}' !")
                line_objects = tuple(Line.build_from(lines))
                yield Chapter(number, title, line_objects)
            else:  # WTF
                raise ValueError(f"Unexpected line found during building a chapter: '{line}'")


@dataclass
class Line:
    character:str
    content:str
    refs:dict


    @staticmethod
    def build_from(lines:[str]) -> [object]:
        """Build Line instances from given lines"""
        lines = iter(lines)
        current_line = None
        while True:
            try:
                line = next(lines).strip()
            except StopIteration:
                break
            if not line: break
            if REG_CHARACTER.match(line):  # new line
                if current_line:
                    yield current_line
                try:
                    character, content, refs = parse_line(line)
                except TypeError:  # parse_line returned None ?!
                    print(f"ERROR: parse_line didn't parse '{line}'")
                current_line = Line(character.strip(), content.strip(), refs)
            else:  # continuation of previous line
                # print('CURRENT LINE:', current_line)
                # print('            :', line)
                current_line.content += '\n' + line
        if current_line:
            yield current_line
