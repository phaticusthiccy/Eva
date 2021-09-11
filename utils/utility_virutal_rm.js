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
