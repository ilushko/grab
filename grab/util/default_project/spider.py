#!/usr/bin/env python
# coding: utf-8
from grab.spider import Spider, Task
from grab.tools.logs import default_logging
from grab import Grab
import logging

from database import db

class {{ PROJECT_NAME_CAMELCASE }}Spider(Spider):
    def task_generator(self):
        yield Task('initial', url='')

    def task_initial(self, grab, task):
        pass
