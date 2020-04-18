const { dependencies, ..._ } = require('./help')

const [a,b, ...args] = process.argv;

_.run(`echo pip install ${args.join(' ')}`).then(dependencies.update);