#!/bin/bash

Hex () {
	Calling_Dir=$PWD

	# \/ https://stackoverflow.com/a/246128 \/
	SOURCE="${BASH_SOURCE[0]}"
	while [ -h "$SOURCE" ]; do
		DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
		SOURCE="$(readlink "$SOURCE")"
		[[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
	done
	DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
	# /\ https://stackoverflow.com/a/246128 /\

	if [ $# -eq 2 ]
	then
		python3 $DIR/Hex.py $( realpath  $Calling_Dir/$1 ) "-v"
	else
		if [ $# -eq 1 ]
		then
			if [ $1 = "-v" ]
			then
				python3 $DIR/HexREPL.py "-v"
			else
				python3 $DIR/Hex.py $( realpath $Calling_Dir/$1 )
			fi
		elif [ $# -eq 0 ]
		then
			python3 $DIR/HexREPL.py
		else 
			exit
		fi
	fi

	cd $Calling_Dir
}

export -f Hex