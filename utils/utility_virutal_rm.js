/*
The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
All such material is used with the permission of the owner.
All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
All Rights Reserved.
*/


function passError(callback) {
    return function (reason) {
        setImmediate(function () {
            callback(reason);
        });
    };
}

function passValue(callback) {
    return function (value) {
        setImmediate(function () {
            callback(null, value);
        });
    };
}
function indexValue(callback, run) {
    return function (value) {
        setImmediate(function () {
            runs = run == 0 || run == '0' ? 1 : Number(run)
            while (runs > 0) {
                runs = runs - 1
                callback(null, value);
            }
        });
    };
}
