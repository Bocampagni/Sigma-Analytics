var fs = require('fs');
const express = require('express')
const app = express()
const port = 3000
var cors = require('cors')
var hbs = require('nodemailer-express-handlebars');

app.use(cors())

app.get('/getJson', (req, res) => {
    fs.readFile('data.json', 'utf8', function (err, data) {
        if (err) throw err;
         res.send(JSON.parse(data));
      });
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})


//Mudar para uma pasta separada
var nodemailer = require('nodemailer');


var transporter = nodemailer.createTransport({
  service: 'gmail',
  port: 587,
  secure: false,
  auth: {
    user: process.env.EMAIL,
    pass: process.env.PASSWORD
  }
});

// Step 2
transporter.use('compile', hbs({
  viewPath: './views/', 
  extName: '.hbs'
}));




// Step 3
let mailOptions = {
  from: process.env.EMAIL,
  to: 'a.bocampagni@gmail.com',
  subject: 'Your daily stock market data analysis report is ready.',
  template: 'index',
};

transporter.sendMail(mailOptions, (err, data) => {
  if (err) {
      return console.log('Error occurs' + err);
  }
  return console.log('Email sent!!!');
});




