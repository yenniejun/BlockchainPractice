let SHA256 = require('crypto-js/SHA256');

class Block {
	constructor(timestamp, data, previousHash = '') {
		this.timestamp = timestamp;
		this.data = data;
		this.previousHash = previousHash;
		this.index = 0;
		this.hash = this.calculateHash();
		this.nonce = 0; //this is for mining
	}

	calculateHash() {
		return SHA256(this.index + this.timestamp + JSON.stringify(this.data) + this.previousHash + this.nonce).toString();
	}

	mineBlock(difficulty) {
		while (this.hash.substring(0, difficulty) !== Array(difficulty + 1).join('0')) {
			this.nonce++;
			this.hash = this.calculateHash();
		}

		console.log('Block mined: ' + this.hash);
	}
}

class Blockchain {
	constructor() {
		this.chain = [this.createGenesisBlock()];
		this.difficulty = 6;
	}

	printChain() {
		console.log(JSON.stringify(this.chain, null, 2));
	}

	printBlockAtIndex(index) {
		console.log(JSON.stringify(this.getBlockAtIndex(index), null, 2));
	}

	printIsChainValid() {
		this.isChainValid() ?
			console.log('Chain is valid.') :
			console.log('Chain is not valid.');
	}

	createGenesisBlock() {
		return new Block(0, '2019/09/01', 'Genesis', '0');
	}

	getLatestBlock() {
		return this.chain[this.chain.length - 1];
	}

	getBlockAtIndex(index) {
		return this.chain.find(x => x.index === index);
	}

	addNewBlock(newBlock) {
		newBlock.previousHash = this.getLatestBlock().hash;
		newBlock.index = this.getLatestBlock().index + 1;
		newBlock.mineBlock(this.difficulty);;
		this.chain.push(newBlock);
	}

	isChainValid() {
		let previousBlock = this.chain[0]; 
		let currentBlock = null; 

		for (let i = 1; i < this.chain.length; i++) {
			currentBlock = this.chain[i];
			
			if (currentBlock.hash !== currentBlock.calculateHash()) {
				return false;
			}

			if (currentBlock.previousHash !== previousBlock.hash) {
				return false;
			}

			previousBlock = currentBlock;

			return true;
		}
	}
}

let YenCoin = new Blockchain();

console.log('Mining Block 1...');
YenCoin.addNewBlock(new Block(Date.now, 'Hello!'));

console.log('Mining Block 2...');
YenCoin.addNewBlock(new Block(Date.now, {amount: 100}));

YenCoin.printChain();
//YenCoin.printBlockAtIndex(2);
//YenCoin.printIsChainValid();


