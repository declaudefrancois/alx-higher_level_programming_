#!/usr/bin/node
/**
 * computes the number of tasks completed by user id.
 */
const request = require('request');

const url = process.argv[2];
request(url, (error, res, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (res && res.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTodos = todos.filter(todo => todo.completed).reduce((acc, current) => {
      if (acc[current.userId] === undefined) {
        acc[current.userId] = 0;
      }
      ++acc[current.userId];
      return acc;
    }, {});
    console.log(completedTodos);
  }
});
