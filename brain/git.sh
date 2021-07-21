#!/bin/bash

install_with_git(){
## install_with_git <name> <url>
    if [ -d $1 ]; then
	echo "Directory \`$1\` already there; not retrieving." 1>&2

    else
	git clone $2
    fi
}

srcs=`cat ./sources.txt`

pushd ./distfiles

for i in $srcs; do wget -nc $i 2>/dev/null; done
#install pylookup adhoc follow-up
install_with_git pylookup http://github.com/tsgates/pylookup.git 2>/dev/null

popd
