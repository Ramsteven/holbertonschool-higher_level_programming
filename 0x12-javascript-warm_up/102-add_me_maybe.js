#!/usr/bin/node
exports.addMeMaybe = function addMeMaybe (number, func) {
  func(++number);
};
