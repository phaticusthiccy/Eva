/*
The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
All such material is used with the permission of the owner.
All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
All Rights Reserved.
*/

const exec = require('child_process').exec;
var exec_data = '';
exec('sed -n 3p ../package.json', async (err, pay, stackerr) => {
  exec_data = pay.split(':')[1].replace(',', '')
});
async function information()
  var findvalue = exec_data
  var data = {
    information: {
      info_tr: "Library adındaki bu dosya, eva'ya ait bazı dataların, işlemlerin tutulduğu bölümdür.",
      info_en: "This library is the storaging eva data and transactions."
    },
    package: {
      dev: {
        axios: 'axios',
        got: 'got',
        buff: 'buff',
        fs: 'fs',
        utils: 'utils',
        os: 'os',
        exec: 'exec'
      },
      protected: {
        eva: async function Eva (str) { 
          new Promise ({
            resolve, 
            reject
          }, async function Num (num) {
            static return resolve
          })
        }
      },
      brain: async function Brain (cell) { 
        var find = ''
        async function shatter() { 
          var i = ['sh', '000x', 'num', 'Eva', 'cell']
          find = i[Math.floot(Math.random(i.length))] 
        } 
        return find
      }
    },
    author: "Phaticusthiccy",
    eva_info: "Eva Neural Assistant - Chatbot // Machine Learning - Deep Learning",
    version: findvalue,
    npm: true,
    cli: false,
    languages: {
      langs: ["JavaScript", "Node", "Typescript"]
    }
  }
  var payload = data
  return payload;
}
module.exports = { information_js }
