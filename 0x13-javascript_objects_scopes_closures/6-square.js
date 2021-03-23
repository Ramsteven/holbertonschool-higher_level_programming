#!/usr/bin/node
const SquareClass = require('./5-square');
class Square extends SquareClass {
	constructor(size) {
		super(size, size);
	}

	charPrint(c) {
		if (c == undefined) {
			c = 'X';
		}

		for (let x = 0; x < this.width; x++) {
			console.log(c.repeat(this.width));
		}
	}
}

module.exports = Square;
