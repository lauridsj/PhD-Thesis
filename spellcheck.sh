#!/bin/bash

aspell -d en_US -t --add-tex-command "cref op" --add-tex-command "Cref op" --add-tex-command "citere op" --add-tex-command "citeres op" --extra-dicts ./aspell-dictionary.txt -c ${1}