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
    const completedTodos = new Map();
    JSON.parse(body).forEach(todo => {
      if (todo.completed) {
        const current = completedTodos.get(todo.userId);
        completedTodos.set(todo.userId, typeof current === 'number' ? current + 1 : 1);
      }
    });

    const users = Array.from(completedTodos);
    const usersLength = users.length;
    for (let i = 0; i < usersLength; i++) {
      const start = i === 0 ? '{' : ' ';
      const end = i === usersLength - 1 ? ' }' : ',';
      console.log(`${start} '${users[i][0]}': ${users[i][1]}${end}`);
    }

    if (usersLength === 0) { console.log("{ }"); }
  }
});
