# The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
# The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
# Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
# All such material is used with the permission of the owner.
# All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
# All Rights Reserved.

## pylookup setup
if [ -d "./distfiles/pylookup" ]; then
    pushd distfiles/pylookup
    ! test -f "pylookup.db" && python pylookup.py -u python-2.7.1-docs-html
    popd
fi

## yasnipet-bundle
pushd distfiles
test -f ./yasnippet*.el.tgz && ! test -f "./yasnippet-bundle.el" && (echo "yasnppet (el.tgz -> el)"; tar xf yasnippet*.el.tgz)
popd

## install pylint and pep8
command_exist_check(){
! which $1 1>/dev/null && cat <<EOF
 *****\`$1\` is not found*****
    sudo easy_install $1
EOF
}
command_exist_check pylint
command_exist_check pep8
command_exist_check ipdb
command_exist_check reimport
