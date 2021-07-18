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
