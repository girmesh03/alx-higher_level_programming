#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
const apiUrl = process.argv[2];

// The request must be made to this URL with the user ID 1
const request = require('request');

// Make the request and print the number of tasks completed by user id
request(apiUrl, function (error, _response, body) {
  // If an error occurred during the request, print the error object
  if (error) {
    console.error(error);
  } else {
    // otherwise, print the number of tasks completed by user id
    const todos = JSON.parse(body);
    const completed = {};
    for (const todo of todos) {
      if (todo.completed) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId]++;
        }
      }
    }
    console.log(completed);
  }
});
