const { dependencies, ..._ } = require('./help')

const [a,b, ...args] = process.argv;

_.run(`pip remove ${args.join(' ')}`).then(dependencies.update)