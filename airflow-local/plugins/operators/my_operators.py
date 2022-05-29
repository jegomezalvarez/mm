#!/usr/bin/env python3

from datetime import datetime

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class TimeDiff(BaseOperator):

    @apply_defaults
    def __init__(self, diff_date: datetime, *args, **kwargs):
        self.diff_date = diff_date
        super(TimeDiff, self).__init__(*args, **kwargs)

    def execute(self, context):
        diff = datetime.now() - self.diff_date
        message = "************** Time difference: {} **************".format(diff)
        print(message)
        return message