# The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
# The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
# Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
# All such material is used with the permission of the owner.
# All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
# All Rights Reserved.

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
