Microservice for Macro Tracker

Table of contents

•	Introduction
•	Requirements

Introduction
  Microservice for Macro Tracker

Requirements
  The Microservice that will be implemented with partner's Macro Tracker app is, Sockets.

  The user will request data by entering information in the app's UI, in which the client will then send the information to the server. The server receives 
  and interprets the information and pulls the data (response) either from an API or json file. The server responds by sending the data to the client
  providing the data the user is requesting. The data is sent to the client, through the app's UI.
  
  Example:
  User enters a protein to get the grams of protein is has, example: chicken
  Message received by Server: 'Meal entered by client is:  chicken'
  Message sent to Client: "Protein amount is:  xx grams'
