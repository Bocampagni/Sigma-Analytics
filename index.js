const csv = require('csv-parser');
const fs = require('fs');

async function getData() {
    const results = [];
    fs.createReadStream('stockData.csv')
        .pipe(csv())
        .on('data', (data) => results.push(data))
        .on('end', () => {
           //Alguma função externa que precise do results
        });
}