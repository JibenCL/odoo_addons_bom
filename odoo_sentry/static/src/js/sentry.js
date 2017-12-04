$(function() {
console.log("configuring raven");
Raven.config('https://45c53506a3c04806abfca0efb2569767@sentry.io/254283').install();
console.log("Raven configured");
});

