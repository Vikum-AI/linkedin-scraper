const scrapedin = require('scrapedin');
const csvWriter = require('csv-writer');
const dotenv = require('dotenv')
const fs = require('fs')

// function getCookies()   {
//     import cookie from './cookies'
// }

const options = {
    email:  process.env.EMAIL,
    password: process.env.PASSWORD, 
    isHeadless: false
}


let link = 'https://www.linkedin.com/in/satyanadella/'


async function getProfile() {
    const profileScraper = await scrapedin(options)
    .then( (profileScraper) => profileScraper(link) ) 
    .then((profile) => console.log(profile))
}


getProfile()



