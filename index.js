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


