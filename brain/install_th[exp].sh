#!/bin/bash
. ./download.sh

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
