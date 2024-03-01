const express = require('express');
const app = express();
const port = 3000;

app.use(express.static('public')); // Serve static files from 'public' directory
app.use(express.urlencoded({ extended: true })); // for parsing application/x-www-form-urlencoded

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});

const multer = require('multer');
const upload = multer({ dest: 'uploads/' }); // Make sure the 'uploads' directory exists 
({
    dest: 'uploads/',
    limits: { fileSize: 10 * 1024 * 1024 }, // for example, 10 MB
  });
  
app.post('/upload', upload.single('contentFile'), (req, res) => {
  // Your handling code here
});


app.post('/upload', upload.single('contentFile'), (req, res) => {
  console.log('File uploaded:', req.file);
  res.send('File uploaded successfully');
});


app.post('/upload', upload.single('contentFile'), (req, res) => {
  console.log('File uploaded:', req.file);
  // Add your file processing logic here
  res.send('File uploaded successfully');
});

const nodemailer = require('nodemailer');

app.post('/contact', (req, res) => {
  const { name, email, message } = req.body;
  // Set up your transporter and mail options
  // Send the email and respond accordingly
});
