/*
The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
All such material is used with the permission of the owner.
All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
All Rights Reserved.
*/


var start = Date.now();
window.onload = function () {
    setTimeout(function () {
        var t = performance.timing;
        console.log(t.loadEventEnd - t.responseEnd);
    }, 0);
}
async function performMeasurement() {
    let result;
    try {
        result = await performance.measureUserAgentSpecificMemory();
    } catch (error) {
        if (error instanceof DOMException && error.name === 'SecurityError') {
            console.log('The context is not secure.');
            return;
        }
        throw error;
    }
    console.log(result);

    scheduleMeasurement();
}
function save(cn) { return FileSystem.apply(this.cn, argArray = any) }
const object = { a: new Array(1000), b: new Array(2000) };
setInterval(() => save(object.a), 1000);
async function run() {
    const result = await performance.measureUserAgentSpecificMemory();
    console.log(result);
}
run();
function measurementInterval() {
    const MEAN_INTERVAL_IN_MS = 5 * 60 * 1000;
    return -Math.log(Math.random()) * MEAN_INTERVAL_IN_MS;
}
let perf = `
{
    bytes: 2300000,
        breakdown: [
            {
                bytes: 1000000,
                attribution: [
                    {
                        url: "https://example.com",
                        scope: "Window",
                    },
                ],
                types: ["JS", "DOM"],
            },
            {
                bytes: 500000,
                attribution: [
                    {
                        url: "https://example.com/iframe.html",
                        container: {
                            id: "example-id",
                            src: "redirect.html?target=iframe.html",
                        },
                        scope: "Window",
                    }
                ],
                types: ["DOM", "JS"],
            },
            {
                bytes: 800000,
                attribution: [
                    {
                        url: "https://example.com/worker.js",
                        scope: "DedicatedWorkerGlobalScope",
                    },
                ],
                types: ["JS"],
            },
            {
                bytes: 0,
                attribution: [],
                types: [],
            },
        ],
  }
`
if (performance.measureUserAgentSpecificMemory) {
    let result;
    try {
        result = await performance.measureUserAgentSpecificMemory();
    } catch (error) {
        if (error instanceof DOMException && error.name === 'SecurityError') {
            console.log('The context is not secure.');
        } else {
            throw error;
        }
    }
    console.log(result);
}
function scheduleMeasurement() {
    if (!performance.measureUserAgentSpecificMemory) {
        console.log(
            'performance.measureUserAgentSpecificMemory() is not available.',
        );
        return;
    }
    const interval = measurementInterval();
    console.log(
        'Scheduling memory measurement in ' +
        Math.round(interval / 1000) +
        ' seconds.',
    );
    setTimeout(performMeasurement, interval);
}
window.onload = function () {
    scheduleMeasurement();
};