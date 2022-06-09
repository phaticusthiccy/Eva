/*
The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
All such material is used with the permission of the owner.
All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
All Rights Reserved.
*/


async function array_q(data) {
  if (!data) { throw new Error ('Missing Data!') } 
  var data_pay = '';
  var array_c = 0;
  var array_f = data.split('')
  array_c = array_f.length 
  function custom(length, current) {
    current = current ? current : '';
    return length ? custom(--length, `${data}` + 'EVA'.charAt(Math.floor(Math.random() * array_c)) + current) : current;
  }
  data_pay = custom(16)
  var scheme = {
    data: {
      count: array_c,
      text: data,
      output: data_pay
    },
    author: 'Phaticusthiccy'
  };
  return scheme;
}
