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
