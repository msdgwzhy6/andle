#!/usr/bin/env python

import andle.android
import andle.sdk

VERSION = "1.5.2"


def update(path, dryrun, remote, gradle):
	data = sdk.load()
	android.update(path, data, dryrun, remote, gradle)


def setsdk(path):
	sdk.setpath(path)
