#  Copyright (c) CONTEXTMACHINE 2022.
#  AEC, computational geometry, digital engineering and Optimizing construction processes.
#
#  Author: Andrew Astakhov <sthv@contextmachine.space>, <aa@contextmachine.ru>
#
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the
#  Free Software Foundation; either version 2 of the License, or (at your
#  option) any later version.  See http://www.gnu.org/copyleft/gpl.html for
#  the full text of the license.
#
#
import os

import boto3

os.environ.setdefault("STORAGE", "https://storage.yandexcloud.net/")



class WatchSession(object):
    storage = os.environ["STORAGE"]

    def __init__(self, bucket=None, **kwargs):
        self.session = boto3.session.Session(**kwargs)
        super().__init__()
        self.bucket = bucket


class S3Session(WatchSession):
    def __init__(self, bucket=None, **kwargs):
        super().__init__(bucket, **kwargs)
        self.s3 = self.session.client(
            service_name='s3',
            endpoint_url=self.storage
        )
