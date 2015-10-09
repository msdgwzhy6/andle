# andle

[![PyPI version](https://badge.fury.io/py/andle.svg)](https://badge.fury.io/py/andle)
[![Build Status](https://travis-ci.org/Jintin/andle.svg?branch=master)](https://travis-ci.org/Jintin/andle)

andle is a command line tool to help you sync android dependencies, sdk or build tool version in gradle base Android projects.

## Installation

Simple install by [pip](http://pip.readthedocs.org/en/stable/installing):

    $ sudo pip install andle

## Usage

The most commonly used command:

    $ andle update -p <path>  [-d dryrun]   # sync project gradle config
    $ andle setsdk -p <path>                # set android sdk path
     
See `andle --help` or `andle <command> --help` for more information.

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/Jintin/andle.

## License

The package is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
